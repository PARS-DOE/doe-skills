# doe-skills

A collection of Claude skills for DOE (Department of Energy) work.

The repo follows the [skills.sh](https://skills.sh) layout — each top-level directory is a skill with a `SKILL.md` at its root, plus any supporting scripts, references, and assets.

## Skills

| Skill | Purpose |
| --- | --- |
| [doe-branding](doe-branding/) | 2025 DOE brand standards — logos, colors, typography, and templates for on-brand deliverables. |
| [empower](empower/) | Empower (EVMS reporting and analysis) user manual and tech notes — concepts, configuration, custom reports, and administration. |
| [pars-json-tools](pars-json-tools/) | Validate and convert PARS CPP JSON; includes schema reference. |

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

## Licensing

This repository mixes three licensing regimes. See [LICENSE](LICENSE) for the full text.

- **Scripts, utilities, and skill instructions** authored for this repo (everything under `pars-json-tools/` and the `SKILL.md` / `README.md` files) are released under the **MIT License**.
- **DOE branding assets** in [`doe-branding/`](doe-branding/) (logos, templates, brand guide, sample fact sheet) are **proprietary to the U.S. Department of Energy**. Use is restricted by the DOE brand guidelines included in `doe-branding/doe-brand-guide.md`.
- **Empower reference content** in [`empower/`](empower/) is **proprietary to Encore Analytics, LLC**. It is a reformatted, agent-friendly version of Encore Analytics' public-facing support documentation and is included here with permission from Encore Analytics.
