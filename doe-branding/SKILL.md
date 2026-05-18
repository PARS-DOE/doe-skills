---
name: doe-branding
description: "DOE brand compliance for documents, presentations, and communications. Use when creating or reviewing any DOE-branded content: slide decks, reports, fact sheets, memos, or any deliverable that needs DOE logos, colors, typography, or layout compliance. Triggers on: DOE branding, brand guide, brand colors, DOE template, DOE logo, DOE style guide, brand compliant, on-brand."
---

# DOE Brand Compliance

Apply the 2025 DOE brand standards to all content. For full details, read [doe-brand-guide.md](doe-brand-guide.md).

## Quick Reference

### Colors (use ONLY these)

**Primary:**

| Name | Hex | Use |
|------|-----|-----|
| Midnight Blue | `#0f142e` | Cover backgrounds, dark sections |
| Cadet Blue | `#1a204c` | Headers, accents |
| Clear Blue | `#21409a` | Links, primary blue |
| Cardinal Red | `#8a181a` | Emphasis only — use sparingly |
| Dark Gray | `#293340` | Body text |
| Light Blue | `#d9dfea` | Light backgrounds, tints |

**Accent:** Energy Blue `#085a9b`, Deep Green `#106636`, Energy Green `#61ad00`, Energy Yellow `#ffbe2e`, Energy Orange `#fa9441`, Sky Blue `#e7f6f8`

**Neutral:** Dark Cool Gray `#52565c`, Medium Cool Gray `#999999`, Soil Brown `#5e4f4d`, Ivory `#fef2e4`

### Typography (Office documents)

| Role | Font | Weights |
|------|------|---------|
| Sans serif | **Arial** | Regular, Bold, Italic, Bold Italic |
| Serif | **Times New Roman** | Regular, Bold, Italic, Bold Italic |

Figtree and STIX Two Text are the preferred DOE typefaces but are not available in Microsoft Office. Use Arial and Times New Roman for all DOCX and PPTX work.

### Gradients (approved combinations only)

- Midnight Blue `#0f142e` to Clear Blue `#21409a`
- Cadet Blue `#1a204c` to Energy Blue `#085a9b`
- Midnight Blue `#0f142e` to Energy Green `#61ad00`
- Deep Green `#106636` to Energy Green `#61ad00`

## Logo Usage

Three logo files are available as reference files:
- `doe-logo-color-horizontal.png` — **preferred** for most uses
- `doe-logo-white-horizontal.png` — for dark backgrounds
- `doe-logo-color-vertical.png` — for vertical layouts

**Rules:**
- The logo is the seal + logotype locked together. Never separate, stretch, recolor, or enclose in shapes.
- Maintain clearspace of 0.5x around the logo (x = seal height).
- The retired "bolt" logo (green ENERGY wordmark) must never be used.
- Do not use the seal alone without BrandManager approval.
- Program office lock-ups must be obtained from BrandManager@hq.doe.gov — do not recreate them.

## Templates

### PowerPoint

The DOE template is at `skills/doe-branding/doe-powerpoint-base.pptx`. It contains the DOE slide master, all 7 layouts, logos, and branding, but **no content slides**. Just add slides and go.

**When creating any DOE presentation, you MUST use `doe-powerpoint-base.pptx`.** Do not create slides from scratch with pptxgenjs or custom layouts. If the user explicitly requests a non-DOE presentation, you may skip the template. Otherwise, DOE branding is the default.

**IMPORTANT:** Never use `prs.slides._sldIdLst` or other underscore-prefixed private attributes to delete slides. This creates files that PowerPoint and LibreOffice flag as corrupted. The base template has no slides to delete — just add what you need.

#### Template Layouts

| Index | Name | Placeholders | Use for |
|-------|------|-------------|---------|
| 0 | Title Slide with subtitle | idx=0 CENTER_TITLE, idx=1 SUBTITLE | Title slide with centered title + subtitle |
| 1 | Title Slide | idx=0 TITLE (bottom of slide) | Alternate cover with title at bottom |
| 2 | 1_Title Bar and Heavy Bullet Content | idx=0 TITLE, idx=12 OBJECT (body) | Standard content slide — **use this for most slides** |
| 3 | 2_Two Bullet Content | idx=0 TITLE, idx=1 OBJECT (left), idx=12 OBJECT (right) | Two-column content |
| 4 | Title Only | idx=0 TITLE | Slide with title only (add free-form shapes below) |
| 5 | 1_Title Slide | idx=0 CENTER_TITLE, idx=1 SUBTITLE | Section break / divider |
| 6 | Closing Slide | (no placeholders) | End slide with DOE branding |

#### Workflow: Creating a DOE Presentation with python-pptx

```python
from pptx import Presentation

# Use the base template (no sample slides to remove)
prs = Presentation('skills/doe-branding/doe-powerpoint-base.pptx')

# Title slide (layout 0)
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.placeholders[0].text = "Your Title Here"
slide.placeholders[1].text = "Your Subtitle Here"

# Content slide (layout 2) — use idx=12 for the body placeholder
slide = prs.slides.add_slide(prs.slide_layouts[2])
slide.placeholders[0].text = "Slide Title"
body = slide.placeholders[12].text_frame
body.clear()
p = body.paragraphs[0]
p.text = "First bullet point"
p = body.add_paragraph()
p.text = "Second bullet point"

# Two-column slide (layout 3) — idx=1 left, idx=12 right
slide = prs.slides.add_slide(prs.slide_layouts[3])
slide.placeholders[0].text = "Two Column Title"
slide.placeholders[1].text_frame.text = "Left column content"
slide.placeholders[12].text_frame.text = "Right column content"

# Closing slide (layout 6)
slide = prs.slides.add_slide(prs.slide_layouts[6])

prs.save('output/my-presentation.pptx')
```

**Key points:**
- Always start from `doe-powerpoint-base.pptx` — never delete slides from the template
- The body placeholder on content slides (layout 2) is idx=12, NOT idx=1
- The two-column layout (layout 3) uses idx=1 (left) and idx=12 (right)
- All template layouts inherit DOE colors, logos, and fonts — do not override them
- Use Arial for any manually styled text; the template defaults handle most styling
- Only use python-pptx's public API — never access underscore-prefixed attributes

### Fact Sheets

Reference `doe-fact-sheet-1page.pdf` for the standard one-page layout. Key elements:
- DOE logo top-left
- Title/headline area with accent color band
- Professional body typography
- Image placement area
- DOE-branded footer

## Creating Brand-Compliant Content

### Documents (DOCX)
- Use Arial for headings, Times New Roman for body (or Arial throughout)
- Apply DOE primary colors for heading accents and section dividers
- Place the horizontal logo in the header or title page
- Use Light Blue or Ivory for subtle background fills
- Maintain generous margins and professional spacing

### Presentations (PPTX)
- Start from the official template (`doe-powerpoint-template.pptx`)
- Override the slides-tools color palette with DOE brand colors above
- Use Midnight Blue or Cadet Blue for dark slide backgrounds
- Use white text on dark backgrounds, Dark Gray text on light
- The DOE logo is built into the template layouts — do not add extra logos

### General Rules
- Never use non-DOE colors for branded content
- Never alter, recreate, or improvise the DOE logo
- Maintain visual consistency across all deliverables
- When in doubt about brand compliance, refer to [doe-brand-guide.md](doe-brand-guide.md)
