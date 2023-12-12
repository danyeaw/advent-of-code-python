# puzzle prompt: https://adventofcode.com/2023/day/3
import re
from math import prod
from typing import Any

from ...base import StrSplitSolution, answer


def get_symbol_coord_to_adjacent_num(
    schematic: str,
) -> dict[tuple[int, int], list[Any]]:
    width = len(schematic[0])
    height = len(schematic)
    symbol_coord_to_adjacent_num: dict[tuple[int, int], list[int]] = {
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
            for coord in adjacent_area & symbol_coord_to_adjacent_num.keys():
                symbol_coord_to_adjacent_num[coord].append(int(num.group()))
    return symbol_coord_to_adjacent_num


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    @answer(520019)
    def part_1(self) -> int:
        return sum(
            sum(value)
            for value in get_symbol_coord_to_adjacent_num(self.input).values()
        )

    @answer(75519888)
    def part_2(self) -> int:
        # There are no symbols except *'s that are adjacent to exactly two numbers
        return sum(
            prod(value)
            for value in get_symbol_coord_to_adjacent_num(self.input).values()
            if len(value) == 2
        )
