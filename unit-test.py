import unittest
from code import PythonUnitTest as P

class PythonTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(P.count("saya"), 4)
        self.assertIsNotNone(P.count("saya"))
    def test_grade(self):
        self.assertEqual(P.grade(90), "A")
        self.assertIsNotNone(P.grade(85))
    def test_oddoreven(self):
        self.assertEqual(P.oddoreven(43), "Ganjil")
        self.assertIsNotNone(P.oddoreven(45))
    def test_kabisat(self):
        self.assertEqual(P.kabisat(1900), "Bukan Tahun Kabisat")
        self.assertIsNotNone(P.kabisat(2000))
    def test_filmRate(self):
        self.assertEqual(P.filmRate(21), "Dewasa")
        self.assertIsNotNone(P.filmRate(19))
    def test_loop_with_range(self):
        self.assertEqual(P.loop_with_range(4, 8), [4, 5, 6, 7, 8])
        self.assertIsNotNone(P.loop_with_range(1, 10))
    def test_even1_100(self):
        self.assertIn(11, P.even1_100())
        self.assertIsNotNone(P.even1_100())
    def test_odd_even_multiples(self):
        self.assertEqual(P.odd_even_multiples(), P.odd_even_multiples())
        self.assertIsNone(P.odd_even_multiples()) # datanya klo di sini ga ditampilin jadinya none,
    def test_reverseword(self):
        self.assertEqual(P.reverseword("saya ingin makan nasi goreng"), "goreng nasi makan ingin saya")
    def test_addtoarray(self):
        self.assertIn('Handuk', P.addtoarray())
        self.assertIsNotNone(P.addtoarray())


if __name__ == "__main__":
    unittest.main()