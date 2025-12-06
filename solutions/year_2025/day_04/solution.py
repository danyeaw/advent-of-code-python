# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4
from enum import Enum

from ...base import StrSplitSolution, answer
from ...utils.graphing import Grid, GridPoint, add_points, parse_grid


class Direction(Enum):
    NW = (-1, 1)
    N = (0, 1)
    NE = (1, 1)
    E = (1, 0)
    SE = (1, -1)
    S = (0, -1)
    SW = (-1, -1)
    W = (-1, 0)


def fewer_than_four_neighbors(grid_point: GridPoint, grid: Grid) -> bool:
    neighbors = sum(
        1 for direction in Direction if add_points(grid_point, direction.value) in grid
    )
    return neighbors < 4


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    @answer(1551)
    def part_1(self) -> int:
        grid = parse_grid(self.input, ignore_chars=".")
        return sum(fewer_than_four_neighbors(grid_point, grid) for grid_point in grid)

    @answer(9784)
    def part_2(self) -> int:
        grid = parse_grid(self.input, ignore_chars=".")
        total = 0
        while True:
            to_remove = [
                grid_point
                for grid_point in grid
                if fewer_than_four_neighbors(grid_point, grid)
            ]
            if not to_remove:
                break
            for grid_point in to_remove:
                del grid[grid_point]
            total += len(to_remove)
        return total
