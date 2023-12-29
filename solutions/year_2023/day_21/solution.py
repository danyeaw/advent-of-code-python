# puzzle prompt: https://adventofcode.com/2023/day/21
from collections import defaultdict, deque
from typing import Iterator

from ...base import StrSplitSolution

GraphPoint = tuple[int, int]


class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: list[GraphPoint] = []

    def in_bounds(self, loc: GraphPoint) -> bool:
        (x, y) = loc
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, loc: GraphPoint) -> bool:
        return loc not in self.walls

    def neighbors(self, loc: GraphPoint) -> Iterator[GraphPoint]:
        (x, y) = loc
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0:
            neighbors.reverse()  # S N W E
        results = filter(self.in_bounds, neighbors)
        return filter(self.passable, results)


def breadth_first_search(
    graph: SquareGrid, start: GraphPoint, steps: int
) -> defaultdict[GraphPoint, set[int]]:
    frontier: deque[tuple[GraphPoint, int]] = deque()
    breadth = 1
    frontier.append((start, breadth))
    reached: defaultdict[GraphPoint, set[int]] = defaultdict(set)
    while frontier:
        current, breadth = frontier.popleft()
        if breadth <= steps:
            # print(f"  Visiting {current} with breadth {breadth}")
            for neighbor in graph.neighbors(current):
                if steps not in reached[neighbor]:
                    frontier.append((neighbor, breadth + 1))
                    reached[neighbor].add(breadth)
            print(breadth)
    return reached


class Solution(StrSplitSolution):
    _year = 2023
    _day = 21

    # @answer(1234)
    def part_1(self) -> int:
        garden_map = [list(row) for row in self.input]
        walls = []
        for row_num, row in enumerate(garden_map):
            for col_num, char in enumerate(row):
                if char == "#":
                    walls.append((col_num, row_num))
                elif char == "S":
                    node: GraphPoint = (col_num, row_num)
        graph = SquareGrid(width=len(garden_map[0]), height=len(garden_map))
        graph.walls = walls
        steps = 64
        # reached = [loc for loc, value in breadth_first_search(graph=graph, start=node, steps).items() if 6 in value]
        # print(reached)
        # for row_num, row in enumerate(garden_map):
        #     for col_num, char in enumerate(row):
        #         if (col_num, row_num) in reached:
        #             print("O", end="")
        #         elif (col_num, row_num) in walls:
        #             print("#", end="")
        #         else:
        #             print(".", end="")
        #     print()
        return len(
            [
                value
                for value in breadth_first_search(
                    graph=graph, start=node, steps=steps
                ).values()
                if steps in value
            ]
        )

    # @answer(1234)
    def part_2(self) -> int:
        return 0
