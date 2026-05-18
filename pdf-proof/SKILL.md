---
name: pdf-proof
description: "Use this skill when the user needs visual proof that specific values exist in a document (PDF, DOCX, PPTX, XLSX) — not just to read a document, but to see exactly where a number, amount, clause, or field appears on the page with a highlighted screenshot. Trigger when someone is cross-referencing a document against something else (a form, a claim, a conversation, another document) and needs confirmation with evidence. Common signals: verifying earned value figures, checking contract terms, matching invoice line items, confirming assessment data against source documents, or cross-referencing PARS DMS documents. The core intent is 'show me the actual text in context' — not summarize, not extract all text, but produce a cropped screenshot with the value highlighted. Do NOT trigger for document operations without a specific value to locate: merging, splitting, summarizing, converting, or creating documents."
---

# PDF Proof Page Generator

This skill produces a self-contained HTML proof page showing highlighted screenshots of specific values found in documents. The user downloads one HTML file with all evidence embedded.

All commands run via the workspace command tool. The proof script is at `skills/pdf-proof/scripts/extract_proof.py`. Uploaded files are in `files/`, PARS DMS documents are in `dms/`.

## Non-PDF Documents

The proof script works on PDFs. For DOCX, PPTX, or XLSX files, convert to PDF first:

```bash
python3 skills/slides-tools/scripts/office/soffice.py \
  --headless --convert-to pdf --outdir proof-output/ "files/document.docx"
```

The converted PDF lands in `proof-output/` with the same base name (e.g., `document.pdf`). Use that path for the proof commands below.

## Single Value: Quick Proof (one command)

For the common case — one document, one or a few values to prove — use `quick-proof` mode. It does find, verify, and assemble in a single command:

```bash
python3 skills/pdf-proof/scripts/extract_proof.py \
  --mode quick-proof \
  --pdf "files/report.pdf" \
  --search "1,250,000" \
  --label "BCWP" \
  --field "CPR Section 1 — BCWP" \
  --value "$1,250,000" \
  --source "CPR Report, page 3" \
  --description "Budgeted Cost of Work Performed from the Contract Performance Report." \
  --title "Earned Value Verification" \
  --output-html "proof-output/proof.html"
```

This finds the value, extracts a verified highlighted screenshot, and produces a self-contained HTML proof page in one shot. Provide a download link:

```
[Download Proof Page](sandbox:proof-output/proof.html)
```

Quick-proof parameters:
- `--pdf`: Path to the source PDF
- `--search`: Text to find and highlight (multiple terms for multiple highlights on one screenshot)
- `--label`: Short label for the proof card header
- `--field`: Source reference (e.g., "Invoice #4521 — Total Amount")
- `--value`: The display value shown in the summary table
- `--source`: Citation text (e.g., "CPR Report, page 3")
- `--description`: Context about this value
- `--title`: Proof page title
- `--output-html`: Where to save the HTML file
- `--page`: Page number if known (auto-detected if omitted)
- `--prefer`: Match selection — `right` (default, best for forms) or `first` (best for inline text)
- `--match-index`: Select a specific match by index if multiple exist
- `--context`: Vertical context in PDF points (default 80, use 120 for contracts)

## Multiple Values: Three-Step Workflow

When proving multiple values across one or more documents, use the three-step workflow. All three steps are required, in order.

### Step 1: Find

For each value, find where it appears:

```bash
python3 skills/pdf-proof/scripts/extract_proof.py \
  --mode find \
  --pdf "files/source.pdf" \
  --search "1,250.00"
```

If there are multiple matches, note the index of the correct one. Use `--match-index N` in Step 2.

### Step 2: Verify

For each value, extract a verified highlighted screenshot:

```bash
python3 skills/pdf-proof/scripts/extract_proof.py \
  --mode verify \
  --pdf "files/source.pdf" \
  --search "1,250.00" \
  --page 5 \
  --json \
  --output "proof-output/proof_bcwp.png" \
  --result-file "proof-output/result_bcwp.json"
```

`--result-file` is required. It saves the extraction data (including the image) to a file that Step 3 reads. Image data never enters your context.

### Step 3: Assemble

Write a JSON manifest at `proof-output/manifest.json`, then assemble the HTML:

```json
{
  "title": "Earned Value Verification — Source Proof",
  "subtitle": "CPR figures vs PARS database",
  "proofs": [
    {
      "label": "BCWP",
      "field": "CPR Section 1 — BCWP",
      "value": "$1,250,000",
      "source": "CPR Report, page 3",
      "description": "Budgeted Cost of Work Performed.",
      "result_file": "result_bcwp.json"
    },
    {
      "label": "ACWP",
      "field": "CPR Section 1 — ACWP",
      "value": "$1,180,000",
      "source": "CPR Report, page 3",
      "description": "Actual Cost of Work Performed.",
      "result_file": "result_acwp.json"
    }
  ]
}
```

Manifest rules:
- One proof entry per question the user asked.
- `result_file` paths are relative to the manifest location.
- `confidence`, `page`, and `verification` text are auto-populated from the result file.
- `is_negative: true` renders the value in red.

Assemble:

```bash
python3 skills/pdf-proof/scripts/extract_proof.py \
  --mode assemble \
  --manifest proof-output/manifest.json \
  --output proof-output/proof.html
```

```
[Download Proof Page](sandbox:proof-output/proof.html)
```

## Troubleshooting

**Value not found:** Try format variations — with/without commas, decimals, dollar signs, parentheses for negatives. Also check nearby pages.

**Wrong match highlighted:** Use `--mode find` to see all matches, then use `--match-index N`.

**Scanned PDF (no text layer):** Add `--ocr` to the command. Requires Tesseract.
