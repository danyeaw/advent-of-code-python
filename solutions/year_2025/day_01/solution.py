# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


def move_dial(current_location: int, direction: str, distance: int) -> int:
    if direction == "L":
        distance = -distance
    return (current_location + distance) % 100

class Solution(StrSplitSolution):
    _year = 2025
    _day = 1


    @answer(1084)
    def part_1(self) -> int:
        location = 50
        zero_counter = 0
        rotations = [(line[0], int(line[1:])) for line in self.input]
        for rotation in rotations:
            location = move_dial(location, rotation[0], rotation[1])
            if location == 0:
                zero_counter += 1
        return zero_counter



    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
