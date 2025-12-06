# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
from enum import Enum

# puzzle prompt: https://adventofcode.com/2025/day/4
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
    total = 0
    for direction in Direction:
        search = add_points(grid_point, direction.value)
        if search in grid and grid[search] != ".":
            total += 1
    return total < 4


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    @answer(1551)
    def part_1(self) -> int:
        grid = parse_grid(self.input, ignore_chars=".")
        return sum(fewer_than_four_neighbors(grid_point, grid) for grid_point in grid)

    @answer(9784)
    def part_2(self) -> int:
        grid = parse_grid(self.input)
        total = 0
        while True:
            removed = 0
            grid_new = grid.copy()
            for grid_point in grid:
                if grid[grid_point] == ".":
                    continue
                if fewer_than_four_neighbors(grid_point, grid):
                    grid_new[grid_point] = "."
                    removed += 1
            if removed == 0:
                break
            total += removed
            grid = grid_new
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
