# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
from itertools import combinations
from math import isqrt

# puzzle prompt: https://adventofcode.com/2025/day/8
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 8

    def parse_boxes(self) -> list[tuple[int, ...]]:
        return [tuple(int(value) for value in box.split(",")) for box in self.input]

    def _calculate_distances(
        self, boxes: list[tuple[int, ...]]
    ) -> list[tuple[tuple[int, ...], tuple[int, ...], int]]:
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
        return distances

    def connect_boxes(
        self,
        distances: list[tuple[tuple[int, ...], tuple[int, ...], int]],
        max_pairs: int | None = None,
        stop_when_unified: bool = False,
    ) -> tuple[
        list[set[tuple[int, ...]]], tuple[tuple[int, ...], tuple[int, ...]] | None
    ]:
        strands: list[set[tuple[int, ...]]] = []
        last_connection = None

        for i, (box1, box2, _) in enumerate(distances):
            if max_pairs is not None and i >= max_pairs:
                break

            strand1 = next((s for s in strands if box1 in s), None)
            strand2 = next((s for s in strands if box2 in s), None)

            if strand1 is strand2 and strand1 is not None:
                continue

            strands_before = len(strands)

            if strand1 is None and strand2 is None:
                strands.append({box1, box2})
            elif strand1 is None:
                assert strand2
                strand2.add(box1)
            elif strand2 is None:
                strand1.add(box2)
            else:
                strand1.update(strand2)
                strands.remove(strand2)

            if stop_when_unified and strands_before > 1 and len(strands) == 1:
                last_connection = (box1, box2)
                break

        return strands, last_connection

    @answer(164475)
    def part_1(self) -> int:
        boxes = self.parse_boxes()
        distances = self._calculate_distances(boxes)
        strands, _ = self.connect_boxes(distances, max_pairs=1000)
        strands.sort(key=len, reverse=True)
        if len(strands) < 3:
            result = 1
            for strand in strands:
                result *= len(strand)
            return result
        return len(strands[0]) * len(strands[1]) * len(strands[2])

    @answer(169521198)
    def part_2(self) -> int:
        boxes = self.parse_boxes()
        distances = self._calculate_distances(boxes)
        _, last_connection = self.connect_boxes(distances, stop_when_unified=True)
        assert last_connection is not None
        return last_connection[0][0] * last_connection[1][0]
