# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
from itertools import combinations
from math import isqrt

# puzzle prompt: https://adventofcode.com/2025/day/8
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 8

    @answer(164475)
    def part_1(self) -> int:
        boxes = [tuple(int(value) for value in box.split(",")) for box in self.input]

        distances = [
            (
                box1,
                box2,
                isqrt(
                    (box2[0] - box1[0]) ** 2
                    + (box2[1] - box1[1]) ** 2
                    + (box2[2] - box1[2]) ** 2
                ),
            )
            for box1, box2 in combinations(boxes, 2)
        ]
        distances.sort(key=lambda x: x[2])

        strands: list[set[tuple[int, ...]]] = []
        for box1, box2, _ in distances[:1000]:
            # Find which strands contain these boxes
            strand1 = next((s for s in strands if box1 in s), None)
            strand2 = next((s for s in strands if box2 in s), None)

            if strand1 is None and strand2 is None:
                strands.append({box1, box2})
            elif strand1 is strand2:
                continue
            elif strand1 is None:
                assert strand2
                strand2.add(box1)
            elif strand2 is None:
                strand1.add(box2)
            else:
                strand1.update(strand2)
                strands.remove(strand2)

        strands.sort(key=len, reverse=True)
        return len(strands[0]) * len(strands[1]) * len(strands[2])

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
