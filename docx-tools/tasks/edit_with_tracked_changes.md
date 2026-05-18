# Task: Edit a DOCX with Track Changes (Redlines)

## When to use

The user wants edits to appear as Word tracked changes (redlines) so a human reviewer can accept or reject each change individually. Common requests:

- "Edit this document with Track Changes on"
- "Make these changes so I can see what was modified"
- "Redline the edits"
- "Show the changes as tracked"

## Key concept

`python-docx` has **no built-in tracked changes support**. Use the `docx-revisions` library, which extends python-docx with proper cross-run text matching and correct OOXML revision markup.

## Workflow

### Step 1: Make tracked edits

**Option A — CLI script (best for simple find-and-replace):**

```bash
# Replace text (handles text split across multiple XML runs)
python skills/docx-tools/scripts/add_tracked_replacements.py input.docx \
  --out output.docx \
  --replace "old text=new text" \
  --replace "another old=another new" \
  --author "Walt"

# Delete a paragraph by matching its content
python skills/docx-tools/scripts/add_tracked_replacements.py input.docx \
  --out output.docx \
  --delete "text in paragraph to remove" \
  --author "Walt"

# Insert a new paragraph
python skills/docx-tools/scripts/add_tracked_replacements.py input.docx \
  --out output.docx \
  --insert "New paragraph to add at the end." \
  --author "Walt"

# Combine all three in one pass
python skills/docx-tools/scripts/add_tracked_replacements.py input.docx \
  --out output.docx \
  --replace "draft=final" \
  --delete "TODO: remove this" \
  --insert "Reviewed and approved." \
  --author "Walt"
```

**Option B — Python script (best for complex or conditional edits):**

```python
from docx_revisions import RevisionDocument
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

rdoc = RevisionDocument("input.docx")

# Enable trackRevisions so Word keeps tracking on when opened
settings = rdoc.document.settings.element
if settings.find(qn("w:trackRevisions")) is None:
    settings.append(OxmlElement("w:trackRevisions"))

# Find-and-replace (handles cross-run text correctly)
rdoc.find_and_replace_tracked("old phrase", "new phrase", author="Walt")

# Replace at a specific character range within a paragraph
para = rdoc.paragraphs[2]
para.replace_tracked_at(start=10, end=25, replace_text="replacement", author="Walt")

# Delete a text range within a paragraph
para.add_tracked_deletion(start=0, end=15, author="Walt")

# Insert text at the end of a paragraph
para.add_tracked_insertion(" appended text", author="Walt")

rdoc.save("output.docx")
```

### Step 2: Render and review

```bash
python skills/docx-tools/render_docx.py output.docx --output_dir out
```

Inspect the PNGs — tracked changes should be visible as colored redlines (insertions underlined, deletions struck through). If rendering shows no redlines but the edits exist, check that `trackRevisions` is enabled in settings.xml.

### Step 3: Deliver

Return the DOCX with tracked changes. The reviewer opens it in Word and uses Review → Accept/Reject to handle each change.

## Accepting or rejecting tracked changes (producing a clean copy)

If the user wants tracked changes **accepted** (finalized into a clean document):

```bash
# Report how many tracked changes exist
python skills/docx-tools/scripts/accept_tracked_changes.py input.docx --mode report

# Accept all changes (produce clean copy)
python skills/docx-tools/scripts/accept_tracked_changes.py input.docx --mode accept --out clean.docx

# Reject all changes (revert to original)
python skills/docx-tools/scripts/accept_tracked_changes.py input.docx --mode reject --out reverted.docx
```

Always render and review the clean copy afterward.

## Common pitfalls

- **Text not found**: Word splits text across XML runs due to formatting, spell-check, and edit history. `docx-revisions` handles this; the old OOXML approach did not. If `find_and_replace_tracked` returns 0 matches, check for whitespace differences or Unicode characters (curly quotes vs straight quotes).
- **Missing trackRevisions flag**: Without `<w:trackRevisions/>` in settings.xml, Word won't show tracking mode as "on" when the document is opened — but existing tracked changes still render. The CLI script sets this automatically.
- **Tables, headers, footers**: `rdoc.paragraphs` covers the main body. For text inside tables, iterate `rdoc.document.tables[n].rows[r].cells[c].paragraphs`. Headers/footers require `rdoc.document.sections[n].header.paragraphs`.
- **Formatting on inserted text**: Tracked insertions inherit the run formatting of the insertion point. If you need specific formatting on inserted text, set it on the returned run after insertion.
