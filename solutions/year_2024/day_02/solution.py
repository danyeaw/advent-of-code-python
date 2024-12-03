# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from collections.abc import Iterable
from itertools import pairwise

from ...base import StrSplitSolution, answer
from ...utils.parsing import parse_int_list


def is_strictly_increasing(report: list[int]) -> bool:
    return all(0 < y - x < 4 for (x, y) in pairwise(report))


def is_strictly_decreasing(report: list[int]) -> bool:
    return is_strictly_increasing(report[::-1])


def is_safe(report: list[int]) -> bool:
    return is_strictly_increasing(report) or is_strictly_decreasing(report)


def remove_level(report: list[int]) -> Iterable[list[int]]:
    for idx in range(len(report)):
        yield report[:idx] + report[idx + 1 :]


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(334)
    def part_1(self) -> int:
        reports = [parse_int_list(line.split()) for line in self.input]
        return sum(is_safe(report) for report in reports)

    @answer(400)
    def part_2(self) -> int:
        reports = [parse_int_list(line.split()) for line in self.input]
        return sum(
            is_safe(report)
            or any(is_safe(dampened) for dampened in remove_level(report))
            for report in reports
        )
