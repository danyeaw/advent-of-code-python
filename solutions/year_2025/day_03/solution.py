# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer


def find_highest(numbers: list[int], size: int) -> int:
    start = 0
    result = []
    for i in range(size):
        end = len(numbers) - (size - i - 1)
        max_val = max(numbers[start:end])
        max_idx = numbers.index(max_val, start)
        result.append(max_val)
        start = max_idx + 1
    return int("".join(map[str](str, result)))


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    def parse_batteries(self):
        return [[int(cell) for cell in bank] for bank in self.input]

    @answer(17445)
    def part_1(self) -> int:
        return sum(find_highest(bank, 2) for bank in self.parse_batteries())

    @answer(173229689350551)
    def part_2(self) -> int:
        return sum(find_highest(bank, 12) for bank in self.parse_batteries())
