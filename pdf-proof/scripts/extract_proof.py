#!/usr/bin/env python3
"""
extract_proof.py — Extract cropped, highlighted screenshots from PDF documents
and assemble them into a self-contained HTML proof page.

Three steps, all required:

  1. find     — Locate where text appears in a PDF (page numbers + coordinates)
  2. verify   — Extract a highlighted screenshot, cross-check the text, save
                result (including base64 image) to a JSON file
  3. assemble — Read result files + a manifest, produce a self-contained HTML
                proof page with all images embedded as data URIs

Usage:
  # Step 1: Find where text appears
  python3 extract_proof.py --mode find --pdf doc.pdf --search "1,250.00"

  # Step 2: Verify and save result to file
  python3 extract_proof.py --mode verify --pdf doc.pdf --search "1,250.00" \
    --page 3 --output proof.png --result-file result.json --json

  # Step 3: Assemble HTML from manifest
  python3 extract_proof.py --mode assemble --manifest manifest.json \
    --output proof.html
"""

import argparse
import base64
import json
import sys
import os
import re
import unicodedata
from io import BytesIO


# ---------------------------------------------------------------------------
# Text normalization helpers
# ---------------------------------------------------------------------------

_LIGATURE_MAP = {
    "\ufb00": "ff",
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
    "\ufb05": "st",
    "\ufb06": "st",
}

_INVISIBLE_CHARS = "\u00ad\u200b\u200c\u200d\u2060\ufeff"


def _normalize_text_for_search(text):
    """Normalize text for searching: Unicode NFC, ligature decomposition,
    and invisible character removal."""
    text = unicodedata.normalize("NFC", text)
    for lig, replacement in _LIGATURE_MAP.items():
        text = text.replace(lig, replacement)
    for ch in _INVISIBLE_CHARS:
        text = text.replace(ch, "")
    return text


import fitz
from PIL import Image, ImageDraw


# ---------------------------------------------------------------------------
# OCR helpers
# ---------------------------------------------------------------------------

def _has_text_layer(page):
    """Check whether a page has an embedded text layer (not scanned-only)."""
    text = page.get_text("text").strip()
    return len(text) > 20  # Arbitrary threshold — a real text layer has content


def _ocr_search(page, search_text):
    """Use Tesseract OCR via PyMuPDF to search a scanned/image-only page.

    Returns a list of fitz.Rect objects, same as page.search_for().
    Requires tesseract to be installed on the system.
    """
    try:
        tp = page.get_textpage_ocr(
            language="eng",
            dpi=300,
            full=True,
        )
        # search_for with a pre-built textpage
        areas = page.search_for(search_text, textpage=tp)
        return areas, True
    except Exception as e:
        print(f"  OCR failed: {e}", file=sys.stderr)
        print("  Install tesseract for scanned PDF support: "
              "apt-get install tesseract-ocr", file=sys.stderr)
        return [], False


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def find_text(pdf_path, search_text, page_num=None, ocr=False):
    """
    Search for text in a PDF. Returns list of dicts with page number and rect.
    If page_num is given (1-indexed), only searches that page.
    If ocr=True, falls back to Tesseract OCR for pages without a text layer.
    """
    doc = fitz.open(pdf_path)
    results = []
    ocr_used = False

    pages_to_search = range(len(doc))
    if page_num is not None:
        pages_to_search = [page_num - 1]

    for p_idx in pages_to_search:
        if p_idx < 0 or p_idx >= len(doc):
            continue
        page = doc[p_idx]

        # Try normal text search first
        areas = page.search_for(search_text)

        # If no results, try text-normalized form (Unicode NFC, ligatures, etc.)
        if not areas:
            normalized = _normalize_text_for_search(search_text)
            if normalized != search_text:
                areas = page.search_for(normalized)

        # If no results and OCR is enabled, try OCR on pages without text
        if not areas and ocr and not _has_text_layer(page):
            print(f"  Page {p_idx + 1}: no text layer detected, running OCR...",
                  file=sys.stderr)
            areas, ocr_ok = _ocr_search(page, search_text)
            if ocr_ok:
                ocr_used = True

        for area in areas:
            results.append({
                "page": p_idx + 1,
                "page_idx": p_idx,
                "rect": area,
                "x0": round(area.x0, 2),
                "y0": round(area.y0, 2),
                "x1": round(area.x1, 2),
                "y1": round(area.y1, 2),
                "ocr": ocr_used,
            })

    doc.close()
    return results


