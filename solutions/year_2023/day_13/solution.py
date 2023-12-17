# puzzle prompt: https://adventofcode.com/2023/day/13

from ...base import TextSolution, answer


def distance(above: list[str], below: list[str]) -> int:
    return sum(a != b for a, b in zip(above, below))


def score_block(block: list[list[str]], match_distance: int) -> int:
    if row := reflection_row(block, match_distance):
        return row * 100
    return col if (col := reflection_row(list(zip(*block)), match_distance)) else 0  # type: ignore


def reflection_row(block: list[list[str]], match_distance: int) -> int:
    for idx in range(len(block)):
        if idx == 0:
            continue
        if (
            sum(
                distance(above, below)
                for above, below in zip(reversed(block[:idx]), block[idx:])
            )
            == match_distance
        ):
            return idx
    return 0


class Solution(TextSolution):
    _year = 2023
    _day = 13

    @answer(30487)
    def part_1(self) -> int:
        blocks = [
            [list(row) for row in block.split("\n")]
            for block in list(self.input.split("\n\n"))
        ]
        return sum(score_block(block, 0) for block in blocks)

    # @answer(1234)
    def part_2(self) -> int:
        blocks = [
            [list(row) for row in block.split("\n")]
            for block in list(self.input.split("\n\n"))
        ]
        return sum(score_block(block, 1) for block in blocks)
