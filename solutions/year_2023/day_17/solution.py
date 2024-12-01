# puzzle prompt: https://adventofcode.com/2023/day/17
import queue
from dataclasses import dataclass
from enum import IntEnum

from ...base import StrSplitSolution, answer

Location = tuple[int, int]


class Direction(IntEnum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def parse_grid(raw_grid: list[list[str]]) -> dict[Location, int]:
    result: dict[Location, int] = {}
    for y, line in enumerate(raw_grid):
        for x, char in enumerate(line):
            result[(x, y)] = int(char)
    return result


@dataclass(frozen=True, order=True)
class State:
    position: tuple[int, int]
    direction: Direction
    momentum: int


class Grid:
    def __init__(
        self,
        width: int,
        height: int,
        weights: dict[Location, int],
        min_momentum: int,
        max_momentum: int,
    ):
        self.width = width
        self.height = height
        self.weights = weights
        self.min_momentum = min_momentum
        self.max_momentum = max_momentum

    def in_bounds(self, loc: Location) -> bool:
        (x, y) = loc
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, current: State) -> list[State]:
        x, y = current.position
        if current.momentum < self.min_momentum:
            if current.direction == Direction.RIGHT:
                neighbors = [State((x + 1, y), Direction.RIGHT, current.momentum + 1)]
            elif current.direction == Direction.LEFT:
                neighbors = [State((x - 1, y), Direction.LEFT, current.momentum + 1)]
            elif current.direction == Direction.UP:
                neighbors = [State((x, y - 1), Direction.UP, current.momentum + 1)]
            elif current.direction == Direction.DOWN:
                neighbors = [State((x, y + 1), Direction.DOWN, current.momentum + 1)]
            else:
                neighbors = [
                    State((x + 1, y), Direction.RIGHT, 1),
                    State((x, y + 1), Direction.DOWN, 1),
                ]
        elif current.direction == Direction.RIGHT:
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
        return [
            neighbor for neighbor in neighbors if neighbor.momentum < self.max_momentum
        ]

    def cost(self, to_node: Location) -> int:
        return self.weights.get(to_node, 1)


def a_star_search(
    grid: Grid,
    start: Location,
    goal: Location,
    momentum_min: int,
) -> tuple[dict[State, State], dict[State, int]]:
    frontier: queue.PriorityQueue[tuple[int, State]] = queue.PriorityQueue()
    start_state = State(start, Direction.NONE, 0)
    frontier.put((0, start_state))
    came_from: dict[State, State] = {start_state: start_state}
    cost_so_far: dict[State, int] = {State(start, Direction.NONE, 0): 0}
    while not frontier.empty():
        priority, current = frontier.get()
        if current.position == goal and current.momentum >= momentum_min:
            break
        for next_neighbor in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(next_neighbor.position)
            if (
                next_neighbor not in cost_so_far
                or new_cost < cost_so_far[next_neighbor]
            ):
                cost_so_far[next_neighbor] = new_cost
                priority = new_cost
                frontier.put((priority, next_neighbor))
                came_from[next_neighbor] = current
    return came_from, cost_so_far


def solve(
    weights: dict[Location, int],
    width: int,
    height: int,
    momentum_min: int,
    momentum_max: int,
) -> int:
    weighted_grid = Grid(width, height, weights, momentum_min, momentum_max)
    start, goal = (0, 0), (width - 1, height - 1)
    came_from, cost_so_far = a_star_search(weighted_grid, start, goal, momentum_min)
    return min(
        cost
        for state, cost in cost_so_far.items()
        if state.position == goal and state.momentum >= momentum_min
    )


class Solution(StrSplitSolution):
    _year = 2023
    _day = 17

    @answer(859)
    def part_1(self) -> int:
        return solve(parse_grid(self.input), len(self.input[0]), len(self.input), 0, 4)

    @answer(1027)
    def part_2(self) -> int:
        return solve(parse_grid(self.input), len(self.input[0]), len(self.input), 4, 11)
