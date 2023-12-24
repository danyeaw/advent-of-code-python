# puzzle prompt: https://adventofcode.com/2023/day/17
import queue
from dataclasses import dataclass
from enum import IntEnum

from ...base import StrSplitSolution

GridLocation = tuple[int, int]


class Direction(IntEnum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def parse_grid(raw_grid: list[list[str]]) -> dict[GridLocation, int]:
    result: dict[GridLocation, int] = {}
    for y, line in enumerate(raw_grid):
        for x, char in enumerate(line):
            result[(x, y)] = int(char)
    return result


def draw_tile(graph, id, style):
    r = " . "
    if "number" in style and id in style["number"]:
        r = " %-2d" % style["number"][id]
    if "point_to" in style and style["point_to"].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style["point_to"][id]
        if x2 == x1 + 1:
            r = " > "
        if x2 == x1 - 1:
            r = " < "
        if y2 == y1 + 1:
            r = " v "
        if y2 == y1 - 1:
            r = " ^ "
    if "path" in style and id in style["path"]:
        r = " @ "
    if "start" in style and id == style["start"]:
        r = " A "
    if "goal" in style and id == style["goal"]:
        r = " Z "
    return r


def draw_grid(graph, **style):
    print("___" * graph.width)
    for y in range(graph.height):
        for x in range(graph.width):
            print(f"{draw_tile(graph, (x, y), style)}", end="")
        print()
    print("~~~" * graph.width)


def reconstruct_path(
    came_from: dict[GridLocation, GridLocation], start: GridLocation, goal: GridLocation
) -> list[GridLocation]:
    current: GridLocation = goal
    path: list[GridLocation] = []
    if current not in came_from:  # no path was found
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


def heuristic(a: GridLocation, b: GridLocation) -> int:
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


@dataclass(frozen=True, order=True)
class State:
    position: tuple[int, int]
    direction: Direction
    momentum: int


class WeightedGrid:
    def __init__(self, width: int, height: int, weights: dict[GridLocation, int]):
        self.width = width
        self.height = height
        self.weights = weights

    def in_bounds(self, loc: GridLocation) -> bool:
        (x, y) = loc
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, current: State) -> list[State]:
        x, y = current.position
        if current.direction == Direction.RIGHT:
            neighbors = [
                State((x, y - 1), Direction.UP, 1),
                State((x, y + 1), Direction.DOWN, 1),
                State((x + 1, y), Direction.RIGHT, current.momentum + 1),
            ]
        elif current.direction == Direction.LEFT:
            neighbors = [
                State((x, y - 1), Direction.UP, 1),
                State((x, y + 1), Direction.DOWN, 1),
                State((x - 1, y), Direction.LEFT, current.momentum + 1),
            ]
        elif current.direction == Direction.UP:
            neighbors = [
                State((x + 1, y), Direction.RIGHT, 1),
                State((x - 1, y), Direction.LEFT, 1),
                State((x, y - 1), Direction.UP, current.momentum + 1),
            ]
        elif current.direction == Direction.DOWN:
            neighbors = [
                State((x + 1, y), Direction.RIGHT, 1),
                State((x - 1, y), Direction.LEFT, 1),
                State((x, y + 1), Direction.DOWN, current.momentum + 1),
            ]
        else:
            neighbors = [
                State((x + 1, y), Direction.RIGHT, 1),
                State((x, y + 1), Direction.DOWN, 1),
            ]
        neighbors = [
            neighbor for neighbor in neighbors if self.in_bounds(neighbor.position)
        ]
        neighbors = [neighbor for neighbor in neighbors if neighbor.momentum < 4]
        return neighbors

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> int:
        return self.weights.get(to_node, 1)


def a_star_search(grid: WeightedGrid, start: GridLocation, goal: GridLocation):
    frontier: queue.PriorityQueue[tuple[int, State]] = queue.PriorityQueue()
    frontier.put((0, State(start, Direction.NONE, 0)))
    came_from: dict[GridLocation, GridLocation] = {start: start}
    cost_so_far: dict[GridLocation, int] = {start: 0}
    while not frontier.empty():
        priority, current = frontier.get()
        if current == goal:
            break
        for next_neighbor in grid.neighbors(current):
            new_cost = cost_so_far[current.position] + grid.cost(
                current.position, next_neighbor.position
            )
            if (
                next_neighbor.position not in cost_so_far
                or new_cost < cost_so_far[next_neighbor.position]
            ):
                cost_so_far[next_neighbor.position] = new_cost
                priority = new_cost + heuristic(next_neighbor.position, goal)
                frontier.put((priority, next_neighbor))
                came_from[next_neighbor.position] = current.position
    draw_grid(grid, point_to=came_from, start=start, goal=goal)
    print()
    draw_grid(grid, path=reconstruct_path(came_from, start=start, goal=goal))
    print()
    draw_grid(grid, number=cost_so_far, start=start, goal=goal)
    return came_from, cost_so_far


class Solution(StrSplitSolution):
    _year = 2023
    _day = 17

    # @answer(1234)
    def part_1(self) -> int:
        width = len(self.input[0])
        height = len(self.input)
        weights = parse_grid(self.input)
        weighted_grid = WeightedGrid(width, height, weights)
        start, goal = (0, 0), (width - 1, height - 1)
        came_from, cost_so_far = a_star_search(weighted_grid, start, goal)
        return max(cost_so_far.values())

    # @answer(1234)
    def part_2(self) -> int:
        return 0
