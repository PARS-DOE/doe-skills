# doe-skills

A collection of [agent skills](https://agentskills.io) for DOE (Department of Energy) work. Skills bundle procedural knowledge, reference material, and helper scripts into version-controlled folders that agentic LLM clients can load on demand.

This repo follows the agentskills.io specification: each top-level directory is a self-contained skill with a `SKILL.md` at its root, plus any supporting scripts, references, and assets. Skills are model- and harness-agnostic.

## Skills

| Skill | Purpose |
| --- | --- |
| [doe-branding](doe-branding/) | 2025 DOE brand standards — logos, colors, typography, and templates for on-brand deliverables. |
| [empower](empower/) | Empower (EVMS reporting and analysis) user manual and tech notes — concepts, configuration, custom reports, and administration. |
| [pars-json-tools](pars-json-tools/) | Validate and convert PARS CPP JSON, look up DIQ check definitions, and reference the CPP JSON schema. |

## Installing

The easiest way to install these skills is with the [`skills` CLI](https://skills.sh), which handles most popular agent harnesses (Claude Code, Cursor, OpenAI Codex, Gemini CLI, OpenCode, GitHub Copilot, and more):

```bash
# List the skills available in this repo
npx skills add PARS-DOE/doe-skills --list

# Install a single skill into your current project (default)
npx skills add PARS-DOE/doe-skills --skill pars-json-tools

# Install globally (available across all projects) and target a specific harness
npx skills add PARS-DOE/doe-skills --skill pars-json-tools -g -a claude-code

# Install everything globally for all detected harnesses
npx skills add PARS-DOE/doe-skills --all -g --agent '*'
```

By default the installer drops skills into `./<harness>/skills/` in your current project. Pass `-g` for the personal-scope location (e.g. `~/.claude/skills/`). Pass `-a <harness>` (repeatable) or `--agent '*'` to target specific harnesses; otherwise the CLI prompts you.

### Doing it by hand

If your harness isn't supported by the CLI, the format is just a folder with a `SKILL.md` at its root — that's the [agentskills.io](https://agentskills.io) standard, supported by [many clients](https://agentskills.io/clients). Clone this repo and symlink (or copy) the skill folders into wherever your harness looks for skills:

```bash
git clone https://github.com/PARS-DOE/doe-skills.git ~/src/doe-skills

# Example: Claude Code personal scope.
mkdir -p ~/.claude/skills
ln -s ~/src/doe-skills/pars-json-tools ~/.claude/skills/pars-json-tools
```

Check your harness's docs for the exact directory it watches.

## What each skill needs at runtime

Each skill states its own dependencies in its `SKILL.md`. Highlights:

- **doe-branding** is documentation and assets only — no runtime dependencies.
- **empower** is reference documentation — no runtime dependencies.
- **pars-json-tools** uses [Bun](https://bun.sh) for its TypeScript validation and Excel-conversion scripts (`ajv`, `ajv-formats`, `xlsx`, `adm-zip`), and Python 3.9+ (standard library only) for the DIQ lookup script.

## Layout

Each skill is self-contained:

```
<skill-name>/
  SKILL.md          # frontmatter + instructions (required)
  scripts/          # optional helper scripts
  references/       # optional reference material
  ...
```

`SKILL.md` begins with YAML frontmatter containing `name` and `description` — the description is what the client uses to decide when to load the skill, so it should be specific about the cases it covers.

## Licensing

This repository mixes three licensing regimes. See [LICENSE](LICENSE) for the full text.

- **Scripts, utilities, and skill instructions** authored for this repo (everything under `pars-json-tools/` and the `SKILL.md` / `README.md` files) are released under the **MIT License**.
- **DOE branding assets** in [`doe-branding/`](doe-branding/) (logos, templates, brand guide, sample fact sheet) are **proprietary to the U.S. Department of Energy**. Use is restricted by the DOE brand guidelines included in `doe-branding/doe-brand-guide.md`.
- **Empower reference content** in [`empower/`](empower/) is **proprietary to Encore Analytics, LLC**. It is a reformatted, agent-friendly version of Encore Analytics' public-facing support documentation and is included here with permission from Encore Analytics.
