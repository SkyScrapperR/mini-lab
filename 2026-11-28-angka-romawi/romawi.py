"""Konverter angka biasa <-> angka Romawi (1-3999) untuk belajar matematika SD."""
import sys

PASANGAN = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def ke_romawi(n):
    """Ubah bilangan bulat 1-3999 menjadi angka Romawi."""
    if not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("Angka harus bilangan bulat 1-3999")
    hasil = []
    for nilai, simbol in PASANGAN:
        while n >= nilai:
            hasil.append(simbol)
            n -= nilai
    return "".join(hasil)


def ke_angka(romawi):
    """Ubah angka Romawi menjadi bilangan biasa; tolak penulisan yang tidak baku."""
    teks = romawi.strip().upper()
    if not teks or any(c not in "IVXLCDM" for c in teks):
        raise ValueError(f"'{romawi}' bukan angka Romawi yang valid")
    nilai = dict((s[-1] if len(s) == 1 else s, v) for v, s in PASANGAN if len(s) == 1)
    total = 0
    for i, c in enumerate(teks):
        if i + 1 < len(teks) and nilai[c] < nilai[teks[i + 1]]:
            total -= nilai[c]
        else:
            total += nilai[c]
    if not 1 <= total <= 3999 or ke_romawi(total) != teks:
        raise ValueError(f"'{romawi}' bukan penulisan angka Romawi yang baku")
    return total


def konversi(masukan):
    masukan = masukan.strip()
    if masukan.isdigit():
        return ke_romawi(int(masukan))
    return str(ke_angka(masukan))


def uji():
    kasus = {1: "I", 4: "IV", 9: "IX", 14: "XIV", 40: "XL", 90: "XC",
             444: "CDXLIV", 1994: "MCMXCIV", 2026: "MMXXVI", 3999: "MMMCMXCIX"}
    for angka, romawi in kasus.items():
        assert ke_romawi(angka) == romawi, (angka, romawi)
        assert ke_angka(romawi) == angka, (romawi, angka)
    for n in range(1, 4000):
        assert ke_angka(ke_romawi(n)) == n
    for salah in ["IIII", "VX", "IC", "ABC", ""]:
        try:
            ke_angka(salah)
        except ValueError:
            continue
        raise AssertionError(f"seharusnya ditolak: {salah!r}")
    print("Semua uji lulus (1-3999 bolak-balik).")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--uji":
        uji()
        return
    if len(sys.argv) > 1:
        daftar = sys.argv[1:]
    else:
        daftar = input("Masukkan angka atau angka Romawi: ").split()
    for item in daftar:
        try:
            print(f"{item} = {konversi(item)}")
        except ValueError as e:
            print(f"{item}: {e}")


if __name__ == "__main__":
    main()
