# The joke the reviewer laughs at

[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/yayass-crypto/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/yayass-crypto/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for the [make.fun competition "The joke the reviewer laughs at"](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329) — a one-line joke about working beside AI coding agents. $35 pot, 20 paid places, free entry, deadline 2026-11-21 12:29 WIB.

## The joke

> My AI agent writes the code and I write 'LGTM' — together we ship bugs neither of us could have written alone.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the joke deterministically to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), then re-reads it and gates it the way the house gate does: 1–280 Unicode code points, not only whitespace, clean UTF-8. Every run produces the same file, byte for byte.

```sh
python3 main.py
# wrote /output/entry.txt (110 characters)
```

## License

MIT — see [LICENSE](LICENSE).
