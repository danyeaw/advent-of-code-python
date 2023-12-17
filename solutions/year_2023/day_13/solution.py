# puzzle prompt: https://adventofcode.com/2023/day/13

from ...base import TextSolution, answer


def score_block(block: list[list[str]]) -> int:
    if row := reflection_row(block):
        return row * 100
    return col if (col := reflection_row(list(zip(*block)))) else 0  # type: ignore


def reflection_row(block: list[list[str]]) -> int:
    for idx in range(len(block)):
        if idx == 0:
            continue
        if all(
            above == below for above, below in zip(reversed(block[:idx]), block[idx:])
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
        return sum(score_block(block) for block in blocks)

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
