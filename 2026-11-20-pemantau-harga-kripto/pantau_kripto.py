#!/usr/bin/env python3
"""Pemantau harga kripto lewat API publik CoinGecko (tanpa API key).

Setiap kali dijalankan, harga terbaru ditambahkan sebagai baris baru ke CSV.
Jika jaringan tidak tersedia, program berhenti dengan rapi (tanpa crash).
"""
import argparse
import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta

URL = "https://api.coingecko.com/api/v3/simple/price"
WITA = timezone(timedelta(hours=8))
KOLOM = ["waktu_wita", "koin", "mata_uang", "harga", "perubahan_24j_persen"]


def ambil_harga(koin, mata_uang, timeout=10):
    """Mengembalikan dict hasil API, atau None bila gagal."""
    query = urllib.parse.urlencode({
        "ids": ",".join(koin),
        "vs_currencies": mata_uang,
        "include_24hr_change": "true",
    })
    req = urllib.request.Request(f"{URL}?{query}", headers={"User-Agent": "mini-lab/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as e:
        print(f"Gagal mengambil data (jaringan/API tidak tersedia): {e}", file=sys.stderr)
        return None


def baris_dari_data(data, koin, mata_uang, waktu=None):
    """Mengubah respons API menjadi daftar baris CSV."""
    waktu = waktu or datetime.now(WITA).strftime("%Y-%m-%d %H:%M:%S")
    hasil = []
    for k in koin:
        info = data.get(k)
        if not info or mata_uang not in info:
            print(f"Peringatan: koin '{k}' tidak ditemukan, dilewati.", file=sys.stderr)
            continue
        perubahan = info.get(f"{mata_uang}_24h_change")
        hasil.append([waktu, k, mata_uang, info[mata_uang],
                      "" if perubahan is None else round(perubahan, 2)])
    return hasil


def simpan_csv(path, baris):
    """Menambahkan baris ke CSV; menulis header jika berkas baru."""
    try:
        with open(path, "r", encoding="utf-8"):
            baru = False
    except FileNotFoundError:
        baru = True
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if baru:
            w.writerow(KOLOM)
        w.writerows(baris)


def main():
    p = argparse.ArgumentParser(description="Pemantau harga kripto -> CSV")
    p.add_argument("--koin", nargs="+", default=["bitcoin", "ethereum", "solana"],
                   help="id koin CoinGecko (default: bitcoin ethereum solana)")
    p.add_argument("--mata-uang", default="usd", help="mis. usd atau idr")
    p.add_argument("--csv", default="harga_kripto.csv", help="berkas keluaran")
    p.add_argument("--demo", action="store_true",
                   help="pakai data contoh (tanpa jaringan) untuk mencoba program")
    a = p.parse_args()

    if a.demo:
        data = {k: {a.mata_uang: 100.0 * (i + 1), f"{a.mata_uang}_24h_change": 1.234 * (i + 1)}
                for i, k in enumerate(a.koin)}
    else:
        data = ambil_harga(a.koin, a.mata_uang)
    if data is None:
        print("Tidak ada data yang disimpan. Coba lagi nanti.")
        return 1

    baris = baris_dari_data(data, a.koin, a.mata_uang)
    if not baris:
        print("Tidak ada baris valid untuk disimpan.")
        return 1
    simpan_csv(a.csv, baris)
    for _, k, mu, h, ch in baris:
        print(f"{k:<12} {h:>14,.2f} {mu.upper()}  ({ch}% / 24 jam)")
    print(f"Tersimpan ke {a.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
