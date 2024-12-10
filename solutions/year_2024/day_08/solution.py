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


def find_antinodes(
    grid: Grid, antenna_type: str, resonance: bool = False
) -> set[GridPoint]:
    positions = [k for k, v in grid.items() if v == antenna_type]
    if len(positions) == 1:
        return set(positions)
    antenna_pairs = combinations(positions, r=2)
    antinodes = set()
    for antenna_pair in antenna_pairs:
        diff: GridPoint = subtract_points(antenna_pair[1], antenna_pair[0])
        if not resonance:
            lower_antinode = subtract_points(antenna_pair[0], diff)
            if lower_antinode in grid:
                antinodes.add(lower_antinode)
            upper_antinode = add_points(antenna_pair[1], diff)
            if upper_antinode in grid:
                antinodes.add(upper_antinode)
        else:
            location = antenna_pair[0]
            antinodes.add(location)
            while True:
                new_loc = subtract_points(location, diff)
                if new_loc not in grid:
                    break
                antinodes.add(new_loc)
                location = new_loc
            location = antenna_pair[1]
            antinodes.add(location)
            while True:
                new_loc = add_points(location, diff)
                if new_loc not in grid:
                    break
                antinodes.add(new_loc)
                location = new_loc

    return antinodes


class Solution(StrSplitSolution):
    _year = 2024
    _day = 8

    @answer((254, 951))
    def solve(self) -> tuple[int, int]:
        grid = parse_grid(self.input)
        antenna_types = {
            antenna_type for antenna_type in grid.values() if antenna_type != "."
        }
        total_antinodes: set[GridPoint] = set()
        total_resonance_antinodes: set[GridPoint] = set()
        for antenna_type in antenna_types:
            antinodes = find_antinodes(grid, antenna_type)
            total_antinodes = total_antinodes | antinodes
            resonance_antinodes = find_antinodes(grid, antenna_type, resonance=True)
            total_resonance_antinodes = total_resonance_antinodes | resonance_antinodes
        draw_grid(grid, total_antinodes)
        draw_grid(grid, total_resonance_antinodes)
        return len(total_antinodes), len(total_resonance_antinodes)
