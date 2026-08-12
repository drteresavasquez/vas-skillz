---
name: example-skill
description: Template skill demonstrating the standard directory layout (SKILL.md, scripts/, references/, assets/). Use as a starting point when creating a new skill in this repo.
---

# Example Skill

This is a template skill showing how the pieces of a skill fit together. Copy this
directory when starting a new skill, then replace the content below.

## When to use this skill

Trigger conditions go here — the specific phrases, file types, or situations that
should cause Claude to load this skill. Be concrete; vague triggers cause the skill
to fire too often or not at all.

## Instructions

1. Describe the steps Claude should follow, in the order it should follow them.
2. Point to bundled files as needed:
   - Run `scripts/example.py` for the deterministic part of the task — Claude can
     execute this without reading its contents into context.
   - Read `references/reference.md` when detailed background or an API reference
     is needed; don't load it unless the task calls for it.
   - Use `assets/template.md` as the starting point for any output file this skill
     produces.
3. Keep this file under ~500 lines. Anything longer or more detailed belongs in
   `references/`, loaded on demand.
