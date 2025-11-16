"""
This code solve the puzzle of advent of code 2024 day 1
https://adventofcode.com/2024/day/1
"""


def solve_puzzle_1(input: str) -> int:
    la, lb = parse_input(input)

    la.sort()
    lb.sort()
    sum = 0
    for a, b in list(zip(la, lb)):
        sum += abs(a - b)

    return sum


def parse_input(input: str) -> tuple[list[int], list[int]]:
    """Parses the advent of code 2024/1 input as two int list"""
    a: list[int] = []
    b: list[int] = []
    for line in input.splitlines():
        parts = line.split()
        if len(parts) != 2:
            raise Exception("Error: The input hasn't the right format!", parts)

        a.append(int(parts[0]))
        b.append(int(parts[1]))

    return (a, b)
