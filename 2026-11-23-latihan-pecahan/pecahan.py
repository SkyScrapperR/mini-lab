#!/usr/bin/env python3
"""Generator latihan soal pecahan untuk siswa SD (penjumlahan, pengurangan, perkalian)."""
import argparse
import random
from fractions import Fraction


def format_pecahan(f: Fraction) -> str:
    """Tampilkan pecahan; bilangan bulat ditulis tanpa penyebut."""
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def buat_soal(rng: random.Random, maks_penyebut: int):
    """Buat satu soal acak: (teks soal, jawaban Fraction)."""
    def acak():
        d = rng.randint(2, maks_penyebut)
        return Fraction(rng.randint(1, d - 1), d)

    a, b = acak(), acak()
    op = rng.choice(["+", "-", "x"])
    if op == "-" and a < b:
        a, b = b, a  # hindari hasil negatif
    hasil = {"+": a + b, "-": a - b, "x": a * b}[op]
    return f"{format_pecahan(a)} {op} {format_pecahan(b)}", hasil


def parse_jawaban(teks: str) -> Fraction:
    """Terima '3/4', '2', atau '1 1/2' (campuran)."""
    bagian = teks.strip().split()
    if len(bagian) == 2:
        return Fraction(int(bagian[0])) + Fraction(bagian[1])
    return Fraction(bagian[0])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-n", "--jumlah", type=int, default=5, help="jumlah soal")
    p.add_argument("--maks-penyebut", type=int, default=8)
    p.add_argument("--seed", type=int, help="seed acak agar soal bisa diulang")
    p.add_argument("--kunci", action="store_true", help="cetak soal + kunci jawaban tanpa interaksi")
    a = p.parse_args()
    rng = random.Random(a.seed)
    soal = [buat_soal(rng, a.maks_penyebut) for _ in range(a.jumlah)]

    if a.kunci:
        for i, (s, h) in enumerate(soal, 1):
            print(f"{i}. {s} = {format_pecahan(h)}")
        return

    benar = 0
    for i, (s, h) in enumerate(soal, 1):
        try:
            jwb = parse_jawaban(input(f"{i}. {s} = "))
        except (ValueError, ZeroDivisionError, IndexError):
            jwb = None
        except EOFError:
            print("\n(input berhenti)")
            break
        if jwb == h:
            benar += 1
            print("   Benar!")
        else:
            print(f"   Belum tepat. Jawaban: {format_pecahan(h)}")
    print(f"Skor: {benar}/{a.jumlah}")


if __name__ == "__main__":
    main()
