# vas-skillz

A personal collection of [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) — packaged instructions, scripts, and reference material that extend what Claude can do.

## Repository layout

Each skill lives in its own top-level directory, named after the skill:

```
skill-name/
├── SKILL.md        # Required — main instructions, keep under 500 lines
├── scripts/         # Optional — executable code (Python, Bash, etc.)
├── references/      # Optional — docs loaded as needed (API guides, examples/)
└── assets/          # Optional — templates and other supporting files
```

- **`SKILL.md`** is the only required file. It starts with YAML frontmatter (`name`, `description`) and a short body describing what the skill does and when to use it. Claude loads the frontmatter always, and the body only when the skill is triggered — so keep it lean.
- **`scripts/`** holds deterministic, executable code Claude can run without loading it into context.
- **`references/`** holds supplementary docs (API guides, detailed examples) that are loaded on demand rather than kept in context.
- **`assets/`** holds templates or other files a skill reads from or writes to.

See [`example-skill/`](./example-skill) for a working template — copy it as a starting point for new skills.

## Adding a new skill

1. Copy `example-skill/` to a new directory named for your skill (kebab-case).
2. Update `SKILL.md`'s frontmatter and instructions.
3. Add any scripts, references, or assets the skill needs.
4. Delete files/folders you don't use — only `SKILL.md` is required.
