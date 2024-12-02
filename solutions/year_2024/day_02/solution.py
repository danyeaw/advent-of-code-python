# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

import itertools

from ...base import StrSplitSolution, answer


def is_safe(report: list[int]) -> bool:
    differences = [y - x for (x, y) in itertools.pairwise(report)]
    return all(0 < difference < 4 for difference in differences) or all(
        0 > difference > -4 for difference in differences
    )

def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe(report):
        return True
    for idx in range(len(report)):
        damped_report = report.copy()
        damped_report.pop(idx)
        if is_safe(damped_report):
            return True
    return False


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(334)
    def part_1(self) -> int:
        data = [line.split() for line in self.input]
        reports = [[int(value) for value in line] for line in data]
        return sum([is_safe(report) for report in reports])

    @answer(400)
    def part_2(self) -> int:
        data = [line.split() for line in self.input]
        reports = [[int(value) for value in line] for line in data]
        return sum([is_safe_with_dampener(report) for report in reports])
