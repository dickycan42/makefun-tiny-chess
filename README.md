[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/dickycan42/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/dickycan42/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# Tiny chess engine (4 KB)

A compact 0x88 alpha-beta chess engine in Python, built for the
make.fun tiny-chess-01 bounty (4,096 byte entrypoint cap).
Bounty page: https://make.fun/bounty/tiny-chess-01

Search: iterative deepening, null-move pruning, LMR, transposition
table with EXACT/LOWER/UPPER bounds and best move, killer moves,
quiescence search. Evaluation is incremental (material, piece-square
tables, bishop pair, tempo, king safety by game phase) with a
100,000 node budget per move. Deterministic: no clock, no randomness.

`main.py` is the entrypoint, packed with the kit's own command
(`makefun compress`) from the readable source `main-readable.py`,
which lives in this folder next to it.

## Verification

Local practice gauntlet against the official scorer: Elo 1173
(floor 1154), 2 wins, 1 draw, 5 losses, wall 742 s of an 1,800 s
budget, about 2.5 s per move (limit 10 s). Move generation passes
perft 18/18. The same harness reproduces the v1 server score
(Elo 705) exactly, so the practice number is trusted.

## Run

The entrypoint is `main.py`, run with python3:

    python3 main.py
