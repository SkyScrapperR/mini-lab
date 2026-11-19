#!/usr/bin/env python3
"""Generator jadwal piket mingguan dan pembagian kelompok acak dari daftar nama."""
import argparse
import random

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]


def baca_nama(path):
    """Baca nama dari file, satu nama per baris; abaikan baris kosong dan duplikat."""
    with open(path, encoding="utf-8") as f:
        nama = [b.strip() for b in f if b.strip()]
    return list(dict.fromkeys(nama))


def buat_piket(nama, rng):
    """Bagi nama ke hari Senin-Jumat secara acak dan merata."""
    acak = nama[:]
    rng.shuffle(acak)
    jadwal = {h: [] for h in HARI}
    for i, n in enumerate(acak):
        jadwal[HARI[i % len(HARI)]].append(n)
    return jadwal


def buat_kelompok(nama, jumlah, rng):
    """Bagi nama ke sejumlah kelompok secara acak dan merata."""
    acak = nama[:]
    rng.shuffle(acak)
    kelompok = [[] for _ in range(jumlah)]
    for i, n in enumerate(acak):
        kelompok[i % jumlah].append(n)
    return kelompok


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("berkas", help="file teks berisi nama (satu per baris)")
    p.add_argument("--mode", choices=["piket", "kelompok"], default="piket")
    p.add_argument("--jumlah", type=int, default=4, help="jumlah kelompok")
    p.add_argument("--seed", type=int, help="biji acak agar hasil bisa diulang")
    a = p.parse_args()

    nama = baca_nama(a.berkas)
    if not nama:
        raise SystemExit("Daftar nama kosong.")
    rng = random.Random(a.seed)

    if a.mode == "piket":
        print("JADWAL PIKET")
        for h, orang in buat_piket(nama, rng).items():
            print(f"{h:7}: {', '.join(orang) if orang else '-'}")
    else:
        if not 1 <= a.jumlah <= len(nama):
            raise SystemExit(f"--jumlah harus 1 sampai {len(nama)}.")
        print("PEMBAGIAN KELOMPOK")
        for i, k in enumerate(buat_kelompok(nama, a.jumlah, rng), 1):
            print(f"Kelompok {i} ({len(k)} orang): {', '.join(k)}")


if __name__ == "__main__":
    main()
