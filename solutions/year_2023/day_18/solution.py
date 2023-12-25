# puzzle prompt: https://adventofcode.com/2023/day/18
from solutions.base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 18

    @answer(76387)
    def part_1(self) -> int:
        lines = [line.split() for line in self.input]
        plan = [
            (direction, int(distance), color) for direction, distance, color in lines
        ]
        x, y, perimeter = 0, 0, 0
        lagoon: list[tuple[int, int]] = [(0, 0)]
        for direction, distance, _ in plan:
            dx, dy = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}[direction]
            x, y = x + dx * distance, y + dy * distance
            lagoon.append((x, y))
            perimeter += distance
        print(lagoon)
        print(lagoon[1:])
        print(list(zip(lagoon, lagoon[1:])))
        for a, b in zip(lagoon, lagoon[1:]):
            print("a", a)
            print("b", b)
        shoelace = (
            sum((a[0] * b[1] - b[0] * a[1]) for a, b in zip(lagoon, lagoon[1:])) // 2
        )
        return shoelace + perimeter // 2 + 1

    # @answer(1234)
    def part_2(self) -> int:
        return 0
