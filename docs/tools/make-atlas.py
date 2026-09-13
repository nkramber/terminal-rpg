#!/usr/bin/env python3
"""Render content/sprites/atlas.png from the grids and the palette (D-107, D-119).

Interim tool until PR-34 ports it to C#. A grid is 16 lines of 16 characters.
Each character is a palette key from content/sprites/palette.json, and a dot
is transparent. The atlas holds every grid in file name order, left to right.

Usage: python3 docs/tools/make-atlas.py [--preview DIR]
  --preview DIR also writes an 8x preview on the night ground into DIR.
"""
import json, struct, sys, zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "content" / "sprites"
SIZE = 16


def fail(msg):
    print(f"make-atlas: {msg}", file=sys.stderr)
    sys.exit(1)


def png(path, w, h, rows):
    raw = b"".join(b"\x00" + b"".join(struct.pack("BBBB", *px) for px in row) for row in rows)
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    data = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
    data += chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.write_bytes(data)


def main():
    palette = json.loads((ROOT / "palette.json").read_text())["colors"]
    rgb = {c["key"]: tuple(int(c["hex"][i:i + 2], 16) for i in (0, 2, 4)) for c in palette}
    grids = sorted(ROOT.glob("*.grid"))
    if not grids:
        fail(f"no .grid file under {ROOT}")
    sprites = []
    for g in grids:
        rows = g.read_text().splitlines()
        if len(rows) != SIZE or any(len(r) != SIZE for r in rows):
            fail(f"{g.name}: a grid is {SIZE} lines of {SIZE} characters")
        for y, r in enumerate(rows):
            for x, ch in enumerate(r):
                if ch != "." and ch not in rgb:
                    fail(f"{g.name}:{y + 1}:{x + 1}: key '{ch}' is not in the palette")
        sprites.append(rows)
    clear = (0, 0, 0, 0)
    sheet = [[(rgb[ch] + (255,)) if ch != "." else clear for s in sprites for ch in s[y]] for y in range(SIZE)]
    png(ROOT / "atlas.png", SIZE * len(sprites), SIZE, sheet)
    print(f"atlas.png: {len(sprites)} sprites, {SIZE * len(sprites)} by {SIZE}")
    if "--preview" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--preview") + 1])
        out.mkdir(parents=True, exist_ok=True)
        night = rgb["K"] + (255,)
        big = [[px for s in sprites for ch in s[y] for px in [(rgb[ch] + (255,)) if ch != "." else night] * 8] for y in range(SIZE) for _ in range(8)]
        png(out / "atlas-8x.png", SIZE * len(sprites) * 8, SIZE * 8, big)
        print(f"{out / 'atlas-8x.png'}: preview")


if __name__ == "__main__":
    main()
