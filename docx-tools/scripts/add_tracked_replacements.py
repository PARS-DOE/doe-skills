#!/usr/bin/env python3
"""Add tracked changes to a DOCX file.

Supports three operations:
  --replace "OLD=NEW"       Find-and-replace with tracked deletion + insertion
  --insert "TEXT"           Append a tracked insertion paragraph
  --delete "SEARCH TEXT"    Delete the first paragraph containing SEARCH TEXT

All changes appear as Word tracked changes (redlines) with author and timestamp.
Uses docx-revisions for robust cross-run text matching.

Usage
-----
# Simple replacements (handles text split across multiple runs)
python scripts/add_tracked_replacements.py in.docx --out out.docx \
  --replace "foo=bar" --replace "old phrase=new phrase" \
  --author "Walt"

# Add a new paragraph at the end
python scripts/add_tracked_replacements.py in.docx --out out.docx \
  --insert "This paragraph was added by the reviewer." \
  --author "Walt"

# Delete a paragraph by matching its text
python scripts/add_tracked_replacements.py in.docx --out out.docx \
  --delete "Remove this paragraph" \
  --author "Walt"

# Combine operations
python scripts/add_tracked_replacements.py in.docx --out out.docx \
  --replace "draft=final" \
  --insert "Reviewed and approved." \
  --delete "TODO: remove before publishing" \
  --author "Walt"
"""

from __future__ import annotations

import argparse
import datetime as _dt

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx_revisions import RevisionDocument


def _enable_track_revisions(rdoc: RevisionDocument) -> None:
    """Ensure trackRevisions is enabled in settings.xml."""
    settings = rdoc.document.settings.element
    if settings.find(qn("w:trackRevisions")) is None:
        settings.append(OxmlElement("w:trackRevisions"))


def _do_replacements(
    rdoc: RevisionDocument, replaces: list[tuple[str, str]], author: str
) -> int:
    total = 0
    for old, new in replaces:
        count = rdoc.find_and_replace_tracked(old, new, author=author)
        if count:
            print(f"  replaced {old!r} -> {new!r} ({count}x)")
        else:
            print(f"  WARNING: {old!r} not found in document")
        total += count
    return total


def _do_insertions(
    rdoc: RevisionDocument, texts: list[str], author: str
) -> int:
    for text in texts:
        last_para = rdoc.paragraphs[-1] if rdoc.paragraphs else None
        if last_para is not None:
            # Add tracked insertion as new content at end of last paragraph,
            # preceded by a line break to start a new visual line
            last_para.add_tracked_insertion(f"\n{text}", author=author)
        print(f"  inserted paragraph: {text[:60]!r}...")
    return len(texts)


def _do_deletions(
    rdoc: RevisionDocument, searches: list[str], author: str
) -> int:
    total = 0
    for search in searches:
        found = False
        for para in rdoc.paragraphs:
            if search in para.text:
                # Delete the entire paragraph text as a tracked deletion
                para.add_tracked_deletion(0, len(para.text), author=author)
                print(f"  deleted paragraph containing: {search[:60]!r}")
                found = True
                total += 1
                break
        if not found:
            print(f"  WARNING: no paragraph containing {search!r}")
    return total


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Add tracked changes to a DOCX (replacements, insertions, deletions)"
    )
    ap.add_argument("in_docx", help="Input DOCX file")
    ap.add_argument("--out", required=True, help="Output DOCX file")
    ap.add_argument("--author", default="Walt", help="Author name for tracked changes")
    ap.add_argument(
        "--replace",
        action="append",
        default=[],
        help="Replacement as OLD=NEW (repeatable)",
    )
    ap.add_argument(
        "--insert",
        action="append",
        default=[],
        help="Text to insert as new tracked paragraph (repeatable)",
    )
    ap.add_argument(
        "--delete",
        action="append",
        default=[],
        help="Search text to find and delete paragraph (repeatable)",
    )
    args = ap.parse_args()

    if not args.replace and not args.insert and not args.delete:
        raise SystemExit("Provide at least one --replace, --insert, or --delete")

    replaces: list[tuple[str, str]] = []
    for rpl in args.replace:
        if "=" not in rpl:
            raise SystemExit(f"--replace must be OLD=NEW, got: {rpl!r}")
        old, new = rpl.split("=", 1)
        replaces.append((old, new))

    rdoc = RevisionDocument(args.in_docx)
    _enable_track_revisions(rdoc)

    total = 0
    if replaces:
        total += _do_replacements(rdoc, replaces, args.author)
    if args.delete:
        total += _do_deletions(rdoc, args.delete, args.author)
    if args.insert:
        total += _do_insertions(rdoc, args.insert, args.author)

    rdoc.save(args.out)
    print(f"[OK] wrote {args.out} (changes={total})")


if __name__ == "__main__":
    main()
