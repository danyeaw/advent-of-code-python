# puzzle prompt: https://adventofcode.com/2023/day/3
import re
from math import prod

from ...base import StrSplitSolution, answer


def get_coord_adjacent_symbol_to_number(schematic: str) -> dict[str, list]:
    width = len(schematic[0])
    height = len(schematic)
    coord_adjacent_symbol_to_number = {
        (r, c): []
        for r in range(width)
        for c in range(height)
        if schematic[r][c] not in "01234566789."
    }
    for row_num, row in enumerate(schematic):
        for num in re.finditer(r"\d+", row):
            adjacent_area = {
                (r, c)
                for r in (row_num - 1, row_num, row_num + 1)
                for c in range(num.start() - 1, num.end() + 1)
            }
            for coord in adjacent_area & coord_adjacent_symbol_to_number.keys():
                coord_adjacent_symbol_to_number[coord].append(int(num.group()))
    return coord_adjacent_symbol_to_number


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    @answer(520019)
    def part_1(self) -> int:
        return sum(
            sum(value)
            for value in get_coord_adjacent_symbol_to_number(self.input).values()
        )

    @answer(75519888)
    def part_2(self) -> int:
        # There are no symbols except *'s that are adjacent to exactly two numbers
        return sum(
            prod(value)
            for value in get_coord_adjacent_symbol_to_number(self.input).values()
            if len(value) == 2
        )
