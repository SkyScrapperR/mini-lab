"""Statistik teks: hitung kata, kalimat, paragraf, kata terpanjang, dan kata tersering."""
import re
import sys
from collections import Counter

# Kata umum bahasa Indonesia yang diabaikan pada daftar kata tersering
KATA_UMUM = {"yang", "dan", "di", "ke", "dari", "itu", "ini", "untuk", "dengan",
             "pada", "adalah", "dalam", "atau", "juga", "akan", "sebuah", "saya"}


def analisis(teks, top=5):
    """Mengembalikan dict statistik dari sebuah teks."""
    kata = re.findall(r"[A-Za-zÀ-ÿ']+", teks.lower())
    kalimat = [k for k in re.split(r"[.!?]+", teks) if k.strip()]
    paragraf = [p for p in re.split(r"\n\s*\n", teks) if p.strip()]
    bermakna = [k for k in kata if k not in KATA_UMUM and len(k) > 2]
    return {
        "karakter": len(teks),
        "kata": len(kata),
        "kalimat": len(kalimat),
        "paragraf": len(paragraf),
        "rata_kata_per_kalimat": round(len(kata) / len(kalimat), 1) if kalimat else 0,
        "kata_terpanjang": max(kata, key=len) if kata else "",
        "waktu_baca_menit": round(len(kata) / 200, 1),  # ~200 kata/menit
        "tersering": Counter(bermakna).most_common(top),
    }


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            teks = f.read()
    else:
        teks = sys.stdin.read()
    h = analisis(teks)
    print(f"Karakter            : {h['karakter']}")
    print(f"Kata                : {h['kata']}")
    print(f"Kalimat             : {h['kalimat']}")
    print(f"Paragraf            : {h['paragraf']}")
    print(f"Rata-rata kata/kal. : {h['rata_kata_per_kalimat']}")
    print(f"Kata terpanjang     : {h['kata_terpanjang']}")
    print(f"Perkiraan waktu baca: {h['waktu_baca_menit']} menit")
    print("Kata tersering      :")
    for k, n in h["tersering"]:
        print(f"  {k:<12} {'#' * n} ({n})")


if __name__ == "__main__":
    main()
