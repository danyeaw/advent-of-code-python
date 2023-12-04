# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
import re
from collections import Counter

# puzzle prompt: https://adventofcode.com/2023/day/4

from ...base import answer, StrSplitSolution


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(28750)
    def part_1(self) -> int:
        total_worth = []
        for line in self.input:
            _, numbers = line.replace("  ", " ").split(": ")
            winners, my_numbers = numbers.split(" | ")
            winners = winners.split(" ")
            my_numbers = my_numbers.split(" ")
            winners = [int(num) for num in winners]
            my_numbers = [int(num) for num in my_numbers]
            if intersect := set(winners).intersection(my_numbers):
                total_worth.append(2**(len(intersect)) // 2)
        return sum(total_worth)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
