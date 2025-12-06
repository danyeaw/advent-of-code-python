# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

import operator
from functools import reduce

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 6
    separator = "\n"

    @answer(5733696195703)
    def part_1(self) -> int:
        rows = [row.split() for row in self.input]
        columns = list(zip(*rows))
        ops = {"+": sum, "*": lambda v: reduce(operator.mul, v, 1)}
        return sum(ops[col[-1]]([int(x) for x in col[:-1]]) for col in columns)

    # @answer(1234)
    def part_2(self) -> int:
        rows = [row.split() for row in self.input]
        print(rows)
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
