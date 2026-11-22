#!/usr/bin/env python3
"""Mengubah teks ringkas menjadi infografis SVG.

Format berkas masukan:
  baris pertama  = judul
  baris berikutnya = "Judul poin: penjelasan" (satu poin per baris)
"""
import sys
import textwrap
from xml.sax.saxutils import escape

WARNA = ["#e76f51", "#f4a261", "#2a9d8f", "#457b9d", "#8e6bbf", "#d6336c"]
LEBAR = 800


def baca(path):
    with open(path, encoding="utf-8") as f:
        baris = [b.strip() for b in f if b.strip()]
    if len(baris) < 2:
        raise ValueError("Butuh minimal satu judul dan satu poin.")
    poin = []
    for b in baris[1:]:
        kepala, _, isi = b.partition(":")
        poin.append((kepala.strip(), isi.strip()) if isi else (f"Poin {len(poin)+1}", b))
    return baris[0], poin


def buat_svg(judul, poin):
    tinggi_kartu, jarak, atas = 110, 20, 120
    total = atas + len(poin) * (tinggi_kartu + jarak) + 30
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{LEBAR}" height="{total}" '
         f'viewBox="0 0 {LEBAR} {total}" font-family="Arial, sans-serif">',
         f'<rect width="100%" height="100%" fill="#fdf6ec"/>',
         f'<rect width="{LEBAR}" height="90" fill="#264653"/>',
         f'<text x="{LEBAR/2}" y="57" font-size="32" font-weight="bold" fill="#fff" '
         f'text-anchor="middle">{escape(judul)}</text>']
    for i, (kepala, isi) in enumerate(poin):
        y = atas + i * (tinggi_kartu + jarak)
        w = WARNA[i % len(WARNA)]
        o.append(f'<rect x="40" y="{y}" width="{LEBAR-80}" height="{tinggi_kartu}" rx="14" fill="#fff" stroke="{w}" stroke-width="3"/>')
        o.append(f'<circle cx="95" cy="{y+tinggi_kartu/2}" r="30" fill="{w}"/>')
        o.append(f'<text x="95" y="{y+tinggi_kartu/2+10}" font-size="28" font-weight="bold" fill="#fff" text-anchor="middle">{i+1}</text>')
        o.append(f'<text x="150" y="{y+35}" font-size="22" font-weight="bold" fill="{w}">{escape(kepala)}</text>')
        for j, kalimat in enumerate(textwrap.wrap(isi, 62)[:3]):
            o.append(f'<text x="150" y="{y+62+j*20}" font-size="16" fill="#333">{escape(kalimat)}</text>')
        if i < len(poin) - 1:
            cy = y + tinggi_kartu
            o.append(f'<polygon points="{LEBAR/2-10},{cy+3} {LEBAR/2+10},{cy+3} {LEBAR/2},{cy+jarak-3}" fill="#999"/>')
    o.append("</svg>")
    return "\n".join(o)


def main():
    masuk = sys.argv[1] if len(sys.argv) > 1 else "contoh.txt"
    keluar = sys.argv[2] if len(sys.argv) > 2 else "infografis.svg"
    try:
        judul, poin = baca(masuk)
    except (OSError, ValueError) as e:
        sys.exit(f"Gagal: {e}")
    with open(keluar, "w", encoding="utf-8") as f:
        f.write(buat_svg(judul, poin))
    print(f"Infografis '{judul}' dengan {len(poin)} poin disimpan ke {keluar}")


if __name__ == "__main__":
    main()
