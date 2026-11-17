import unittest
from kalkulator_posisi import hitung

class Uji(unittest.TestCase):
    def test_long(self):
        h = hitung(1000, 1, 100, 95, 115)
        self.assertAlmostEqual(h["ukuran_unit"], 2.0)
        self.assertAlmostEqual(h["risk_reward"], 3.0)
        self.assertEqual(h["arah"], "long")
    def test_short(self):
        h = hitung(1000, 1, 100, 105, 90)
        self.assertEqual(h["arah"], "short")
        self.assertAlmostEqual(h["risk_reward"], 2.0)
    def test_error(self):
        with self.assertRaises(ValueError):
            hitung(1000, 1, 100, 100)

if __name__ == "__main__":
    unittest.main()
