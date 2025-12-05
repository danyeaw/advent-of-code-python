# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer


def find_invalid(start: int, stop: int) -> int:
    invalid = []
    for num in range(start, stop + 1):
        num_str = str(num)
        mid_point = len(num_str) // 2
        if num_str[0] == "0" or num_str[:mid_point] == num_str[mid_point:]:
            invalid.append(num)
    return sum(invalid)


def find_invalid_twice(start: int, stop: int) -> int:
    invalid = []
    for num in range(start, stop + 1):
        num_str = str(num)
        if num_str[0] == "0" or num_str in (num_str + num_str)[1:-1]:
            invalid.append(num)
    return sum(invalid)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ","

    @answer(40055209690)
    def part_1(self) -> int:
        ranges = [
            tuple(int(value) for value in values.split("-")) for values in self.input
        ]
        return sum(find_invalid(range_[0], range_[1]) for range_ in ranges)

    @answer(50857215650)
    def part_2(self) -> int:
        ranges = [
            tuple(int(value) for value in values.split("-")) for values in self.input
        ]
        return sum(find_invalid_twice(range_[0], range_[1]) for range_ in ranges)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
