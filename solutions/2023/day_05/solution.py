# puzzle prompt: https://adventofcode.com/2023/day/5
import re

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 5

    @answer(251346198)
    def part_1(self) -> int:
        seeds = [
            int(seed)
            for seed in re.search(r"seeds:.*\n", self.input)
            .group()
            .split(": ")[1]
            .split()
        ]
        text = re.sub(r"seeds:.*\n\n", "", self.input)
        text = re.sub(r".*:.*\n", "", text).split("\n\n")
        maps = [[map.split() for map in group.split("\n")] for group in text]
        maps = [[[int(val) for val in row] for row in map] for map in maps]

        locations = []
        for seed in seeds:
            value = seed
            for map in maps:
                for row in map:
                    if row[1] <= value <= row[1] + row[2]:
                        value = row[0] + value - row[1]
                        break
            locations.append(value)
        return min(locations)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
