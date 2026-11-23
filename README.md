# The joke about the demo

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

Entry for the [make.fun](https://make.fun) bounty
**"The joke about the demo"** (`the-joke-about-the-demo-20261123-0112`).

## The joke

> Working beside an AI coding agent is like pair programming with a genius who never sleeps, types at 200 wpm, and is absolutely certain about the one function it got completely wrong.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes that one line
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The output
is deterministic: two runs produce byte-identical files.

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## Owner

- make.fun handle: `golden-finch-73-9417`
- Wallet: `86Te13NFCXtMUZYtHPQuvfWhmpnVtdehcxtqWrT1Gz6x` (see `.makefun/owner.json`)
- Referral code: `xj4rk6j0`

## License

MIT — see [LICENSE](LICENSE).
