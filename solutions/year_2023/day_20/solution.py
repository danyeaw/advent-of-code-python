# puzzle prompt: https://adventofcode.com/2023/day/20

import graphviz

from ...base import TextSolution


class Solution(TextSolution):
    _year = 2023
    _day = 20

    # @answer(1234)
    def part_1(self) -> int:
        graphviz.Source.from_file("solutions/year_2023/day_20/graph.gv")
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
