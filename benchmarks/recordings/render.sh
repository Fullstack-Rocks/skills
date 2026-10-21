#!/bin/bash
# usage: render.sh <name>  (cast -> warped cast -> gif)
R=$(cd "$(dirname "$0")" && pwd); n=$1; OUT=${OUT:-$R/out}
python3 "$R/warp.py" "$OUT/$n.cast" "$OUT/$n.warp.cast"
agg --theme github-dark --font-family "Menlo,Apple Symbols,Symbol" --font-size 16 --line-height 1.3 \
  --speed 1.0 --idle-time-limit 6 --last-frame-duration 8 "$OUT/$n.warp.cast" "$OUT/$n.raw.gif" >/dev/null 2>&1
gifsicle -O3 --lossy=40 --colors 128 "$OUT/$n.raw.gif" -o "$OUT/$n.gif"
echo "$n: $(du -h "$OUT/$n.gif" | cut -f1)"
