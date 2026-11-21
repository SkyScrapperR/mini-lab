#!/usr/bin/env python3
"""Membuat flashcard (HTML interaktif + CSV) dari file teks kosakata Indonesia-Inggris."""
import csv, html, random, sys


def baca_kosakata(path):
    """Baca baris 'indonesia = inggris'; abaikan baris kosong dan komentar (#)."""
    pasangan = []
    with open(path, encoding="utf-8") as f:
        for no, baris in enumerate(f, 1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue
            if "=" not in baris:
                print(f"Peringatan: baris {no} dilewati (tidak ada '=')", file=sys.stderr)
                continue
            a, b = (x.strip() for x in baris.split("=", 1))
            if a and b:
                pasangan.append((a, b))
    return pasangan


def tulis_csv(pasangan, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["indonesia", "inggris"])
        w.writerows(pasangan)


def tulis_html(pasangan, path):
    kartu = "\n".join(
        f'<div class="kartu" onclick="this.classList.toggle(\'balik\')">'
        f'<div class="muka depan">{html.escape(a)}</div>'
        f'<div class="muka belakang">{html.escape(b)}</div></div>'
        for a, b in pasangan
    )
    isi = f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8"><title>Flashcard</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{{font-family:sans-serif;background:#f4f1ea;margin:0;padding:1rem}}
h1{{text-align:center}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}}
.kartu{{position:relative;height:100px;cursor:pointer;perspective:600px}}
.muka{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
border-radius:10px;font-size:1.1rem;text-align:center;padding:6px;backface-visibility:hidden;
transition:transform .4s;box-shadow:0 1px 4px #0003}}
.depan{{background:#fff}}.belakang{{background:#2f6f5e;color:#fff;transform:rotateY(180deg)}}
.kartu.balik .depan{{transform:rotateY(180deg)}}.kartu.balik .belakang{{transform:rotateY(360deg)}}
</style></head><body><h1>Flashcard ({len(pasangan)} kartu)</h1>
<p style="text-align:center">Klik kartu untuk membaliknya.</p>
<div class="grid">
{kartu}
</div></body></html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(isi)


def main():
    sumber = sys.argv[1] if len(sys.argv) > 1 else "kosakata.txt"
    acak = "--acak" in sys.argv
    try:
        pasangan = baca_kosakata(sumber)
    except OSError as e:
        sys.exit(f"Gagal membaca {sumber}: {e}")
    if not pasangan:
        sys.exit("Tidak ada kosakata yang valid.")
    if acak:
        random.shuffle(pasangan)
    tulis_csv(pasangan, "flashcard.csv")
    tulis_html(pasangan, "flashcard.html")
    print(f"Selesai: {len(pasangan)} kartu -> flashcard.html, flashcard.csv")


if __name__ == "__main__":
    main()