def _select_match(areas, match_index, prefer, search_text, page_num):
    """Pick the best match from a list of fitz.Rect results.

    Returns (selected_rect, index, confidence, note).
    Confidence: "high" if single match, "medium" if auto-selected from
    multiple, "low" if a fallback variation was used.
    """
    if match_index is not None and 0 <= match_index < len(areas):
        return areas[match_index], match_index, "high", "Explicit match index"

    if len(areas) == 1:
        return areas[0], 0, "high", "Single match on page"

    # Multiple matches — print warning and auto-select
    print(f"  WARNING: {len(areas)} matches for '{search_text}' on page {page_num}:",
          file=sys.stderr)
    for i, a in enumerate(areas):
        rightmost = a.x0 == max(r.x0 for r in areas)
        print(f"    [{i}] x={a.x0:.0f}, y={a.y0:.0f}"
              f"{'  (rightmost)' if rightmost else ''}",
              file=sys.stderr)

    if prefer == "right":
        selected = max(areas, key=lambda r: r.x0)
    elif prefer == "last":
        selected = areas[-1]
    else:
        selected = areas[0]

    sel_idx = areas.index(selected)
    print(f"  -> Using match [{sel_idx}] (--prefer {prefer}). "
          f"Override with --match-index N if wrong.", file=sys.stderr)
    return selected, sel_idx, "medium", f"Auto-selected ({prefer}) from {len(areas)} matches"


def _find_text_in_page(page, search_text):
    """Extract full page text and find the search string with flexible matching.

    Strips invisible characters and normalizes Unicode on both sides, then
    returns the *actual text as it appears in the PDF* so it can be fed back
    to page.search_for() for precise coordinates.  Returns None if not found.
    """
    page_text = page.get_text("text")
    if not page_text:
        return None

    norm_page = unicodedata.normalize("NFC", page_text)
    norm_search = _normalize_text_for_search(search_text)

    # Fast path: case-insensitive find on NFC-normalized text
    idx = norm_page.lower().find(norm_search.lower())
    if idx >= 0:
        return norm_page[idx:idx + len(norm_search)]

    # Slow path: strip invisible chars, build index map back to original
    invisible = set(_INVISIBLE_CHARS)
    clean_map = []  # clean_idx -> original_idx
    clean_chars = []
    for orig_idx, ch in enumerate(norm_page):
        if ch not in invisible:
            clean_map.append(orig_idx)
            clean_chars.append(ch)
    clean_text = "".join(clean_chars)

    idx = clean_text.lower().find(norm_search.lower())
    if idx >= 0 and idx + len(norm_search) <= len(clean_map):
        orig_start = clean_map[idx]
        orig_end = clean_map[idx + len(norm_search) - 1] + 1
        return norm_page[orig_start:orig_end]

    return None


