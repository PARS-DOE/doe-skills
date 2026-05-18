# CLAUDE.md — context for agents working on this repo

This file is for an agent that has cloned `doe-skills` and is being asked to maintain it. Read [README.md](README.md) first for the user-facing description.

## What this repo is

A small, hand-curated collection of [agent skills](https://agentskills.io) for DOE work. The skills here are the ones we've authored or have permission to redistribute. Skills that exist in commercial agent bundles (Anthropic, OpenAI, etc.) are deliberately *not* republished here — users should pull those from their vendor's official channel.

The repo is intentionally narrow. Don't bulk-add skills just because they could live here.

## Layout

```
doe-branding/        DOE brand standards + logos and templates
empower/             Empower (EVMS) user manual + tech notes
pars-json-tools/     PARS CPP JSON validation, Excel conversion, DIQ lookup
LICENSE              Tri-licensed (see "Licensing" below)
README.md            User-facing entry point
```

Every skill folder is self-contained and has `SKILL.md` at its root with `name` / `description` frontmatter. The format follows the agentskills.io spec — don't add client-specific extensions (Claude Code's `allowed-tools`, OpenAI Codex's runtime hints, etc.) unless they degrade gracefully on other clients.

## Licensing (this matters when editing)

The repo bundles three regimes — see [LICENSE](LICENSE) for the full text. Quick summary:

- **MIT** — anything we authored: SKILL.md files, the README, the LICENSE, and every script/utility under `pars-json-tools/`.
- **DOE proprietary** — everything in `doe-branding/`. Logos, brand guide, PowerPoint templates, sample fact sheet. Use is governed by `doe-branding/doe-brand-guide.md`.
- **Encore Analytics proprietary** — everything in `empower/`. Reformatted from Encore's public support docs, included with permission.

When adding files, be explicit about which regime they fall under. If in doubt, ask the user before committing.

## What belongs here vs. doesn't

**Belongs:**
- Skills authored for DOE work that we own outright.
- DOE-specific reference material we have permission to redistribute.
- Tools for DOE data formats (PARS CPP JSON, EIA datasets, etc.).
- Vendor docs reformatted for agent use *only with explicit permission* from the vendor.

**Doesn't belong:**
- Skills cloned or derived from a commercial agent bundle (Anthropic's skills marketplace, OpenAI/ChatGPT's internal skills, etc.). Users get those through their vendor.
- Generic skills with no DOE angle (e.g. a generic `docx-tools`). Recommend an upstream skill instead.
- Anything that depends on a specific harness's built-in tools (e.g. a Monty-internal `get_diq_definition` MCP tool). If a skill needs functionality that doesn't exist as a portable script, write the script.

## Skill authoring conventions

- **Be specific in `description`**. Clients use it to decide when to load the skill, and most clients truncate it at ~1,500 characters. Lead with the strongest trigger phrase.
- **Use workspace-relative paths in instructions** (e.g. `skills/pars-json-tools/foo.py`) rather than hard-coding `~/.claude/skills/...`. Different clients install to different directories; relative paths work everywhere.
- **Standard library first** for scripts. If a skill can be done with stdlib Python or plain `bun`, prefer that. Heavy dependencies hurt portability and make the skill harder to vet.
- **Keep `SKILL.md` short**. Move detailed reference material into sibling files and link from `SKILL.md`. Most clients load the body into context for the rest of the session; long bodies are an ongoing token cost.
- **No client-specific shell injection**. Claude Code supports `` !`command` `` in SKILL.md to inline command output before the model sees it. Other clients ignore it. Don't write skills that depend on that feature working.

## Working on `pars-json-tools` specifically

- `validate-pars-json.ts` and `json-to-excel.ts` run under Bun. They depend on `ajv`, `ajv-formats`, `xlsx`, `adm-zip` — install with `bun add` if you're testing locally.
- `get-diq-definition.py` hits the public PARS Wiki (https://wiki.pars.doe.gov) and converts the rendered HTML to markdown using only the Python stdlib. It does NOT require API credentials — the wiki is publicly readable. If you're tempted to add a `WIKIJS_API_TOKEN` path, push back: the public route works fine, and credential setup is a barrier to adoption.
- The DIQ ID inference (number-only → DS dataset) takes digits 2-3 as the dataset number. First digit is `1` (single-dataset DIQ) or `9` (cross-dataset DIQ). Don't break that mapping.
- The `pars-cpp-json-schema-v5-0-3.json` file is large (~2,700 lines). Don't read it during normal work — the compact reference covers what's needed.

## Working on `empower`

This is reference documentation, not executable. When updating:
- Source content lives on Encore Analytics' support pages. Don't rewrite material; reformat for agent legibility (proper markdown headings, table-of-contents structure, no broken cross-page references).
- Keep the chapter/section structure that already exists. The user manual chapters map 1:1 to Encore's published manual.
- If you're adding new pages, get the user to confirm Encore has cleared the source first.

## Working on `doe-branding`

Read `doe-branding/doe-brand-guide.md` before touching anything else. The skill exists to enforce the brand guide; the brand guide is the source of truth.

The PowerPoint template, logos, and fact sheet are DOE proprietary. Don't modify them. If something looks off, raise it with the user — the fix is upstream at DOE, not here.

## Adding a new skill

1. Confirm with the user that the skill belongs here (see "What belongs here vs. doesn't").
2. Create `skills/<name>/SKILL.md` with name/description frontmatter and concise instructions.
3. If the skill bundles content from a third party, get redistribution clearance *first* and update `LICENSE` and the README's Licensing section to call out the new regime.
4. Update the Skills table in `README.md`.
5. If the skill ships scripts, list runtime dependencies in `SKILL.md` and in the "What each skill needs at runtime" section of `README.md`.

## Removing a skill

If a skill turns out to overlap with a commercial bundle, or if we lose redistribution permission, remove it cleanly:
1. `git rm -r <skill>/`
2. Drop its row from the README skills table.
3. Drop its licensing note from `LICENSE` and the README if no other content covers that regime.
4. Commit with a one-line message explaining *why* it's being removed (overlap with vendor bundle, permission revoked, etc.) so the history makes sense to future maintainers.

## Git and commit conventions

- One logical change per commit. Don't bundle a new skill with unrelated cleanup.
- Commit message body should explain *why*. The diff already shows the what.
- Default to `Co-Authored-By: Claude` footer when an agent did the work.
- The remote is `origin` → `https://github.com/PARS-DOE/doe-skills` (currently private).

## Things to push back on

- "Add the docx skill from \[vendor\]" — no, point them at the vendor's official channel.
- "Make this skill assume Claude Code" — no, skills here stay harness-neutral.
- "Add a build/CI step" — probably no. This is content, not a software product. If validation is needed (e.g. lint the SKILL.md frontmatter), keep it lightweight.
- "Rewrite the Empower docs to be shorter / restructure them" — only with Encore's involvement. We reformatted with permission; we shouldn't substantively rewrite.
