# ALDER dev log

Shared, append-only log for both teaching assistants working on this project
(Claude Code = manager/architect, Qwen3/Cline = hands-on teaching partner).
Add a dated entry each session: what was covered, what Gav now understands,
what's open for next time. Don't edit past entries — append new ones.

---

## 2026-07-15 — Claude Code

Set up the local Qwen3/Cline teaching setup (Ollama + Qwen3 14B + Cline
extension + this log). Also locked in the active build target and taught
Python fundamentals up through `for` loops.

**Where things stand:**
- Python: Gav has variables, lists, zero-based indexing, `IndexError`, and
  `for` loops solid (confirmed via correct predictions in the REPL, not just
  told). Next concept: nested lists (list of lists) as a grid — was about to
  do the `grid[1]` vs `grid[1][0]` predict-then-verify exercise.
- Build target: a synthetic terrain heightmap, matching the ALDER whitepaper's
  own build order (step 4, "Site 01"). Six-step plan, currently on step 1.
  Full detail in Claude's memory; ask Claude Code if you need the roadmap
  re-stated.
- Standing rule: Gav writes/understands every line. No large code dumps from
  either assistant.

**Next action:** resume at the `grid[1]` / `grid[1][0]` prediction.