def _try_variations(page, search_text, ocr=False):
    """Try common formatting variations of the search text.

    Returns (areas, variation_used, is_fallback, used_ocr).
    """
    used_ocr = False

    def _search(text):
        return page.search_for(text)

    # Phase 0: Exact match
    areas = _search(search_text)
    if areas:
        return areas, search_text, False, False

    # Phase 1: Text-normalized search (Unicode NFC, ligatures, invisible chars)
    normalized = _normalize_text_for_search(search_text)
    if normalized != search_text:
        areas = _search(normalized)
        if areas:
            return areas, normalized, True, False

    # Phase 2: Page-text-extraction fallback — find actual PDF string flexibly
    found_actual = _find_text_in_page(page, search_text)
    if found_actual and found_actual != search_text and found_actual != normalized:
        areas = _search(found_actual)
        if areas:
            return areas, found_actual, True, False

    # Phase 3: Numeric/financial formatting variations
    variations = [
        search_text.replace(",", ""),
        f"({search_text})",
        f"({search_text}.)",
        search_text + ".",
        "-" + search_text,
        search_text.lstrip("-"),
        search_text.replace("$", ""),
        search_text.replace("$", "").replace(",", ""),
    ]
    seen = {search_text, normalized}
    if found_actual:
        seen.add(found_actual)
    for v in variations:
        if v not in seen:
            seen.add(v)
            areas = _search(v)
            if areas:
                return areas, v, True, False

    # Phase 4: OCR fallback (for scanned/image-only pages)
    if ocr and not _has_text_layer(page):
        print(f"  No text layer — running OCR...", file=sys.stderr)
        areas, ocr_ok = _ocr_search(page, search_text)
        if areas:
            return areas, search_text, False, True
        if ocr_ok:
            for v in variations:
                if v in seen:
                    areas, _ = _ocr_search(page, v)
                    if areas:
                        return areas, v, True, True

    return [], None, False, False


def _read_text_at_rect(page, rect, expand=2):
    """Extract the actual text content at a given rectangle.

    Expands the rect slightly to ensure full character capture.
    Returns the extracted text string.
    """
    expanded = fitz.Rect(
        rect.x0 - expand,
        rect.y0 - expand,
        rect.x1 + expand,
        rect.y1 + expand,
    )
    words = page.get_text("words")
    matched = []
    for w in words:
        wr = fitz.Rect(w[:4])
        if wr.intersects(expanded):
            matched.append(w[4])
    return " ".join(matched)


def _normalize_for_comparison(text):
    """Normalize text for fuzzy comparison (Unicode, ligatures, invisible chars,
    whitespace, punctuation, case)."""
    text = _normalize_text_for_search(text)
    return re.sub(r"[\s,$().%-]+", "", text).lower()


