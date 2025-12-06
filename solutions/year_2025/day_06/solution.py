# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

import operator
from functools import reduce

from ...base import StrSplitSolution, answer


def math_operation(op: str, values: list[int]) -> int:
    if op == "+":
        return sum(values)
    if op == "*":
        return reduce(operator.mul, values, 1)
    return 0


class Solution(StrSplitSolution):
    _year = 2025
    _day = 6
    separator = "\n"

    @answer(5733696195703)
    def part_1(self) -> int:
        rows = [[num for num in row.split(" ") if num] for row in self.input]
        columns = [list(col) for col in zip(*rows)]
        return sum(
            math_operation(column[-1], [int(x) for x in column[:-1]])
            for column in columns
        )

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
