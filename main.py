#!/usr/bin/env python3
"""Entrypoint: copy entry.png from the repository root to /output/entry.png.

Stdlib only, deterministic, no network.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
