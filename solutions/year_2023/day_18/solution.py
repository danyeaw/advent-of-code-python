# puzzle prompt: https://adventofcode.com/2023/day/18
import itertools

from solutions.base import StrSplitSolution, answer


def solve(plan: list[tuple[str, int]]) -> int:
    x, y, perimeter = 0, 0, 0
    lagoon: list[tuple[int, int]] = [(0, 0)]
    for direction, distance in plan:
        dx, dy = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}[direction]
        x, y = x + dx * distance, y + dy * distance
        lagoon.append((x, y))
        perimeter += distance
    shoelace = (
        sum((a[0] * b[1] - b[0] * a[1]) for a, b in itertools.pairwise(lagoon)) // 2
    )
    return shoelace + perimeter // 2 + 1


class Solution(StrSplitSolution):
    _year = 2023
    _day = 18

    @answer(76387)
    def part_1(self) -> int:
        lines = [line.split() for line in self.input]
        plan = [(direction, int(distance)) for direction, distance, _ in lines]
        return solve(plan)

    # @answer(1234)
    def part_2(self) -> int:
        num_to_dir = {0: "R", 1: "D", 2: "L", 3: "U"}
        plan = [
            (num_to_dir[int(line[-2:-1])], int(line[-7:-2], 16)) for line in self.input
        ]
        return solve(plan)
