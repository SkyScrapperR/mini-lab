"""Konverter satuan sederhana (panjang, berat, waktu) untuk belajar matematika SD.

Contoh:
    python3 konverter.py 2.5 km m
    python3 konverter.py 90 menit jam
    python3 konverter.py --tangga panjang   # tampilkan tangga satuan
"""
import argparse
import sys

# Nilai tiap satuan dinyatakan dalam satuan dasar (m, g, detik).
SATUAN = {
    "panjang": {"km": 1000, "hm": 100, "dam": 10, "m": 1, "dm": 0.1, "cm": 0.01, "mm": 0.001},
    "berat": {"ton": 1_000_000, "kuintal": 100_000, "kg": 1000, "hg": 100, "dag": 10, "g": 1, "mg": 0.001},
    "waktu": {"hari": 86400, "jam": 3600, "menit": 60, "detik": 1},
}


def cari_besaran(satuan):
    for besaran, tabel in SATUAN.items():
        if satuan in tabel:
            return besaran
    raise ValueError(f"Satuan tidak dikenal: {satuan}")


def konversi(nilai, dari, ke):
    """Ubah nilai dari satuan `dari` ke satuan `ke` (harus satu besaran)."""
    b1, b2 = cari_besaran(dari), cari_besaran(ke)
    if b1 != b2:
        raise ValueError(f"Tidak bisa mengubah {b1} ({dari}) ke {b2} ({ke})")
    return nilai * SATUAN[b1][dari] / SATUAN[b1][ke]


def format_angka(x):
    return f"{x:.6f}".rstrip("0").rstrip(".")


def main(argv=None):
    p = argparse.ArgumentParser(description="Konverter satuan panjang, berat, waktu.")
    p.add_argument("nilai", nargs="?", type=float)
    p.add_argument("dari", nargs="?")
    p.add_argument("ke", nargs="?")
    p.add_argument("--tangga", choices=list(SATUAN), help="tampilkan urutan satuan")
    a = p.parse_args(argv)
    if a.tangga:
        print(" > ".join(SATUAN[a.tangga]))
        return 0
    if a.nilai is None or not a.dari or not a.ke:
        p.print_usage()
        return 1
    try:
        hasil = konversi(a.nilai, a.dari, a.ke)
    except ValueError as e:
        print(f"Galat: {e}", file=sys.stderr)
        return 2
    print(f"{format_angka(a.nilai)} {a.dari} = {format_angka(hasil)} {a.ke}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
