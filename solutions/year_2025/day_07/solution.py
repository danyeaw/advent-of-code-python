# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
from enum import Enum

# puzzle prompt: https://adventofcode.com/2025/day/7
from ...base import StrSplitSolution, answer
from ...utils.graphing import Grid, GridPoint, add_points, parse_grid


class Direction(Enum):
    E = (1, 0)
    S = (0, 1)
    W = (-1, 0)


def split_beams(start_pos: GridPoint, diagram: Grid) -> int:
    beams: set[GridPoint] = {add_points(start_pos, (0, 2))}
    visited: set[GridPoint] = set()
    total = 0

    while beams:
        next_beams = set()
        for beam in beams:
            if beam in visited or beam not in diagram:
                continue
            visited.add(beam)
            element = diagram[beam]
            if element in ("S", "."):
                next_beams.add(add_points(beam, Direction.S.value))
            elif element == "^":
                split1 = add_points(beam, Direction.W.value)
                split2 = add_points(beam, Direction.E.value)
                if split1 not in next_beams:
                    next_beams.add(split1)
                if split2 not in next_beams:
                    next_beams.add(split2)
                total += 1

        beams = next_beams

    return total


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    @answer(1690)
    def part_1(self) -> int:
        diagram = parse_grid(self.input)
        start_pos: GridPoint = next(
            key for key, value in diagram.items() if value == "S"
        )
        return split_beams(start_pos, diagram)

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
