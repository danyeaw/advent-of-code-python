# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

import re

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(167090022)
    def part_1(self) -> int:
        pattern = re.compile(r"mul\((\d+),(\d+)\)")
        match_iter = re.finditer(pattern, self.input)
        return sum(int(match.group(1)) * int(match.group(2)) for match in match_iter)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
