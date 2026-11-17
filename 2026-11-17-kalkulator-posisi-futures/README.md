# Kalkulator Posisi Futures

Alat hitung (bukan saran investasi): ukuran posisi, risk-reward, margin, leverage aman, dan perkiraan harga likuidasi dari modal, persen risiko, entry, dan stop loss.

## Cara menjalankan

```
python3 kalkulator_posisi.py --modal 1000 --risiko 1 --entry 65000 --stop 63700 --target 68250 --leverage 5
python3 test_kalkulator.py   # uji
```

## Contoh keluaran

```
Arah               : long
Risiko             : 10.00 (1.0% modal)
Jarak stop loss    : 2.00%
Ukuran posisi      : 0.007692 unit
Nilai posisi       : 500.00
Leverage minimum   : 0.50x
Leverage aman maks : 25.0x (buffer 2x jarak stop)
Margin (5.00x)   : 100.00
Likuidasi (kira2)  : 52000.00
Risk-reward        : 1 : 2.50
Potensi untung     : 25.00

Catatan: alat hitung saja, bukan saran investasi.
```

Rumus likuidasi disederhanakan; bursa nyata punya biaya dan margin pemeliharaan.
