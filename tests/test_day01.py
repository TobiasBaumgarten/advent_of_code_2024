from pathlib import Path
import unittest
from puzzles.day_01 import solve_puzzle_1, solve_puzzle_2, parse_input


class TestDay01(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.EXAMPLE_INPUT = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    def test_parse_example(self):
        a, b = parse_input(self.EXAMPLE_INPUT)

        self.assertEqual(a, [3, 4, 2, 1, 3, 3])
        self.assertEqual(b, [4, 3, 5, 3, 9, 3])

    def test_solve_1_example(self):
        sum = solve_puzzle_1(self.EXAMPLE_INPUT)
        self.assertEqual(sum, 11)

    def test_solve_1_input(self):
        input = Path("puzzle_input/day_01.txt").read_text()
        sum = solve_puzzle_1(input)
        self.assertEqual(sum, 1580061)

    def test_solve_2_example(self):
        sum = solve_puzzle_2(self.EXAMPLE_INPUT)
        self.assertEqual(sum, 31)

    def test_solve_2_input(self):
        input = Path("puzzle_input/day_01.txt").read_text()
        sum = solve_puzzle_2(input)
        self.assertEqual(sum, 23046913)


if __name__ == "__main__":
    unittest.main()
