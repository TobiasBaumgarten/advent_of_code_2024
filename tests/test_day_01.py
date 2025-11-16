from pathlib import Path
import unittest
from puzzels.day_01 import parse_input, solve_puzzle_1

EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


class TestDay01(unittest.TestCase):
    def test_parse_example(self):
        a, b = parse_input(EXAMPLE_INPUT)

        self.assertEqual(a, [3, 4, 2, 1, 3, 3])
        self.assertEqual(b, [4, 3, 5, 3, 9, 3])

    def test_solve_1_example(self):
        sum = solve_puzzle_1(EXAMPLE_INPUT)
        self.assertEqual(sum, 11)

    def test_solve_1_input(self):
        input = Path("puzzle_input/day_01.txt").read_text()
        sum = solve_puzzle_1(input)
        self.assertEqual(sum, 1580061)


if __name__ == "__main__":
    unittest.main()
