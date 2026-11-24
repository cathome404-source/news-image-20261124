# news-image-20261124

[![bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/news-image-20261124)
[![owner](https://img.shields.io/badge/owner-cathome404--source-green)](https://github.com/cathome404-source)
[![repo](https://img.shields.io/badge/repo-news--image--20261124-orange)](https://github.com/cathome404-source/news-image-20261124)

One-page newspaper of 24 November 2026: 36 dated stories across 9 regions, drawn in code.

## Run it

```sh
python3 render.py
python3 main.py
```

`render.py` reads `stories.json` and draws `entry.png` (1024x1024) with PIL
using only the bundled DejaVu fonts in `fonts/`. `main.py` copies
`entry.png` to `/output/entry.png`. No network, no clock, no randomness.
