import unittest
from pathlib import Path

from puzzles.day_03 import Parser, parse_input_1, solve_puzzle


class TestDay02(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.EXAMPLE = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )

    def test_parse_example(self):
        result = parse_input_1(self.EXAMPLE)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], (2, 4))

    def test_solve_1_example(self):
        safe_reports = solve_puzzle(self.EXAMPLE)
        self.assertEqual(safe_reports, 161)

    def test_solve_1_input(self):
        input = Path("puzzle_input/day_03.txt").read_text()
        safe_reports = solve_puzzle(input)
        self.assertEqual(safe_reports, 188741603)

    def test_solve_2_input(self):
        input = Path("puzzle_input/day_03.txt").read_text()
        safe_reports = solve_puzzle(input, Parser.PART2)
        self.assertEqual(safe_reports, 67269798)


if __name__ == "__main__":
    unittest.main()