def extract_crop(pdf_path, search_text, page_num, output_path,
                 highlight="value", context=80, scale=5, pad=8,
                 margin_left=30, margin_right=10, match_index=None,
                 prefer="right", verify=False, ocr=False):
    """
    Extract a cropped region from a PDF page centered on the found text,
    with a precise highlight drawn at the exact text coordinates.

    search_text can be a single string or a list of strings. When a list is
    given, each term gets its own highlight and the crop spans all of them.

    Returns:
        dict with result info including confidence and optional verification
    """
    # Normalise to list so the rest of the code is uniform
    search_terms = [search_text] if isinstance(search_text, str) else list(search_text)

    doc = fitz.open(pdf_path)
    page_idx = page_num - 1

    if page_idx < 0 or page_idx >= len(doc):
        doc.close()
        return {"error": f"Page {page_num} out of range (PDF has {len(doc)} pages)"}

    page = doc[page_idx]
    page_rect = page.rect

    # --- locate every search term and pick the best match for each ----------
    matched_rects = []   # (rect, term, sel_idx, confidence, note, variation)
    errors = []

    for term in search_terms:
        areas, variation_used, is_fallback, used_ocr = _try_variations(
            page, term, ocr=ocr
        )
        if not areas:
            errors.append(term)
            continue

        text_rect, sel_idx, confidence, confidence_note = _select_match(
            areas, match_index, prefer, term, page_num
        )
        if is_fallback and confidence == "high":
            confidence = "medium"
            confidence_note += f" (matched variation '{variation_used}')"
        if used_ocr and confidence == "high":
            confidence = "medium"
            confidence_note += " (via OCR)"

        matched_rects.append({
            "rect": text_rect,
            "term": term,
            "sel_idx": sel_idx,
            "total_matches": len(areas),
            "confidence": confidence,
            "confidence_note": confidence_note,
            "variation": variation_used if is_fallback else None,
            "ocr": used_ocr,
        })

    if not matched_rects:
        doc.close()
        return {"error": f"Text not found on page {page_num}: {errors}"}

    # --- compute crop region spanning all matched rects ---------------------
    all_y0 = min(m["rect"].y0 for m in matched_rects)
    all_y1 = max(m["rect"].y1 for m in matched_rects)

    crop_x0 = margin_left
    crop_y0 = max(0, all_y0 - context)
    crop_x1 = page_rect.width - margin_right
    crop_y1 = min(page_rect.height, all_y1 + context)

    crop = fitz.Rect(crop_x0, crop_y0, crop_x1, crop_y1)

    # --- render -------------------------------------------------------------
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat, clip=crop)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # --- draw highlights for every matched rect ----------------------------
    if highlight != "none":
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)

        for m in matched_rects:
            r = m["rect"]
            if highlight == "value":
                hx0 = (r.x0 - pad - crop_x0) * scale
                hy0 = (r.y0 - pad - crop_y0) * scale
                hx1 = (r.x1 + pad - crop_x0) * scale
                hy1 = (r.y1 + pad - crop_y0) * scale
            elif highlight == "row":
                hx0 = (crop_x0 + 5 - crop_x0) * scale
                hy0 = (r.y0 - pad - crop_y0) * scale
                hx1 = (crop_x1 - 5 - crop_x0) * scale
                hy1 = (r.y1 + pad - crop_y0) * scale

            overlay_draw.rectangle(
                [hx0, hy0, hx1, hy1],
                fill=(249, 115, 22, 80),  # soft orange, ~31% opacity
            )

        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    # --- save ---------------------------------------------------------------
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    img.save(output_path)

    # --- encode base64 for embedding in HTML --------------------------------
    buf = BytesIO()
    img.save(buf, format="PNG")
    img_base64 = base64.b64encode(buf.getvalue()).decode("ascii")

    # --- build result -------------------------------------------------------
    primary = matched_rects[0]
    result = {
        "output": output_path,
        "image_base64": img_base64,
        "page": page_num,
        "search_text": search_terms[0] if len(search_terms) == 1 else search_terms,
        "found_at": {
            "x0": round(primary["rect"].x0, 2),
            "y0": round(primary["rect"].y0, 2),
            "x1": round(primary["rect"].x1, 2),
            "y1": round(primary["rect"].y1, 2),
        },
        "highlights": len(matched_rects),
        "confidence": min((m["confidence"] for m in matched_rects),
                          key=lambda c: ["high", "medium", "low"].index(c)),
        "image_size": {"width": img.width, "height": img.height},
    }

    if errors:
        result["not_found"] = errors

    if len(matched_rects) > 1:
        result["matched_terms"] = [
            {"term": m["term"],
             "confidence": m["confidence"],
             "confidence_note": m["confidence_note"]}
            for m in matched_rects
        ]

    # --- verification (for each term) --------------------------------------
    if verify:
        verifications = []
        all_pass = True
        for m in matched_rects:
            readback = _read_text_at_rect(page, m["rect"])
            norm_search = _normalize_for_comparison(m["term"])
            norm_readback = _normalize_for_comparison(readback)
            text_match = norm_search in norm_readback or norm_readback in norm_search
            if not text_match:
                all_pass = False
                print(f"  VERIFY FAIL: searched '{m['term']}', "
                      f"readback '{readback}'", file=sys.stderr)
            verifications.append({
                "search_text": m["term"],
                "readback_text": readback,
                "text_match": text_match,
                "status": "pass" if text_match else "fail",
            })

        result["verification"] = verifications if len(verifications) > 1 else verifications[0]
        if not all_pass:
            result["confidence"] = "low"

    doc.close()
    return result


