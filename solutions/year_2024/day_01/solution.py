# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2086478)
    def part_1(self) -> int:
        first_ids, second_ids = [], []
        for line in self.input:
            left, right = line.split()
            first_ids.append(int(left))
            second_ids.append(int(right))
        first_ids = sorted(first_ids)
        second_ids = sorted(second_ids)

        return sum(
            abs(first_ids[num] - second_ids[num]) for num in range(len(first_ids))
        )

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
