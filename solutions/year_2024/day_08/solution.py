# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
# puzzle prompt: https://adventofcode.com/2024/day/8

from itertools import combinations

from ...base import StrSplitSolution, answer
from ...utils.graphing import (
    Grid,
    GridPoint,
    add_points,
    draw_grid,
    parse_grid,
    subtract_points,
)


def find_antinodes(grid: Grid, antenna_type: str) -> set[GridPoint]:
    positions = [k for k, v in grid.items() if v == antenna_type]
    if len(positions) == 1:
        return set(positions)
    antenna_pairs = combinations(positions, r=2)
    antinodes = set()
    for antenna_pair in antenna_pairs:
        diff: GridPoint = subtract_points(antenna_pair[1], antenna_pair[0])
        lower_antinode = subtract_points(antenna_pair[0], diff)
        if lower_antinode in grid:
            antinodes.add(lower_antinode)
        upper_antinode = add_points(antenna_pair[1], diff)
        if upper_antinode in grid:
            antinodes.add(upper_antinode)
    return antinodes


class Solution(StrSplitSolution):
    _year = 2024
    _day = 8

    @answer(254)
    def part_1(self) -> int:
        grid = parse_grid(self.input)
        antenna_types = {
            antenna_type for antenna_type in grid.values() if antenna_type != "."
        }
        total_antinodes: set[GridPoint] = set()
        for antenna_type in antenna_types:
            antinodes = find_antinodes(grid, antenna_type)
            total_antinodes = total_antinodes | antinodes
        draw_grid(grid, total_antinodes)
        return len(total_antinodes)

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
