# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from collections import Counter

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2086478)
    def part_1(self) -> int:
        first_ids: list[int] = []
        second_ids: list[int] = []
        for line in self.input:
            left, right = line.split()
            first_ids.append(int(left))
            second_ids.append(int(right))
        first_ids = sorted(first_ids)
        second_ids = sorted(second_ids)
        return sum(
            abs(first_ids[num] - second_ids[num]) for num in range(len(first_ids))
        )

    @answer(24941624)
    def part_2(self) -> int:
        first_ids: list[int] = []
        second_ids: list[int] = []
        for line in self.input:
            left, right = line.split()
            first_ids.append(int(left))
            second_ids.append(int(right))
        counter = Counter(second_ids)
        return sum(first_id * counter[first_id] for first_id in first_ids)
