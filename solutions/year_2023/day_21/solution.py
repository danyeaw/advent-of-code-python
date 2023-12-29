# puzzle prompt: https://adventofcode.com/2023/day/21
from collections import deque
from typing import Iterator

from ...base import StrSplitSolution

GraphPoint = tuple[int, int]


class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.rocks: list[GraphPoint] = []

    def in_bounds(self, loc: GraphPoint) -> bool:
        (x, y) = loc
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, loc: GraphPoint) -> bool:
        return loc not in self.rocks

    def neighbors(self, loc: GraphPoint) -> Iterator[GraphPoint]:
        (x, y) = loc
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0:
            neighbors.reverse()  # S N W E
        results = filter(self.in_bounds, neighbors)
        return filter(self.passable, results)


def breadth_first_search(
    graph: SquareGrid, start: GraphPoint, step_length: int
) -> tuple[int, set[GraphPoint]]:
    frontier: deque[tuple[GraphPoint, int]] = deque()
    result = breadth = 0
    frontier.append((start, breadth))
    reached: set[GraphPoint] = set()
    reachable: set[GraphPoint] = set()
    while frontier:
        current, breadth = frontier.popleft()
        if breadth > step_length:
            continue

        # If the parity of the step matches the step length
        # It is reachable and doesn't need to be searched again
        if current in reached:
            continue
        if breadth % 2 == step_length % 2:
            result += 1
            reachable.add(current)

        reached.add(current)
        for neighbor in graph.neighbors(current):
            frontier.append((neighbor, breadth + 1))
    return result, reachable


def draw_garden(
    garden_map: list[list[str]], reached: set[GraphPoint], rocks: list[GraphPoint]
) -> None:
    for row_num, row in enumerate(garden_map):
        for col_num, char in enumerate(row):
            if (col_num, row_num) in reached:
                print("O", end="")
            elif (col_num, row_num) in rocks:
                print("#", end="")
            else:
                print(".", end="")
        print()


class Solution(StrSplitSolution):
    _year = 2023
    _day = 21

    # @answer(1234)
    def part_1(self) -> int:
        garden_map = [list(row) for row in self.input]
        rocks = []
        start: GraphPoint = (0, 0)
        for row_num, row in enumerate(garden_map):
            for col_num, char in enumerate(row):
                if char == "#":
                    rocks.append((col_num, row_num))
                elif char == "S":
                    start = (col_num, row_num)
        graph = SquareGrid(width=len(garden_map[0]), height=len(garden_map))
        graph.rocks = rocks
        step_length = 6 if self.use_test_data else 64
        result, reached = breadth_first_search(graph, start, step_length)
        if self.use_test_data:
            draw_garden(garden_map, reached, rocks)
        return result

    # @answer(1234)
    def part_2(self) -> int:
        return 0
