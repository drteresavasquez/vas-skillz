# Severity guide

**REVIEW** — placeholder scale, adjust to match how your team actually
triages.

| Severity | Meaning | Example |
|---|---|---|
| Critical | Data loss, security exposure, or the app is unusable for most users. Fix now. | Auth bypass; writes corrupting user data. |
| High | A core flow is broken with no reasonable workaround. | Checkout fails for all users on one payment method. |
| Medium | A flow is broken but a workaround exists, or the impact is limited to a minority of users/cases. | Export fails only for reports over 10k rows. |
| Low | Cosmetic, or an edge case with negligible user impact. | Misaligned button on a rarely-visited settings page. |

When unsure between two levels, ask: "if this shipped to everyone
unfixed, what's the worst plausible outcome this week?" — pick the level
that answer supports, not the level that feels proportionate to how
annoying the bug is to look at.
