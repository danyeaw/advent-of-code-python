# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer


def find_invalid(start: int, stop: int) -> int:
    return sum(
        num
        for num in range(start, stop + 1)
        if (num_str := str(num))[0] == "0"
        or num_str[: len(num_str) // 2] == num_str[len(num_str) // 2 :]
    )


def find_invalid_twice(start: int, stop: int) -> int:
    return sum(
        num
        for num in range(start, stop + 1)
        if (num_str := str(num))[0] == "0" or num_str in (num_str + num_str)[1:-1]
    )


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ","

    def parse_ranges(self):
        return [
            tuple[int, ...](int(value) for value in values.split("-"))
            for values in self.input
        ]

    @answer(40055209690)
    def part_1(self) -> int:
        return sum(find_invalid(start, stop) for start, stop in self.parse_ranges())

    @answer(50857215650)
    def part_2(self) -> int:
        return sum(
            find_invalid_twice(start, stop) for start, stop in self.parse_ranges()
        )
