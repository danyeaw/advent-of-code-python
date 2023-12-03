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
                    start_idx = int(match.start())
                    end_idx = int(match.end())
                    left_area_idx = max(start_idx - 1, 0)
                    right_area_idx = min(end_idx + 1, len(current_row))
                    if previous_row:
                        area.append(previous_row[left_area_idx:right_area_idx])
                    area.extend(
                        (
                            current_row[left_area_idx:right_area_idx],
                            next_row[left_area_idx:right_area_idx],
                        )
                    )
                    matching_numbers.extend(
                        int(current_row[start_idx:end_idx])
                        for row in area
                        for char in row
                        if char in SYMBOLS
                    )
            previous_row = current_row
            current_row = next_row
        return sum(matching_numbers)

    @answer(75519888)
    def part_2(self) -> int:
        matching_numbers = []
        previous_row = None
        current_row = None
        width = len(self.input[0])
        self.input.append("." * width)
        for next_row in self.input:
            if current_row:
                for match in re.finditer(r"\*", current_row):
                    full_rows = []
                    area = []
                    start_idx = int(match.start())
                    end_idx = int(match.end())
                    left_area_idx = max(start_idx - 1, 0)
                    right_area_idx = min(end_idx + 1, len(current_row))
                    if previous_row:
                        full_rows.append(previous_row)
                        area.append(previous_row[left_area_idx:right_area_idx])
                    area.extend(
                        (
                            current_row[left_area_idx:right_area_idx],
                            next_row[left_area_idx:right_area_idx],
                        )
                    )
                    full_rows.extend([current_row, next_row])
                    numbers = []
                    for row in full_rows:
                        for int_match in re.finditer(r"\d+", row):
                            num_start = int_match.start()
                            num_end = int_match.end()
                            if (
                                left_area_idx <= num_start < right_area_idx
                                or left_area_idx < num_end <= right_area_idx
                            ):
                                numbers.append(int(int_match.group()))
                    if len(numbers) == 2:
                        matching_numbers.append(numbers[0] * numbers[1])

            previous_row = current_row
            current_row = next_row
        return sum(matching_numbers)
