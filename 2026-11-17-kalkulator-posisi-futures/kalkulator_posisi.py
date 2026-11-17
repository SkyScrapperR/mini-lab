#!/usr/bin/env python3
"""Kalkulator ukuran posisi futures (alat hitung saja, BUKAN saran investasi).

Menghitung ukuran posisi dari modal, persen risiko, harga entry, dan stop loss,
plus risk-reward, margin, dan perkiraan harga likuidasi (disederhanakan).
"""
import argparse


def hitung(modal, risiko_persen, entry, stop, target=None, leverage=None, arah=None):
    if modal <= 0 or entry <= 0 or stop <= 0 or risiko_persen <= 0:
        raise ValueError("Modal, risiko, entry, dan stop loss harus > 0")
    if entry == stop:
        raise ValueError("Entry dan stop loss tidak boleh sama")
    arah = arah or ("long" if stop < entry else "short")
    if (arah == "long") != (stop < entry):
        raise ValueError(f"Stop loss tidak cocok dengan arah {arah}")

    risiko_uang = modal * risiko_persen / 100
    jarak = abs(entry - stop)
    ukuran = risiko_uang / jarak            # jumlah unit/koin
    nilai_posisi = ukuran * entry
    hasil = {
        "arah": arah,
        "risiko_uang": risiko_uang,
        "jarak_stop_persen": jarak / entry * 100,
        "ukuran_unit": ukuran,
        "nilai_posisi": nilai_posisi,
        "leverage_minimum": nilai_posisi / modal,
    }
    # Leverage aman: likuidasi harus jauh di luar stop loss (buffer 2x jarak stop)
    jarak_pct = jarak / entry
    hasil["leverage_aman_maks"] = max(1.0, 1 / (2 * jarak_pct))
    lev = leverage or max(1.0, hasil["leverage_minimum"])
    hasil["leverage_dipakai"] = lev
    hasil["margin"] = nilai_posisi / lev
    sisi = 1 if arah == "long" else -1
    hasil["harga_likuidasi_kira2"] = entry * (1 - sisi / lev)
    if target is not None:
        if (arah == "long") != (target > entry):
            raise ValueError("Target tidak cocok dengan arah posisi")
        hasil["risk_reward"] = abs(target - entry) / jarak
        hasil["potensi_untung"] = ukuran * abs(target - entry)
    return hasil


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--modal", type=float, required=True, help="modal (USDT)")
    p.add_argument("--risiko", type=float, default=1.0, help="risiko per trade, persen")
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--stop", type=float, required=True)
    p.add_argument("--target", type=float)
    p.add_argument("--leverage", type=float)
    a = p.parse_args()
    try:
        h = hitung(a.modal, a.risiko, a.entry, a.stop, a.target, a.leverage)
    except ValueError as e:
        raise SystemExit(f"Error: {e}")
    print(f"Arah               : {h['arah']}")
    print(f"Risiko             : {h['risiko_uang']:.2f} ({a.risiko}% modal)")
    print(f"Jarak stop loss    : {h['jarak_stop_persen']:.2f}%")
    print(f"Ukuran posisi      : {h['ukuran_unit']:.6f} unit")
    print(f"Nilai posisi       : {h['nilai_posisi']:.2f}")
    print(f"Leverage minimum   : {h['leverage_minimum']:.2f}x")
    print(f"Leverage aman maks : {h['leverage_aman_maks']:.1f}x (buffer 2x jarak stop)")
    print(f"Margin ({h['leverage_dipakai']:.2f}x)   : {h['margin']:.2f}")
    print(f"Likuidasi (kira2)  : {h['harga_likuidasi_kira2']:.2f}")
    if "risk_reward" in h:
        print(f"Risk-reward        : 1 : {h['risk_reward']:.2f}")
        print(f"Potensi untung     : {h['potensi_untung']:.2f}")
    print("\nCatatan: alat hitung saja, bukan saran investasi.")


if __name__ == "__main__":
    main()
