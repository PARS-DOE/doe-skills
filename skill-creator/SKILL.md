---
name: skill-creator
description: "Guide for creating and updating high-quality skills. Use whenever a user asks to create, update, edit, improve, or troubleshoot a skill, and for questions about skills (e.g., What are skills? What can I use skills for? How do I create one?)."
---

# Skill Creator

## What are Skills?
Skills are small, reusable bundles of instructions and optional reference files that teach Walt how to perform specific tasks or follow precise conventions consistently. Building a skill is like putting together a training manual for a new hire.

This skill is used for both creating new skills and updating existing skills.

When the user is asking what Skills are, how they help, where to start, or what they can use Skills for, answer that question first instead of jumping into the creation workflow.

## Skill Structure and Components
- **Overall structure**
  A Skill is a set of instructions with optional reference file attachments. The instructions define when the Skill should be used and exactly how Walt should behave.
- **SKILL.md format**
  Skills use YAML frontmatter with the Skill's name and description, followed by markdown instructions. The description determines *when* the skill is auto-invoked.
- **Reference files**
  A Skill can include additional files such as documentation, datasets, templates, or scripts. These are attached as reference files and available in the workspace when the skill is active.

## Skill Use Cases
- **Reusable tasks**
  Skills can bundle repeatable logic and instructions into a reliable workflow, such as building a financial model, parsing documents, generating reports, or running standardized analyses.
- **Tool and data source guidance**
  Skills can encode best practices for using tools or data sources, including which database tables to query, how to structure requests, and how to format or validate outputs.
- **Conventions and standards**
  Skills are well-suited for capturing organizational conventions like writing style, formatting rules, compliance language, or review checklists, ensuring consistency across all conversations.
- **Multi-step workflows**
  Skills can support complex workflows by coordinating instructions, scripts, and resources across domains.

## Writing Effective Skill Instructions
- **Be concise**: Skill instructions should be as lightweight as possible while still being precise. Skills share context window space with the system prompt, conversation history, and other active Skills. Focus on specific, opinionated, and non-obvious content. Favor short examples and concrete guidance over long explanations.
- **Constraint vs flexibility**: Choose the right level of constraint for the task. For open-ended tasks, use high-level but specific written guidance. For highly deterministic tasks, include scripts and require execution. For anything in between, include template examples or pseudo-code.

## SKILL.md Format

```yaml
---
name: skill-name
description: "When to use this skill and what it does"
---

# Instructions

Body content here...
```

### Frontmatter
- `name`: Lowercase, alphanumeric and hyphens only (1-64 chars). No leading/trailing/consecutive hyphens.
- `description`: The primary triggering mechanism — include both what the Skill does and specific triggers/contexts for when to use it. All "when to use" information belongs here, not in the body. Max 1024 chars.

### Body
- Max 20,000 characters
- Contains behavioral guidance, examples, and references to attached files
- Keep focused and compact — treat it as a control plane, not a knowledge dump

## Progressive Loading and Context Efficiency
Walt automatically loads Skills and their reference files incrementally as they become relevant.

### How Content Is Loaded
1. **Skill metadata** — The name and description are always available and determine *whether* the skill is activated
2. **Core instructions** — When a Skill is selected, the body is loaded with the essential workflow and rules
3. **Reference files** — Additional files are read only when explicitly needed for the current step

### Design Guidelines
Keep the main instructions focused and compact. When content grows large (>500 lines), move details into separate reference files and link to them from the main instructions.

### Common Organization Patterns

**Pattern 1: High-level guide with references**
```markdown
# PDF Processing
## Quick start
Extract text with pdfplumber:
[code example]

## Advanced features
- **Form filling**: See forms-reference.md for complete guide
- **API reference**: See api-reference.md for all methods
```

**Pattern 2: Domain-specific organization**
Organize by domain to avoid loading irrelevant context:
- `references/finance.md` (revenue, billing metrics)
- `references/sales.md` (opportunities, pipeline)

**Pattern 3: Conditional details**
```markdown
# DOCX Processing
## Creating documents
Use python-docx for new documents.
## Editing documents
For simple edits, modify directly.
**For tracked changes**: See tracked-changes.md
```

**Important guidelines:**
- **Avoid deeply nested references** — Keep references one level deep. All reference files should link directly from the main instructions.
- **Structure longer reference files** — For files longer than 100 lines, include a table of contents at the top.

## Skill Creation Process

1. Understanding the Skill with Concrete Examples by Asking Questions
2. Plan reusable skill contents (instructions, reference files, scripts)
3. Write the skill instructions
4. Iterate based on real usage

### Step 1: Understanding the Skill with Concrete Examples

Pause and ask the user clarifying questions before continuing. At minimum, clarify: (1) expected input, (2) expected output, and (3) any tools or data sources to be used. The user's initial request was likely short and ambiguous — ask follow-up questions to fully understand intent.

If the user is asking about Skills conversationally:
1. Explain what a Skill is in plain language
2. Give concrete examples tailored to the user's context
3. Mention they can manage skills from the Skills page in the sidebar
4. End with a direct next-step question

To avoid overwhelming users, start with the most important questions and follow up as needed.

### Step 2: Planning the Reusable Skill Contents

Analyze each concrete example by:
1. Considering how to execute the example from scratch
2. Identifying what reference files, scripts, or documentation would help when executing repeatedly

Example: When building a `pdf-editor` skill, rotating a PDF requires the same code each time → include a reference script.
Example: When building a `data-query` skill, querying requires knowing table schemas → include schema documentation as a reference file.

Remember: Walt excels at text analysis and transformation natively — only add scripts for operations that benefit from deterministic code.

### Step 3: Write the Skill

Write the SKILL.md with proper frontmatter and body. Follow these guidelines:
- Use imperative/infinitive form in instructions
- Make the description clearly describe triggering conditions
- Keep instructions focused on what's specific, opinionated, and non-obvious
- Include reference files for detailed documentation, schemas, templates, or scripts

### Step 4: Iterate

After testing the skill in real conversations:
1. Notice struggles or inefficiencies
2. Identify how instructions or reference files should be updated
3. Implement changes and test again

## Additional Guidance
- Consult `references/workflows.md` for sequential and conditional workflow patterns
- Consult `references/output-patterns.md` for template and example patterns for consistent output