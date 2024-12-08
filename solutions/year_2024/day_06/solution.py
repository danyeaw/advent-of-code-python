# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6
from ...base import StrSplitSolution, answer
from ...utils.graphing import Grid, GridPoint, add_points, parse_grid

direction = {
    "east": (0, 1),
    "north": (-1, 0),
    "south": (1, 0),
    "west": (0, -1),
}


def rotate(current_direction: str) -> str:
    if current_direction == "north":
        return "east"
    if current_direction == "east":
        return "south"
    if current_direction == "south":
        return "west"
    return "north"


def track_guard(grid: Grid) -> set[GridPoint]:
    """Returns an empty set if the guard gets stuck in a loop."""
    position = next(k for k, v in grid.items() if v == "^")
    current_direction = "north"
    visited = set()
    while True:
        visited.add((position, current_direction))
        next_position = add_points(position, direction[current_direction])
        if next_position not in grid:
            break
        if grid[next_position] == "#":
            current_direction = rotate(current_direction)
            next_position = position
        if (next_position, current_direction) in visited:
            return set()
        position = next_position
    return {position for position, _ in visited}


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    @answer((5269, 1957))
    def solve(self) -> tuple[int, int]:
        grid = parse_grid(self.input)
        path = track_guard(grid)
        path_size = len(path)
        possible_obstructions = 0
        for position in path:
            if grid[position] != ".":
                continue
            grid[position] = "#"
            path = track_guard(grid)
            if not path:
                possible_obstructions += 1
            grid[position] = "."

        return path_size, possible_obstructions
