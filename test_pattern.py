import unittest

from pattern import build_pattern


class TestBuildPattern(unittest.TestCase):
    def test_n_zero(self):
        self.assertEqual(build_pattern(0), "")

    def test_n_two(self):
        self.assertEqual(build_pattern(2), "a\naa")

    def test_n_three(self):
        self.assertEqual(build_pattern(3), "a\naa\naaa")

    def test_n_four(self):
        self.assertEqual(build_pattern(4), "a\naa\naaa\naaaa")

    def test_any_n(self):
        for n in range(20):
            with self.subTest(n=n):
                lines = build_pattern(n).splitlines()
                self.assertEqual(len(lines), n)
                self.assertEqual(lines, ["a" * count for count in range(1, n + 1)])


if __name__ == "__main__":
    unittest.main()
