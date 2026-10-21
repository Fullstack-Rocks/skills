# Recordings

The GIFs in the main README are real interactive Claude Code sessions on the demo shop, recorded by script:

- `drive.exp` (expect) starts `claude`, answers the first-run dialogs, types each message once the previous turn has gone quiet, and exits. Claude Code switches the terminal to the kitty keyboard protocol, so Enter is sent as `CSI 13 u`.
- `record.sh` copies `demo/` (plus an optional fixture) into `~/fsr-demo/<name>`, records the session with asciinema in a clean environment with `COLORTERM=truecolor`, so the TUI keeps its 24-bit colors, then renders it.
- `warp.py` shortens spinner-only stretches, adds a reading pause before each follow-up, starts at the main UI (skipping the folder-trust dialog), and replaces the local username.
- `render.sh` turns the cast into a GIF with agg and gifsicle.

Needs a logged-in `claude` CLI, plus `asciinema`, `agg` and `gifsicle` (`brew install asciinema agg gifsicle`).

```bash
benchmarks/recordings/record.sh call-depth call-depth commit no \
  "How deep is the call chain from POST /orders/{id}/refund? Use the call-depth skill."
# output: benchmarks/recordings/out/call-depth.gif (out/ is gitignored)
```
