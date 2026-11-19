# Generator Jadwal Piket & Kelompok Acak

Membagi daftar nama menjadi jadwal piket Senin–Jumat atau beberapa kelompok secara acak dan merata.

## Cara menjalankan

```
python3 jadwal.py nama-contoh.txt                       # jadwal piket
python3 jadwal.py nama-contoh.txt --mode kelompok --jumlah 4
python3 jadwal.py nama-contoh.txt --seed 1              # hasil bisa diulang
```

File nama: satu nama per baris (baris kosong dan duplikat diabaikan).

## Contoh keluaran (`--mode kelompok --jumlah 4 --seed 1`)

```
PEMBAGIAN KELOMPOK
Kelompok 1 (3 orang): Hadi, Fajar, Eko
Kelompok 2 (3 orang): Laras, Gita, Budi
Kelompok 3 (3 orang): Ani, Dewi, Joko
Kelompok 4 (3 orang): Indah, Kirana, Citra
```
