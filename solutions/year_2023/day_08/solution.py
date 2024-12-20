# puzzle prompt: https://adventofcode.com/2023/day/8
import itertools
import math

from ...base import TextSolution, answer


def parse(lines: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    inputs = lines.split("\n\n")
    left_right = [
        int(direction) for direction in inputs[0].replace("L", "0").replace("R", "1")
    ]
    node_lines = inputs[1].split("\n")
    nodes = [
        [node.split(" = ")[0], tuple(node.split(" = ")[1].strip("()").split(", "))]
        for node in node_lines
    ]
    node_to_node: dict[str, tuple[str, str]] = dict(nodes)  # type: ignore
    return left_right, node_to_node


class Solution(TextSolution):
    _year = 2023
    _day = 8

    @answer(19241)
    def part_1(self) -> int:
        left_right, node_to_node = parse(self.input)
        location = "AAA"
        count = 0
        for direction in itertools.cycle(left_right):
            location = node_to_node[location][direction]
            count += 1
            if location == "ZZZ":
                break
        return count

    @answer(9606140307013)
    def part_2(self) -> int:
        left_right, node_to_node = parse(self.input)
        locations = [
            init_location for init_location in node_to_node if init_location[2] == "A"
        ]
        start_end_loop = [[0, 0] for _ in range(6)]
        for count, direction in enumerate(itertools.cycle(left_right)):
            for idx, node in enumerate(locations):
                locations[idx] = node_to_node[node][direction]
            for idx, location in enumerate(locations):
                if location[2] == "Z":
                    if start_end_loop[idx][0] == 0:
                        start_end_loop[idx][0] = count
                    elif start_end_loop[idx][1] == 0:
                        start_end_loop[idx][1] = count
            if all(
                loop_length[0] != 0 and loop_length[1] != 0
                for loop_length in start_end_loop
            ):
                break
        loop_lengths = [
            start_end_loop[idx][1] - start_end_loop[idx][0]
            for idx in range(len(start_end_loop))
        ]
        return math.lcm(*loop_lengths)
