# doe-skills

A collection of Claude skills oriented around DOE (Department of Energy) work and the document formats DOE staff most often deal with: Word, PDF, and PARS CPP JSON.

The repo follows the [skills.sh](https://skills.sh) layout — each top-level directory is a skill with a `SKILL.md` at its root, plus any supporting scripts, references, and assets.

## Skills

| Skill | Purpose |
| --- | --- |
| [docx-tools](docx-tools/) | Read, create, edit, redline, and comment on `.docx` files; visual QA via rendered PNGs. |
| [doe-branding](doe-branding/) | 2025 DOE brand standards — logos, colors, typography, and templates for on-brand deliverables. |
| [pars-json-tools](pars-json-tools/) | Validate and convert PARS CPP JSON; includes schema reference. |
| [pdf-proof](pdf-proof/) | Generate a self-contained HTML proof page with highlighted screenshots showing where specific values appear in a document. |
| [pdf-tools](pdf-tools/) | PDF creation, editing, extraction, forms, OCR, redaction, and rendering. |

## Layout

Each skill is self-contained:

```
<skill-name>/
  SKILL.md          # frontmatter + instructions (required)
  scripts/          # optional helper scripts
  references/       # optional reference material
  ...
```

`SKILL.md` begins with YAML frontmatter containing `name` and `description` — the description is what tooling uses to decide when to load the skill, so it should be specific about triggers.
