#!/usr/bin/env python3
"""Simulasi pelemparan dadu untuk belajar peluang (matematika SD/PGSD).

Pemakaian:
    python3 simulasi_dadu.py                    # 1 dadu, 600 lemparan
    python3 simulasi_dadu.py -n 6000 -d 2       # 2 dadu, 6000 lemparan
    python3 simulasi_dadu.py --seed 42          # hasil bisa diulang
"""
import argparse
import random
from collections import Counter
from itertools import product


def peluang_teori(jumlah_dadu):
    """Peluang teoretis tiap jumlah mata dadu (dihitung dari semua kemungkinan)."""
    semua = Counter(sum(k) for k in product(range(1, 7), repeat=jumlah_dadu))
    total = 6 ** jumlah_dadu
    return {m: c / total for m, c in sorted(semua.items())}


def simulasi(n, jumlah_dadu, rng):
    """Lempar dadu sebanyak n kali, hitung frekuensi tiap jumlah mata."""
    return Counter(sum(rng.randint(1, 6) for _ in range(jumlah_dadu)) for _ in range(n))


def tampilkan(frekuensi, teori, n):
    print(f"{'Mata':>4} {'Frek':>6} {'Empiris':>8} {'Teori':>8}  Diagram")
    for mata, p in teori.items():
        f = frekuensi.get(mata, 0)
        batang = "#" * round(f / n * 100)
        print(f"{mata:>4} {f:>6} {f / n:>8.3f} {p:>8.3f}  {batang}")


def main():
    ap = argparse.ArgumentParser(description="Simulasi lemparan dadu dan perbandingan dengan peluang teori.")
    ap.add_argument("-n", "--lemparan", type=int, default=600, help="jumlah lemparan (default 600)")
    ap.add_argument("-d", "--dadu", type=int, default=1, help="jumlah dadu per lemparan (1-4)")
    ap.add_argument("--seed", type=int, default=None, help="seed acak agar hasil bisa diulang")
    a = ap.parse_args()
    if a.lemparan < 1 or not 1 <= a.dadu <= 4:
        ap.error("lemparan harus >= 1 dan dadu antara 1 sampai 4")
    rng = random.Random(a.seed)
    print(f"Melempar {a.dadu} dadu sebanyak {a.lemparan} kali\n")
    tampilkan(simulasi(a.lemparan, a.dadu, rng), peluang_teori(a.dadu), a.lemparan)
    print("\nSemakin banyak lemparan, peluang empiris makin mendekati peluang teori.")


if __name__ == "__main__":
    main()
