# Pemantau Harga Kripto

Skrip Python (tanpa library tambahan, tanpa API key) yang mengambil harga kripto dari API publik CoinGecko dan menambahkannya ke berkas CSV. Bila jaringan tidak tersedia, skrip berhenti dengan pesan rapi.

Hanya alat pencatat data, bukan saran investasi.

## Cara menjalankan

```bash
python3 pantau_kripto.py                                   # bitcoin, ethereum, solana (USD)
python3 pantau_kripto.py --koin bitcoin dogecoin --mata-uang idr
python3 pantau_kripto.py --demo                            # data contoh tanpa jaringan
```

Jalankan berkala (mis. cron) untuk membangun riwayat harga di `harga_kripto.csv`.

## Contoh keluaran

```
bitcoin              100.00 USD  (1.23% / 24 jam)
ethereum             200.00 USD  (2.47% / 24 jam)
Tersimpan ke harga_kripto.csv
```

Contoh isi CSV ada di `contoh_harga_kripto.csv`.
