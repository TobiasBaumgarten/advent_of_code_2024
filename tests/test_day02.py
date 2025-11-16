import unittest
from pathlib import Path

from puzzles.day_02 import parse_input, solve_puzzle_1, solve_puzzle_2


class TestDay02(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.EXAMPLE = """7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9"""

    def test_parse_example(self):
        result = parse_input(self.EXAMPLE)
        self.assertEqual(result[0], [7, 6, 4, 2, 1])
        self.assertEqual(result[-1], [1, 3, 6, 7, 9])

    def test_solve_1_example(self):
        safe_reports = solve_puzzle_1(self.EXAMPLE)
        self.assertEqual(safe_reports, 2)

    def test_solve_2_example(self):
        safe_reports = solve_puzzle_2(self.EXAMPLE)
        self.assertEqual(safe_reports, 4)

    def test_solve_1_input(self):
        input = Path("puzzle_input/day_02.txt").read_text()
        safe_reports = solve_puzzle_1(input)
        self.assertEqual(safe_reports, 624)

    def test_solve_2_input(self):
        input = Path("puzzle_input/day_02.txt").read_text()
        safe_reports = solve_puzzle_2(input)
        self.assertEqual(safe_reports, 658)


if __name__ == "__main__":
    unittest.main()
