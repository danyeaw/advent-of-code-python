# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer


def combine_ranges(ranges: list[tuple[int, ...]]) -> int:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    total = 0
    current_start, current_end = sorted_ranges[0][0], sorted_ranges[0][1]
    for start, end in sorted_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            total += current_end - current_start + 1
            current_start, current_end = start, end
    total += current_end - current_start + 1
    return total


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

    @answer(342433357244012)
    def part_2(self) -> int:
        fresh_ranges_str, _ = self.input
        fresh_tuples = [
            tuple(int(num) for num in nums_str.split("-"))
            for nums_str in fresh_ranges_str.split("\n")
        ]
        return combine_ranges(fresh_tuples)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
