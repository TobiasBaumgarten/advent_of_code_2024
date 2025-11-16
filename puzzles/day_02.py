def parse_input(input: str) -> list[list[int]]:
    """Parses the input of advent of code 2024/2"""
    result: list[list[int]] = []

    for line in input.splitlines():
        report = list(map(int, line.split()))
        result.append(report)

    return result


def is_report_safe(report: list[int]) -> bool:
    """Checks if the given report is safe"""
    length = len(report) - 1

    # check the first rule: "The levels are either all increasing or all decreasing."
    assending = report[0] < report[1]
    is_sorted = all((report[i] < report[i + 1]) == assending for i in range(length))

    # check the second rule: "Any two adjacent levels differ by at least one and at most three."
    is_range_safe = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(length))

    return is_range_safe and is_sorted


def solve_puzzle_1(input: str) -> int:
    """Returns how many reports are safe"""
    reports = parse_input(input)
    return sum(is_report_safe(r) for r in reports)
