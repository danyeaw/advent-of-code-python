# puzzle prompt: https://adventofcode.com/2023/day/5
from itertools import batched, chain

from ...base import TextSolution, answer


def parse_range(line: str) -> tuple[range, int]:
    dest_start, source_start, rng = [int(val) for val in line.split()]
    return range(source_start, source_start + rng), dest_start - source_start


def parse_map(map_block: str) -> list[tuple[range, int]]:
    return sorted(
        [parse_range(line) for line in map_block.split("\n")[1:]],
        key=lambda r: r[0].start,
    )


def do_ranges_overlap(a: range, b: range) -> bool:
    return a.start < b.stop and b.start < a.stop


def shift_range(r: range, offset: int) -> range:
    return range(r.start + offset, r.stop + offset)


def layer_transform(num: int, layer: list[tuple[range, int]]) -> int:
    return next((num + offset for mask, offset in layer if num in mask), num)


def apply_transformations(
    base: range, transforms: list[tuple[range, int]]
) -> list[range]:
    for mask, offset in transforms:
        # 1 - no overlap; skip this mask
        if not do_ranges_overlap(base, mask):
            continue

        # 2 - base is inside mask, shift entire base
        if mask.start <= base.start and base.stop <= mask.stop:
            return [shift_range(base, offset)]

        # 3 - mask is a subset of base
        # return unshifted left, shifted middle, and recurse for the rest
        if base.start <= mask.start and mask.stop <= base.stop:
            return [
                range(base.start, mask.start),
                shift_range(mask, offset),
                *apply_transformations(range(mask.stop, base.stop), transforms),
            ]

        # 4 - mask overlaps only the left side,
        # return masked left, recurse for the rest
        if mask.start <= base.start and mask.stop <= base.stop:
            return [
                shift_range(range(base.start, mask.stop), offset),
                *apply_transformations(range(mask.stop, base.stop), transforms),
            ]

        # 5 - mask overlaps only the right side
        # return unshifted left, masked right
        if base.start <= mask.start and base.stop <= mask.stop:
            return [
                range(base.start, mask.start),
                shift_range(range(mask.start, base.stop), offset),
            ]

    # no masks overlapped this base; pass it through
    return [base]


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

    @answer(72263011)
    def part_2(self) -> int:
        blocks = self.input.split("\n\n")
        seeds = [int(seed) for seed in blocks[0][6:].split()]
        seeds = [range(start, start + rng) for start, rng in batched(seeds, 2)]
        locations = []
        map_layers = [parse_map(block) for block in blocks[1:]]
        for seed_range in seeds:
            ranges = [seed_range]
            for layer in map_layers:
                ranges = list(
                    chain.from_iterable(apply_transformations(r, layer) for r in ranges)
                )
            locations.append(sorted(ranges, key=lambda r: r.start)[0].start)
        locations = [loc for loc in locations if loc != 0]
        return min(locations)
