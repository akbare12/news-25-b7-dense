# The World Today — 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/akbare12/news-25-b7-dense/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/akbare12/news-25-b7-dense/reward.svg)](https://make.fun/bounty/news-image-20261125)

Dense front page for the make.fun news-image bounty `news-image-20261125`: 50 stories, 10 regions, hero trio across the top, 13 illustration panels, numbered cards, map pins and a sources footer. Date check: Tuesday 25 November 2026. All text in English.

## Hero trio

- **Trump tariffs:** 14 partners hit, China at 20%.
- **AI chip selloff:** Kospi -6.16% to 4,697.51; Samsung -9.87%, Hynix -11.05%.
- **Shenzhou-24:** first foreign astronaut aboard Tiangong — Pakistan's Muhammad Zeeshan Ali.

Also: Kospi crash and the Bogor gold mine collapse (9 dead, 17 trapped, 25 Nov).

## How it works

- `gen.py` renders `entry.png` at build time (Pillow, build machine only).
- `main.py` is stdlib-only: it copies `entry.png` to `MAKEFUN_OUTPUT_DIR/entry.png`.
- Every card carries a certainty mark: C = confirmed, R = reported, CL = claim. Every hero carries a WHY IT MATTERS line.

## Run

```sh
python3 gen.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
