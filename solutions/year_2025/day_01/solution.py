# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


def move_dial(current_location: int, direction: str, distance: int) -> tuple[int, int]:
    step = -1 if direction == "L" else 1
    zeros = 0
    location = current_location

    for _ in range(distance):
        location = (location + step) % 100
        if location == 0:
            zeros += 1

    return location, zeros


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer((1084, 6475))
    def solve(self) -> tuple[int, int]:
        location = 50
        part1_counter = 0
        part2_counter = 0
        rotations = [(line[0], int(line[1:])) for line in self.input]
        for rotation in rotations:
            location, zeros = move_dial(location, rotation[0], rotation[1])
            if location == 0:
                part1_counter += 1
            part2_counter += zeros
        return part1_counter, part2_counter
