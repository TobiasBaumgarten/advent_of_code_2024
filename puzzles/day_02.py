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


def solve_puzzle_2(input: str) -> int:
    reports = parse_input(input)
    sum_safe_reports = 0

    for report in reports:
        if is_report_safe(report):
            sum_safe_reports += 1
            continue

        # when the report isn't safe remove a part of the list and check it again
        is_mod_report_safe = False

        for idx in range(len(report)):
            mod_report = report[:idx] + report[idx + 1 :]
            if is_report_safe(mod_report):
                is_mod_report_safe = True
                break

        if is_mod_report_safe:
            sum_safe_reports += 1

    return sum_safe_reports
