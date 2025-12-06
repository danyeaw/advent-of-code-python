# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

import operator
from functools import reduce

from ...base import StrSplitSolution, answer
from ...utils.graphing import parse_grid


def calculate_result(numbers: list[int], operator: str | None, ops: dict) -> int:
    """Calculate result of applying operator to numbers."""
    if numbers and operator:
        return ops[operator](numbers)
    return 0


class Solution(StrSplitSolution):
    _year = 2025
    _day = 6
    separator = "\n"

    @answer(5733696195703)
    def part_1(self) -> int:
        rows = [row.split() for row in self.input]
        columns = list(zip(*rows))
        ops = {"+": sum, "*": lambda v: reduce(operator.mul, v, 1)}
        return sum(ops[col[-1]]([int(x) for x in col[:-1]]) for col in columns)

    @answer(10951882745757)
    def part_2(self) -> int:
        grid = parse_grid(self.input)
        max_x = max(x for x, y in grid)
        max_y = max(y for x, y in grid)

        total = 0
        current_numbers: list[int] = []
        current_operator: str | None = None
        ops = {"+": sum, "*": lambda v: reduce(operator.mul, v, 1)}

        for x in range(max_x, -1, -1):
            col_chars = [grid.get((x, y), " ") for y in range(max_y + 1)]

            if all(c == " " for c in col_chars):
                total += calculate_result(current_numbers, current_operator, ops)
                current_numbers = []
                current_operator = None
                continue

            # Find the last non-space character to check for operator
            non_space_chars = [c for c in col_chars if c != " "]
            if not non_space_chars:
                continue

            if non_space_chars[-1] in "*+":
                current_operator = non_space_chars[-1]
                digits = non_space_chars[:-1]
            else:
                digits = non_space_chars

            if digits:
                current_numbers.append(int("".join(digits)))

        total += calculate_result(current_numbers, current_operator, ops)
        return total
