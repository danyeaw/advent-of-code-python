# puzzle prompt: https://adventofcode.com/2023/day/3
import re

from ...base import StrSplitSolution, answer

SYMBOLS = ("*", "@", "#", "$", "%", "&", "*", "/", "=", "+", "-")


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    @answer(520019)
    def part_1(self) -> int:
        matching_numbers = []
        previous_row = None
        current_row = None
        width = len(self.input[0])
        self.input.append("." * width)
        for next_row in self.input:
            if current_row:
                for match in re.finditer(r"\d+", current_row):
                    area = []
                    left_num_idx = int(match.span()[0])
                    right_num_idx = int(match.span()[1])
                    left_area_idx = max(left_num_idx - 1, 0)
                    right_area_idx = min(right_num_idx + 1, len(current_row))
                    if previous_row:
                        area.append(previous_row[left_area_idx:right_area_idx])
                    area.extend(
                        (
                            current_row[left_area_idx:right_area_idx],
                            next_row[left_area_idx:right_area_idx],
                        )
                    )
                    matching_numbers.extend(
                        int(current_row[left_num_idx:right_num_idx])
                        for row in area
                        for char in row
                        if char in SYMBOLS
                    )
            previous_row = current_row
            current_row = next_row
        return sum(matching_numbers)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
