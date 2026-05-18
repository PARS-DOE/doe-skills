# doe-skills

A collection of Claude skills for DOE (Department of Energy) work.

The repo follows the [skills.sh](https://skills.sh) layout — each top-level directory is a skill with a `SKILL.md` at its root, plus any supporting scripts, references, and assets.

## Skills

| Skill | Purpose |
| --- | --- |
| [doe-branding](doe-branding/) | 2025 DOE brand standards — logos, colors, typography, and templates for on-brand deliverables. |
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
