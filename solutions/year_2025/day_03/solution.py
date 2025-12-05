# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer


def find_highest_two(numbers: list[int]) -> int:
    return max(
        int(f"{numbers[i]}{numbers[j]}")
        for i in range(len(numbers))
        for j in range(i + 1, len(numbers))
    )


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    @answer(17445)
    def part_1(self) -> int:
        batteries = [[int(cell) for cell in bank] for bank in self.input]
        return sum(find_highest_two(bank) for bank in batteries)

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
