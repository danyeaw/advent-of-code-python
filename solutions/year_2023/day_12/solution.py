# puzzle prompt: https://adventofcode.com/2023/day/12
import re

from ...base import StrSplitSolution


class Solution(StrSplitSolution):
    _year = 2023
    _day = 12

    # @answer(1234)
    def part_1(self) -> int:
        for line in self.input:
            record, pattern_str = line.split()
            pattern = [int(value) for value in pattern_str.split(",")]
            record = re.sub(r"\.+", ".", record)
            record = re.sub(r"^\.|\.$", r"", record)
            print(record)
            print(pattern)
            # Dynamic programming here
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
