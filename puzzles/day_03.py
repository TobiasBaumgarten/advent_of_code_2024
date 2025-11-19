import re
from enum import Enum


class Parser(Enum):
    PART1 = 1
    PART2 = 2


def parse_input_1(input: str) -> list[tuple[int, int]]:
    """Parser for the first part of the puzzle"""
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    return [
        tuple(map(int, match)) for match in matches
    ]  # parse the matches to int # type: ignore


def parse_input_2(input: str) -> list[tuple[int, int]]:
    """Parser for the second part of the puzzle"""
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\)")

    results = []
    default = True
    enable_mul = default

    # check the matches for do and don't
    for match in pattern.finditer(input):
        if match.group() == "do()":
            enable_mul = True
        elif match.group() == "don't()":
            enable_mul = False
        else:
            # when the mul is enabled add it to the list of results
            if enable_mul:
                group = tuple(map(int, match.groups()))  # parse to int
                results.append(group)
                enable_mul = default  # reset zu default

    return results


def solve_puzzle(input: str, type: Parser = Parser.PART1) -> int:
    """solve the puzzle with the given parser"""
    if type == Parser.PART1:
        numbers = parse_input_1(input)
    else:
        numbers = parse_input_2(input)

    mult_numbers = [a * b for a, b in numbers]
    return sum(mult_numbers)