# ---------------------------------------------------------------------------
# HTML assembly
# ---------------------------------------------------------------------------

def _build_summary_row(proof):
    """Build one <tr> for the summary table."""
    value = proof.get("value", "")
    neg_cls = ' class="negative"' if proof.get("is_negative") else ""
    source = proof.get("source", "")
    field = proof.get("field", proof.get("label", ""))
    return (
        f'<tr>'
        f'<td class="field">{field}</td>'
        f'<td class="value"{neg_cls}>{value}</td>'
        f'<td class="source">{source}</td>'
        f'</tr>'
    )


def _confidence_badge(conf):
    """Return the HTML for a confidence badge."""
    labels = {"high": "Verified", "medium": "Unverified", "low": "Check"}
    label = labels.get(conf, conf)
    return f'<span class="confidence-badge confidence-{conf}">{label}</span>'


def _build_proof_card(proof):
    """Build one proof card HTML block."""
    label = proof.get("label", "")
    value = proof.get("value", "")
    page = proof.get("page", "")
    conf = proof.get("confidence", "medium")
    desc = proof.get("description", "")
    verification = proof.get("verification")
    img_b64 = proof.get("image_base64", "")

    parts = []
    parts.append('<div class="proof-card">')
    parts.append('<div class="proof-header">')
    parts.append(f'<h3>{label}: <span class="highlight">{value}</span></h3>')
    if page:
        parts.append(f'<span class="badge">Page {page}</span>')
    parts.append(_confidence_badge(conf))
    parts.append('</div>')
    parts.append('<div class="proof-body">')
    if desc:
        parts.append(f'<p>{desc}</p>')
    if img_b64:
        parts.append('<div class="screenshot">')
        parts.append(f'<img src="data:image/png;base64,{img_b64}" alt="Proof screenshot">')
        parts.append('</div>')
    if verification:
        parts.append('<details class="verification">')
        parts.append('<summary>Extraction details</summary>')
        parts.append(f'<div class="math">{verification}</div>')
        parts.append('</details>')
    parts.append('</div>')
    parts.append('</div>')
    return "\n".join(parts)


