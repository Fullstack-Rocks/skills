#!/bin/bash
# usage: record.sh <name> <fixture|none> <commit|uncommitted|none> <claude-md: yes|no> <message> [<message> ...]
set -u
R=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$R/../.." && pwd)
OUT=${OUT:-$R/out}; mkdir -p "$OUT"
name=$1; fixture=$2; mode=$3; claudemd=$4; shift 4
dir=$HOME/fsr-demo/$name
rm -rf "$dir"; mkdir -p "$dir"
rsync -a --exclude node_modules --exclude .venv --exclude WALKTHROUGH.md --exclude __pycache__ "$REPO/demo/" "$dir/"
cd "$dir" && git init -q -b main && true
[ "$claudemd" = yes ] && printf 'Before writing or changing code, load the `under-engineering` skill and follow it.\n' > CLAUDE.md
[ "$mode" = commit ] && rsync -a --exclude '*.json' "$REPO/benchmarks/fixtures/$fixture/" "$dir/"
git add -A && git -c user.name=demo -c user.email=demo@example.com commit -qm "shop demo"
[ "$mode" = uncommitted ] && rsync -a --exclude '*.json' "$REPO/benchmarks/fixtures/$fixture/" "$dir/"
env -i HOME="$HOME" PATH="$PATH" TERM=xterm-256color COLORTERM=truecolor LANG=en_US.UTF-8 USER="$USER" \
  asciinema rec --overwrite --headless --window-size 100x30 -c "$R/drive.exp 15 $(printf "%q " "$@")" "$OUT/$name.cast" >/dev/null 2>&1
OUT="$OUT" "$R/render.sh" "$name"
