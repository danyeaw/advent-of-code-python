# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 5
    separator = "\n\n"

    @answer(607)
    def part_1(self) -> int:
        fresh_ranges_str, available_ids_str = self.input
        fresh_tuples = [
            tuple(int(num) for num in nums_str.split("-"))
            for nums_str in fresh_ranges_str.split("\n")
        ]
        fresh_ranges = [
            range(id_range[0], id_range[1] + 1) for id_range in fresh_tuples
        ]
        available_ids = [int(available) for available in available_ids_str.split("\n")]
        return sum(1 for i in available_ids if any(i in rng for rng in fresh_ranges))

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
