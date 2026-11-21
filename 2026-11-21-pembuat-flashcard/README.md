# Pembuat Flashcard

Mengubah file teks kosakata (`indonesia = inggris`, satu pasang per baris) menjadi
flashcard HTML yang bisa dibalik dengan klik, plus berkas CSV (bisa diimpor ke Anki).

## Cara menjalankan

```
python3 buat_flashcard.py kosakata.txt          # urutan asli
python3 buat_flashcard.py kosakata.txt --acak   # diacak
```

Buka `flashcard.html` di browser. Baris kosong dan yang diawali `#` diabaikan.

## Contoh keluaran

```
Selesai: 10 kartu -> flashcard.html, flashcard.csv
```
