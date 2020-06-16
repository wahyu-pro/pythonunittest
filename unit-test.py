import unittest
from code import PythonUnitTest as P

class PythonTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(P.count("saya"), 4)
    def test_grade(self):
        self.assertEqual(P.grade(90), "A")
    def test_oddoreven(self):
        self.assertEqual(P.oddoreven(43), "Ganjil")
    def test_kabisat(self):
        self.assertEqual(P.kabisat(1900), "Bukan Tahun Kabisat")
    def test_filmRate(self):
        self.assertEqual(P.filmRate(21), "Dewasa")
    def test_loop_with_range(self):
        self.assertEqual(P.loop_with_range(4, 8), [4, 5, 6, 7, 8])
    def test_even1_100(self):
        self.assertEqual(P.even1_100(), list)
    def test_odd_even_multiples(self):
        pass
    def test_reverseword(self):
        self.assertEqual(P.reverseword("saya ingin makan nasi goreng"), "goreng nasi makan ingin saya")
    def test_addtoarray(self):
        self.assertIn('Handuk', P.addtoarray())


if __name__ == "__main__":
    unittest.main()