# ARK Electronics docs

This repo is the GitBook git sync source for [docs.arkelectron.com](https://docs.arkelectron.com). `SUMMARY.md` is the nav. A page that isn't listed there isn't published, and GitBook builds each page's URL from where it sits in the nav.

Read the matching skill in `.agents/skills/` before you start:

| Skill | Read it before |
|---|---|
| `docs-writing` | Writing or editing any page, or reviewing a docs PR |
| `product-pages` | Adding a product, or adding, moving or deleting a product's pages |

- Images go in `.gitbook/assets/` and are linked by a path relative to the page.
- Commit subjects read `docs(<product or area>): <subject>`, such as `docs(hadron-adapter): add the ARK Hadron Adapter pages`.
- Stage files by path. Never `git add -A`, because agents that fetch live pages leave HTML files in the repo root.
- `gh pr edit` fails on this repo with a Projects (classic) GraphQL error. Edit a PR's title or body with `gh api -X PATCH repos/ARK-Electronics/gitbook/pulls/<N> -F body=@<file>`.

Claude Code reads neither `AGENTS.md` nor `.agents/` directly. `CLAUDE.md` imports this file, and each `.claude/skills/<name>` is a symlink into `.agents/skills/`. Add the symlink when you add a skill.
