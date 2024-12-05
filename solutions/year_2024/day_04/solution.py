# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
# puzzle prompt: https://adventofcode.com/2024/day/4

from collections.abc import Iterator

from ...base import StrSplitSolution

GridPoint = tuple[int, int]
Grid = dict[GridPoint, str]


def parse_grid(raw_grid: list[str], ignore_chars: str = "") -> Grid:
    result: Grid = {}
    for row, line in enumerate(raw_grid):
        for col, char in enumerate(line):
            if char == ignore_chars:
                continue
            result[row, col] = char
    return result


def add_points(a: GridPoint, b: GridPoint) -> GridPoint:
    return a[0] + b[0], a[1] + b[1]


def subtract_points(a: GridPoint, b: GridPoint) -> GridPoint:
    return a[0] - b[0], a[1] - b[1]


OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def neighbors(
    center: GridPoint,
    max_size: int | None,
    num_directions=8,
    diagonals=False,
) -> Iterator[tuple[int, int]]:
    assert num_directions in {4, 8, 9}

    for offset_x, offset_y in OFFSETS:
        if diagonals and not (offset_x and offset_y):
            # orthogonal; skip
            continue
        if num_directions == 4 and not diagonals and offset_x and offset_y:
            # diagonal; skip
            continue
        if num_directions != 9 and not (offset_x or offset_y):
            # skip self
            continue
        next_x, next_y = add_points(center, (offset_x, offset_y))
        # max size implies a min size
        if max_size and (next_x < 0 or next_y < 0):
            continue
        if max_size and (next_x > max_size or next_y > max_size):
            continue
        yield next_x, next_y


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        grid = parse_grid(self.input)
        total = 0
        for center, letter in grid.items():
            if letter != "X":
                continue
            for neighbor in neighbors(center, max_size=len(self.input) - 1):
                if grid[neighbor] != "M":
                    continue
                offset = subtract_points(neighbor, center)
                next_letter = add_points(neighbor, offset)
                if (
                    grid.get(next_letter) == "A"
                    and grid.get(add_points(next_letter, offset)) == "S"
                ):
                    total += 1
        return total

    # @answer(1234)
    def part_2(self) -> int:
        grid = parse_grid(self.input)
        total = 0
        for center, letter in grid.items():
            cross_sections = 0
            if letter != "A":
                continue
            for neighbor in neighbors(
                center, max_size=len(self.input) - 1, num_directions=4, diagonals=True
            ):
                if grid[neighbor] != "M":
                    continue
                offset = subtract_points(center, neighbor)
                next_letter = add_points(center, offset)
                if grid.get(next_letter) == "S":
                    cross_sections += 1
            if cross_sections == 2:
                total += 1
        return total
