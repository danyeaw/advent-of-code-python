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

    @answer(89823704)
    def part_2(self) -> int:
        pattern = re.compile(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)")
        match_iter = re.finditer(pattern, self.input)
        enable_sum = True
        total = 0
        for match in match_iter:
            if match.group(0) == "don't()":
                enable_sum = False
            elif match.group(0) == "do()":
                enable_sum = True
            elif enable_sum:
                total += int(match.group(3)) * int(match.group(4))
        return total
