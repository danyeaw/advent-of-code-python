# puzzle prompt: https://adventofcode.com/2023/day/5
from ...base import TextSolution, answer


def parse_range(line: str) -> tuple[range, int]:
    dest_start, source_start, rng = [int(val) for val in line.split()]
    return range(source_start, source_start + rng), dest_start - source_start


def parse_map(map_block: str) -> list[tuple[range, int]]:
    return sorted(
        [parse_range(line) for line in map_block.split("\n")[1:]],
        key=lambda r: r[0].start,
    )


def layer_transform(num: int, layer: list[tuple[range, int]]) -> int:
    for mask, offset in layer:
        if num in mask:
            return num + offset
    return num


class Solution(TextSolution):
    _year = 2023
    _day = 5

    @answer(251346198)
    def part_1(self) -> int:
        blocks = self.input.split("\n\n")
        seeds = [int(seed) for seed in blocks[0][6:].split()]
        map_layers = [parse_map(block) for block in blocks[1:]]

        locations = []
        for seed in seeds:
            for layer in map_layers:
                seed = layer_transform(seed, layer)
            locations.append(seed)
        return min(locations)

    # @answer(1234)
    def part_2(self) -> int:
        pass
