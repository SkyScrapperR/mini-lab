# Latihan Pecahan

Generator soal latihan pecahan (penjumlahan, pengurangan, perkalian) untuk siswa SD, dengan penilaian otomatis.

## Cara menjalankan

```bash
python3 pecahan.py                 # 5 soal interaktif
python3 pecahan.py -n 10 --maks-penyebut 12
python3 pecahan.py --seed 1 --kunci   # cetak soal + kunci jawaban
```

Jawaban boleh ditulis `3/4`, `2`, atau campuran `1 1/2`. Hasil dinilai setelah disederhanakan.

## Contoh keluaran (`--seed 1 --kunci -n 3`)

```
1. 1/3 - 1/4 = 1/12
2. 1/2 + 4/5 = 13/10
3. 1/2 - 1/2 = 0
```
