"""Kalkulator FPB dan KPK dengan langkah faktorisasi prima (bahan belajar SD)."""
import sys
from collections import Counter
from math import prod


def faktorisasi(n):
    """Mengembalikan Counter {bilangan prima: pangkat} untuk n >= 2."""
    hasil, p = Counter(), 2
    while p * p <= n:
        while n % p == 0:
            hasil[p] += 1
            n //= p
        p += 1
    if n > 1:
        hasil[n] += 1
    return hasil


def tulis(f):
    return " x ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))


def hitung(angka):
    fs = [faktorisasi(a) for a in angka]
    semua = set().union(*fs)
    fpb = prod(p ** min(f[p] for f in fs) for p in semua)
    kpk = prod(p ** max(f[p] for f in fs) for p in semua)
    return fs, fpb, kpk


def main(argv):
    try:
        angka = [int(a) for a in argv]
    except ValueError:
        print("Masukkan bilangan bulat saja.")
        return 1
    if len(angka) < 2 or any(a < 2 for a in angka):
        print("Pemakaian: python fpb_kpk.py 12 18 [24 ...]  (bilangan >= 2)")
        return 1
    fs, fpb, kpk = hitung(angka)
    for a, f in zip(angka, fs):
        print(f"{a} = {tulis(f)}")
    print(f"FPB = {fpb} (pangkat terkecil dari faktor yang sama)")
    print(f"KPK = {kpk} (pangkat terbesar dari semua faktor)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
