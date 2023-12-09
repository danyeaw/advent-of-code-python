# puzzle prompt: https://adventofcode.com/2023/day/8
from itertools import cycle

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 8

    @answer(19241)
    def part_1(self) -> int:
        inputs = self.input.split("\n\n")
        left_right = [
            int(direction)
            for direction in inputs[0].replace("L", "0").replace("R", "1")
        ]
        nodes = inputs[1].split("\n")
        nodes = [
            [node.split(" = ")[0], tuple(node.split(" = ")[1].strip("()").split(", "))]
            for node in nodes
        ]
        node_to_node = dict(nodes)
        location = "AAA"
        count = 0
        for direction in cycle(left_right):
            location = node_to_node[location][direction]
            count += 1
            if location == "ZZZ":
                break
        return count

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
