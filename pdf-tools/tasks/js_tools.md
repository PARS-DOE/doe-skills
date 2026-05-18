# JavaScript PDF helpers (pdf-lib, pdfjs-dist)

These tools are for things Python libraries often struggle with:
- filling and flattening AcroForm fields reliably across viewers
- getting text extraction similar to what browsers do (pdfjs)

---

## Dependencies

Node dependencies (pdf-lib, pdfjs-dist) are pre-installed in the workspace.

If Node.js tools are unavailable for any reason, fall back to the Python helpers:
- Form fill (best-effort): `python skills/pdf-tools/scripts/pdf_edit.py fill-form in.pdf --values values.json -o out.pdf`
- Text extraction: `python skills/pdf-tools/scripts/pdf_extract.py text in.pdf --method pdfplumber`

---

## Fill form (pdf-lib)

```bash
node skills/pdf-tools/js/fill_form.mjs --input in.pdf --values values.json --output out.pdf --flatten
```

`values.json` example:

```json
{
  "name": "Ada Lovelace",
  "agree": true,
  "state": "CA"
}
```

---

## List fields (pdf-lib)

```bash
node skills/pdf-tools/js/extract_form_fields.mjs --input in.pdf
```

---

## Extract text (pdfjs)

```bash
node skills/pdf-tools/js/extract_text_pdfjs.mjs --input in.pdf > text.txt
```

Tip: prefer Python-based extraction for coordinates/layout (`pdf_extract.py text --layout_json ...`) and use pdfjs text as a cross-check.