"""Kalkulator keliling dan luas bangun datar.

Jalankan tanpa argumen untuk mode interaktif, atau pakai argumen CLI:
    python3 bangun_datar.py persegi 5
    python3 bangun_datar.py persegi_panjang 8 3
    python3 bangun_datar.py segitiga 3 4 5
    python3 bangun_datar.py lingkaran 7
    python3 bangun_datar.py trapesium 4 6 3 2 2.5   (a, b, tinggi, kaki1, kaki2)
    python3 bangun_datar.py jajar_genjang 6 4 5     (alas, tinggi, sisi miring)
    python3 bangun_datar.py belah_ketupat 6 8       (diagonal1, diagonal2)
    python3 bangun_datar.py layang_layang 6 8 5 4   (diag1, diag2, sisi a, sisi b)
"""
import math
import sys


def _positif(*nilai):
    if any(v <= 0 for v in nilai):
        raise ValueError("Semua ukuran harus lebih besar dari 0.")


def persegi(s):
    _positif(s)
    return 4 * s, s * s


def persegi_panjang(p, l):
    _positif(p, l)
    return 2 * (p + l), p * l


def segitiga(a, b, c):
    _positif(a, b, c)
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ketiga sisi tidak membentuk segitiga.")
    k = a + b + c
    s = k / 2
    luas = math.sqrt(s * (s - a) * (s - b) * (s - c))  # rumus Heron
    return k, luas


def lingkaran(r):
    _positif(r)
    return 2 * math.pi * r, math.pi * r * r


def trapesium(a, b, t, kaki1, kaki2):
    _positif(a, b, t, kaki1, kaki2)
    return a + b + kaki1 + kaki2, (a + b) * t / 2


def jajar_genjang(alas, tinggi, sisi):
    _positif(alas, tinggi, sisi)
    return 2 * (alas + sisi), alas * tinggi


def belah_ketupat(d1, d2):
    _positif(d1, d2)
    sisi = math.sqrt((d1 / 2) ** 2 + (d2 / 2) ** 2)
    return 4 * sisi, d1 * d2 / 2


def layang_layang(d1, d2, a, b):
    _positif(d1, d2, a, b)
    return 2 * (a + b), d1 * d2 / 2


BANGUN = {
    "persegi": (persegi, ["sisi"]),
    "persegi_panjang": (persegi_panjang, ["panjang", "lebar"]),
    "segitiga": (segitiga, ["sisi a", "sisi b", "sisi c"]),
    "lingkaran": (lingkaran, ["jari-jari"]),
    "trapesium": (trapesium, ["sisi sejajar a", "sisi sejajar b", "tinggi", "kaki 1", "kaki 2"]),
    "jajar_genjang": (jajar_genjang, ["alas", "tinggi", "sisi miring"]),
    "belah_ketupat": (belah_ketupat, ["diagonal 1", "diagonal 2"]),
    "layang_layang": (layang_layang, ["diagonal 1", "diagonal 2", "sisi a", "sisi b"]),
}


def hitung(nama, angka):
    fungsi, params = BANGUN[nama]
    if len(angka) != len(params):
        raise ValueError(f"{nama} butuh {len(params)} ukuran: {', '.join(params)}")
    return fungsi(*angka)


def cetak(nama, angka):
    keliling, luas = hitung(nama, angka)
    print(f"Bangun : {nama.replace('_', ' ')}")
    print(f"Ukuran : {', '.join(str(a) for a in angka)}")
    print(f"Keliling = {keliling:.2f}")
    print(f"Luas     = {luas:.2f}")


def interaktif():
    nama_list = list(BANGUN)
    print("Pilih bangun datar:")
    for i, n in enumerate(nama_list, 1):
        print(f"  {i}. {n.replace('_', ' ')}")
    pilih = int(input("Nomor: ")) - 1
    nama = nama_list[pilih]
    angka = [float(input(f"{p}: ")) for p in BANGUN[nama][1]]
    cetak(nama, angka)


def main(argv):
    try:
        if len(argv) < 2:
            interaktif()
        elif argv[1] in BANGUN:
            cetak(argv[1], [float(x) for x in argv[2:]])
        else:
            print(__doc__)
            return 1
    except (ValueError, IndexError) as e:
        print(f"Kesalahan: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
