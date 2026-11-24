# Statistik Teks

Alat kecil Python untuk menganalisis teks: jumlah karakter, kata, kalimat, paragraf, kata terpanjang, perkiraan waktu baca, dan kata tersering (kata umum diabaikan).

## Cara menjalankan

```
python3 statistik_teks.py contoh.txt
# atau lewat stdin
echo "Halo dunia." | python3 statistik_teks.py
```

## Contoh keluaran

```
Karakter            : 189
Kata                : 25
Kalimat             : 4
Paragraf            : 2
Rata-rata kata/kal. : 6.2
Kata terpanjang     : menyenangkan
Perkiraan waktu baca: 0.1 menit
Kata tersering      :
  matematika   ### (3)
  belajar      ## (2)
  guru         ## (2)
  menyenangkan # (1)
  membantu     # (1)
```
