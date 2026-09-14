#!/usr/bin/env python3
"""Render content/sprites/atlas.png from the grids and the palette (D-107, D-119).

OUT OF DATE (D-406). The 16 by 16 grids and atlas.png that this tool reads left
the repository on 2026-09-14 (D-405), so a run now fails with "no .grid file".
The sprite format is 32 by 32 (D-228), and the approved sample grids live in
docs/samples/2026-09-14-cast-sprites/ (D-402). Keep this file as a reference:
PR-34 ports it to the C# atlas command for the new format, then retires it.

Interim tool until PR-34 ports it to C#. A grid is 16 lines of 16 characters.
Each character is a palette key from content/sprites/palette.json, and a dot
is transparent. The atlas holds every grid in file name order, left to right.

Usage: python3 docs/tools/make-atlas.py [--check] [--preview DIR]
  --check       decodes the committed atlas.png and compares its pixels with
                the grids, and writes nothing. The comparison reads pixels,
                never file bytes, because the compressed bytes depend on the
                zlib build and on the encoder (PR-34 emits other bytes).
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


def decode(path):
    """Read an 8-bit RGBA PNG with filter type 0 on every row, the form this tool writes."""
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"{path.name} is not a PNG file")
    pos, w, h = 8, 0, 0
    idat = b""
    while pos < len(data):
        n = struct.unpack(">I", data[pos:pos + 4])[0]
        t = data[pos + 4:pos + 8]
        body = data[pos + 8:pos + 8 + n]
        if t == b"IHDR":
            w, h, depth, color = struct.unpack(">IIBB", body[:10])
            if (depth, color) != (8, 6):
                fail(f"{path.name} is not 8-bit RGBA")
        elif t == b"IDAT":
            idat += body
        pos += 12 + n
    raw = zlib.decompress(idat)
    stride = 1 + 4 * w
    rows = []
    for y in range(h):
        line = raw[y * stride:(y + 1) * stride]
        if line[0] != 0:
            fail(f"{path.name} row {y} uses filter {line[0]}, and this reader handles filter 0 alone")
        rows.append([tuple(line[1 + 4 * x:5 + 4 * x]) for x in range(w)])
    return w, h, rows


def main():
    palette = json.loads((ROOT / "palette.json").read_text())["colors"]
    rgb = {}
    for c in palette:
        if c["key"] in rgb:
            fail(f"palette key '{c['key']}' is defined twice")
        rgb[c["key"]] = tuple(int(c["hex"][i:i + 2], 16) for i in (0, 2, 4))
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
    if "--check" in sys.argv:
        w, h, rows = decode(ROOT / "atlas.png")
        if (w, h) != (SIZE * len(sprites), SIZE):
            fail(f"atlas.png is {w} by {h}, and the grids give {SIZE * len(sprites)} by {SIZE}")
        for y in range(h):
            for x in range(w):
                if rows[y][x] != sheet[y][x]:
                    fail(f"atlas.png differs from the grids at pixel {x},{y}: {rows[y][x]} against {sheet[y][x]}")
        print(f"atlas.png matches the grids: {len(sprites)} sprites, {w} by {h}")
        return
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