def assemble_html(manifest_path, template_path, output_path):
    """Read a JSON manifest and HTML template, produce a self-contained proof page.

    The manifest references extraction result files that contain the base64 image
    data. This keeps image data out of Walt's context — Walt writes a small manifest
    with metadata, the script handles the heavy image data internally.

    Manifest JSON schema:
    {
      "title": "...",
      "subtitle": "...",
      "summary_heading": "Values Verified",
      "proofs": [
        {
          "label": "Field Name",
          "field": "Source ref",
          "value": "$1,250.00",
          "is_negative": false,
          "source": "Document, page N",
          "description": "Context about this value.",
          "result_file": "proof-output/result_bcwp.json",
          "confidence": "high",
          "verification": "Searched: '1,250.00' → Readback: '1,250.00' ✓"
        }
      ],
      "footnote": "Generated by pdf-proof skill."
    }

    Each proof entry MUST have a "result_file" pointing to a JSON file saved by
    --result-file during the verify step. The assemble step reads image data
    from these files — image data never passes through the caller's context.
    """
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    with open(template_path, "r") as f:
        template = f.read()

    title = manifest.get("title", "Document Verification Proof")
    subtitle = manifest.get("subtitle", "")
    heading = manifest.get("summary_heading", "Values Verified")
    proofs = manifest.get("proofs", [])
    footnote = manifest.get("footnote", "")

    # Load image data from result files
    manifest_dir = os.path.dirname(os.path.abspath(manifest_path))
    for p in proofs:
        result_file = p.get("result_file")
        if not result_file:
            print(f"  WARNING: proof '{p.get('label', '?')}' has no result_file — "
                  f"screenshot will be missing", file=sys.stderr)
            continue

        if not os.path.isabs(result_file):
            result_file = os.path.join(manifest_dir, result_file)

        if not os.path.exists(result_file):
            print(f"  WARNING: result file not found: {result_file}", file=sys.stderr)
            continue

        with open(result_file, "r") as rf:
            result_data = json.load(rf)

        if result_data.get("image_base64"):
            p["image_base64"] = result_data["image_base64"]

        # Auto-populate page from result if not in manifest
        if not p.get("page") and result_data.get("page"):
            p["page"] = result_data["page"]

        # Derive confidence from verification status, not match heuristics.
        # The raw "confidence" field in result JSON reflects things like
        # multiple matches or OCR — it should NOT determine the badge.
        verification = result_data.get("verification")
        if isinstance(verification, dict):
            if verification.get("text_match") and verification.get("status") == "pass":
                p["confidence"] = "high"
            elif verification.get("status") == "fail":
                p["confidence"] = "low"
            else:
                p["confidence"] = "medium"
        elif isinstance(verification, list):
            # Multiple search terms — all must pass
            all_pass = all(
                v.get("text_match") and v.get("status") == "pass"
                for v in verification
            )
            any_fail = any(v.get("status") == "fail" for v in verification)
            if all_pass:
                p["confidence"] = "high"
            elif any_fail:
                p["confidence"] = "low"
            else:
                p["confidence"] = "medium"
        elif not p.get("confidence"):
            p["confidence"] = "medium"

        # Auto-generate verification text if manifest omits it
        if not p.get("verification") and verification:
            if isinstance(verification, dict):
                search = verification.get("search_text", "")
                readback = verification.get("readback_text", "")
                if verification.get("text_match"):
                    p["verification"] = (
                        f"Searched: '{search}' → Readback: '{readback}' ✓"
                    )
                else:
                    p["verification"] = (
                        f"Searched: '{search}' → Readback: '{readback}' ✗ "
                        f"(verification failed)"
                    )
            elif isinstance(verification, list):
                lines = []
                for v in verification:
                    search = v.get("search_text", "")
                    readback = v.get("readback_text", "")
                    mark = "✓" if v.get("text_match") else "✗"
                    lines.append(f"'{search}' → '{readback}' {mark}")
                p["verification"] = "\n".join(lines)

    # Build content
    content_parts = []
    content_parts.append(f"<h1>{title}</h1>")
    if subtitle:
        content_parts.append(f'<p class="subtitle">{subtitle}</p>')

    # Summary table
    content_parts.append('<div class="summary-box">')
    content_parts.append(f"<h2>{heading}</h2>")
    content_parts.append('<table class="summary-table">')
    content_parts.append("<thead><tr><th>Field</th><th>Value</th><th>Source</th></tr></thead>")
    content_parts.append("<tbody>")
    for p in proofs:
        content_parts.append(_build_summary_row(p))
    content_parts.append("</tbody></table></div>")

    # Proof cards
    for p in proofs:
        content_parts.append(_build_proof_card(p))

    if footnote:
        content_parts.append(f'<p class="footnote">{footnote}</p>')

    content = "\n".join(content_parts)

    # Inject into template
    html = template.replace("{{TITLE}}", title).replace("{{CONTENT}}", content)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)

    print(f"Proof page saved: {output_path} ({len(proofs)} proof(s))")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract cropped, highlighted screenshots from PDFs"
    )
    parser.add_argument("--pdf", help="Path to the PDF file")
    parser.add_argument("--search", nargs="+",
                        help="Text to search for (multiple terms = multiple "
                             "highlights on the same screenshot)")
    parser.add_argument("--mode", required=True,
                        choices=["find", "verify", "assemble", "quick-proof"],
                        help="'find' to locate text, "
                             "'verify' to extract highlighted screenshot + cross-check, "
                             "'assemble' to build HTML proof page from manifest, "
                             "'quick-proof' to do find+verify+assemble in one shot")
    parser.add_argument("--page", type=int, default=None,
                        help="1-indexed page number (required for verify)")
    parser.add_argument("--output", default="proof.png",
                        help="Output path (PNG for verify, HTML for assemble)")
    parser.add_argument("--highlight", default="value",
                        choices=["value", "row", "none"],
                        help="Highlight style")
    parser.add_argument("--context", type=int, default=80,
                        help="Vertical context in PDF points (default: 80)")
    parser.add_argument("--scale", type=int, default=5,
                        help="Render scale factor (default: 5)")
    parser.add_argument("--prefer", default="right",
                        choices=["right", "first", "last"],
                        help="When multiple matches: 'right' (rightmost, best for "
                             "forms), 'first', or 'last' (default: right)")
    parser.add_argument("--match-index", type=int, default=None,
                        help="Use the Nth match (0-indexed), overrides --prefer")
    parser.add_argument("--ocr", action="store_true",
                        help="Enable OCR fallback for scanned/image-only PDFs "
                             "(requires tesseract)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON")
    parser.add_argument("--result-file", default=None,
                        help="Save full extraction result (including base64 image) "
                             "to this JSON file instead of printing it. Stdout "
                             "receives only a short summary. Use with assemble mode.")
    parser.add_argument("--manifest", default=None,
                        help="Path to JSON manifest (assemble mode)")
    parser.add_argument("--template", default=None,
                        help="Path to HTML template (assemble mode)")
    # quick-proof args
    parser.add_argument("--label", default=None,
                        help="Proof card label (quick-proof mode)")
    parser.add_argument("--field", default=None,
                        help="Field/source reference (quick-proof mode)")
    parser.add_argument("--value", default=None,
                        help="Display value for the proof card (quick-proof mode)")
    parser.add_argument("--source", default=None,
                        help="Source citation text (quick-proof mode)")
    parser.add_argument("--description", default=None,
                        help="Description text for the proof card (quick-proof mode)")
    parser.add_argument("--title", default=None,
                        help="Proof page title (quick-proof mode)")
    parser.add_argument("--output-html", default=None,
                        help="Output HTML path (quick-proof mode)")

    args = parser.parse_args()

    if args.mode == "assemble":
        if not args.manifest:
            print("Error: --manifest is required for assemble mode", file=sys.stderr)
            sys.exit(1)
        template = args.template
        if not template:
            # Default: look for template relative to this script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            template = os.path.join(script_dir, "..", "assets", "proof_template.html")
        assemble_html(args.manifest, template, args.output)
        return

    if args.mode == "quick-proof":
        # Single-command: find → verify → assemble for one proof
        if not args.pdf:
            print("Error: --pdf is required", file=sys.stderr)
            sys.exit(1)
        if not args.search:
            print("Error: --search is required", file=sys.stderr)
            sys.exit(1)

        search = args.search[0] if len(args.search) == 1 else args.search
        output_html = args.output_html or "proof-output/proof.html"
        output_dir = os.path.dirname(output_html) or "proof-output"
        os.makedirs(output_dir, exist_ok=True)

        # Find
        first_term = args.search[0]
        page = args.page
        if page is None:
            find_results = find_text(args.pdf, first_term, ocr=args.ocr)
            if not find_results:
                print(f"Error: '{first_term}' not found in any page",
                      file=sys.stderr)
                sys.exit(1)
            page = find_results[0]["page"]
            print(f"Found on page {page}")

        # Verify
        png_path = os.path.join(output_dir, "proof.png")
        result_path = os.path.join(output_dir, "result.json")

        result = extract_crop(
            args.pdf, search, page, png_path,
            highlight=args.highlight,
            context=args.context,
            scale=args.scale,
            match_index=args.match_index,
            prefer=args.prefer,
            verify=True,
            ocr=args.ocr,
        )

        if "error" in result:
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)

        with open(result_path, "w") as rf:
            json.dump(result, rf, indent=2)

        # Build manifest in memory and write it
        search_label = first_term if isinstance(search, str) else " / ".join(args.search)
        pdf_name = os.path.basename(args.pdf)
        manifest = {
            "title": args.title or f"Document Verification — {search_label}",
            "proofs": [{
                "label": args.label or search_label,
                "field": args.field or search_label,
                "value": args.value or search_label,
                "source": args.source or f"{pdf_name}, page {page}",
                "description": args.description or "",
                "result_file": "result.json",
            }],
            "footnote": "Generated by pdf-proof skill.",
        }

        manifest_path = os.path.join(output_dir, "manifest.json")
        with open(manifest_path, "w") as mf:
            json.dump(manifest, mf, indent=2)

        # Assemble
        template = args.template
        if not template:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            template = os.path.join(script_dir, "..", "assets", "proof_template.html")

        assemble_html(manifest_path, template, output_html)
        return

    # All other modes require --pdf and --search
    if not args.pdf:
        print("Error: --pdf is required", file=sys.stderr)
        sys.exit(1)
    if not args.search:
        print("Error: --search is required", file=sys.stderr)
        sys.exit(1)

    # Normalise: single search term → string, multiple → list
    search = args.search[0] if len(args.search) == 1 else args.search

    if args.mode == "find":
        # Find mode: search for each term
        terms = args.search
        all_results = []
        for term in terms:
            results = find_text(args.pdf, term, args.page, ocr=args.ocr)
            for r in results:
                r["search_text"] = term
            all_results.extend(results)
        if args.json:
            for r in all_results:
                r["rect"] = str(r["rect"])
            print(json.dumps(all_results, indent=2))
        else:
            if not all_results:
                print(f"Not found: {terms}")
            else:
                for r in all_results:
                    print(f"  '{r.get('search_text', '')}' → "
                          f"Page {r['page']}: ({r['x0']}, {r['y0']}) "
                          f"to ({r['x1']}, {r['y1']})")

    elif args.mode == "verify":
        if not args.result_file:
            print("Error: --result-file is required for verify mode. "
                  "It stores the image data needed by the assemble step.",
                  file=sys.stderr)
            sys.exit(1)

        if args.page is None:
            # Auto-find page from first search term
            first_term = args.search[0]
            results = find_text(args.pdf, first_term, ocr=args.ocr)
            if not results:
                print(f"Error: '{first_term}' not found in any page",
                      file=sys.stderr)
                sys.exit(1)
            args.page = results[0]["page"]
            if not args.json:
                print(f"Auto-found on page {args.page}")

        result = extract_crop(
            args.pdf, search, args.page, args.output,
            highlight=args.highlight,
            context=args.context,
            scale=args.scale,
            match_index=args.match_index,
            prefer=args.prefer,
            verify=True,
            ocr=args.ocr,
        )

        if "error" in result:
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)

        # Save full result (with base64) to result file — this is the
        # only place image data is persisted. The assemble step reads it.
        os.makedirs(os.path.dirname(args.result_file) or ".", exist_ok=True)
        with open(args.result_file, "w") as rf:
            json.dump(result, rf, indent=2)

        # Print summary to stdout — never includes base64
        summary = {k: v for k, v in result.items() if k != "image_base64"}
        if args.json:
            print(json.dumps(summary, indent=2))
        else:
            conf = result["confidence"]
            conf_icon = {"high": "+", "medium": "~", "low": "!"}[conf]
            n = result.get("highlights", 1)
            print(f"Saved: {result['output']} "
                  f"({result['image_size']['width']}x"
                  f"{result['image_size']['height']}, "
                  f"{n} highlight{'s' if n > 1 else ''})")
            print(f"  Confidence: [{conf_icon}] {conf}")
            print(f"  Result file: {args.result_file}")


if __name__ == "__main__":
    main()
