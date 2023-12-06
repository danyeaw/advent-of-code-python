# puzzle prompt: https://adventofcode.com/2023/day/5
import re
from itertools import batched

from ...base import TextSolution, answer


def parse(text: str) -> list[list[list[int]]]:
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
    return [[[int(val) for val in row] for row in map] for map in maps]


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
        for start_seed, rng in batched(seeds, 2):
            for seed in range(start_seed, start_seed + rng):
                value = seed
                for map in maps:
                    for row in map:
                        if row[1] <= value <= row[1] + row[2]:
                            value = row[0] + value - row[1]
                            break
                locations.append(value)
        return min(locations)
