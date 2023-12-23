# puzzle prompt: https://adventofcode.com/2023/day/16
from collections import deque
from dataclasses import dataclass
from enum import Enum

from ...base import StrSplitSolution, answer


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def add_points(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


@dataclass(frozen=True)
class State:
    direction: Direction
    position: tuple[int, int]

    def next_states(self, char: str) -> list["State"]:
        match char:
            case ".":
                return [self.step()]
            case "-" if self.direction in (Direction.LEFT, Direction.RIGHT):
                return [self.step()]
            case "|" if self.direction in (Direction.UP, Direction.DOWN):
                return [self.step()]
            case "\\" if self.direction == Direction.UP:
                direction = Direction.LEFT
                return [State(direction, self.next_position_by_direction(direction))]
            case "\\" if self.direction == Direction.DOWN:
                direction = Direction.RIGHT
                return [State(direction, self.next_position_by_direction(direction))]
            case "\\" if self.direction == Direction.LEFT:
                direction = Direction.UP
                return [State(direction, self.next_position_by_direction(direction))]
            case "\\" if self.direction == Direction.RIGHT:
                direction = Direction.DOWN
                return [State(direction, self.next_position_by_direction(direction))]
            case "/" if self.direction == Direction.UP:
                direction = Direction.RIGHT
                return [State(direction, self.next_position_by_direction(direction))]
            case "/" if self.direction == Direction.DOWN:
                direction = Direction.LEFT
                return [State(direction, self.next_position_by_direction(direction))]
            case "/" if self.direction == Direction.LEFT:
                direction = Direction.DOWN
                return [State(direction, self.next_position_by_direction(direction))]
            case "/" if self.direction == Direction.RIGHT:
                direction = Direction.UP
                return [State(direction, self.next_position_by_direction(direction))]
            case "-" if self.direction in (Direction.UP, Direction.DOWN):
                return [
                    State(
                        Direction.LEFT, self.next_position_by_direction(Direction.LEFT)
                    ),
                    State(
                        Direction.RIGHT,
                        self.next_position_by_direction(Direction.RIGHT),
                    ),
                ]
            case "|" if self.direction in (Direction.LEFT, Direction.RIGHT):
                return [
                    State(Direction.UP, self.next_position_by_direction(Direction.UP)),
                    State(
                        Direction.DOWN, self.next_position_by_direction(Direction.DOWN)
                    ),
                ]
            case _:
                raise ValueError("Invalid character")

    @property
    def next_position(self) -> tuple[int, int]:
        return self.next_position_by_direction(self.direction)

    def next_position_by_direction(self, direction: Direction) -> tuple[int, int]:
        direction_to_offset = {
            Direction.UP: (0, -1),
            Direction.DOWN: (0, 1),
            Direction.RIGHT: (1, 0),
            Direction.LEFT: (-1, 0),
        }
        return add_points(self.position, direction_to_offset[direction])

    def step(self) -> "State":
        return State(self.direction, self.next_position)


def parse_grid(raw_grid: list[list[str]]) -> dict[tuple[int, int], str]:
    result: dict[tuple[int, int], str] = {}
    for row, line in enumerate(raw_grid):
        for col, char in enumerate(line):
            result[(col, row)] = char
    return result


class Solution(StrSplitSolution):
    _year = 2023
    _day = 16

    @answer(7046)
    def part_1(self) -> int:
        grid = parse_grid(self.input)
        seen_states: set[State] = set()
        queue: deque[State] = deque([State(Direction.RIGHT, (0, 0))])
        while queue:
            current = queue.pop()
            if current in seen_states:
                continue
            seen_states.add(current)
            for next_state in current.next_states(grid[current.position]):
                if next_state.position in grid:
                    queue.append(next_state)
        return len({seen_state.position for seen_state in seen_states})

    @answer(7313)
    def part_2(self) -> int:
        grid = parse_grid(self.input)
        max_x = len(self.input[0]) - 1
        max_y = len(self.input) - 1
        largest_tiles = 0
        for position in grid.keys():
            queue: deque[State] = deque()
            if position[0] == 0:
                queue.append(State(Direction.RIGHT, position))
            elif position[0] == max_x:
                queue.append(State(Direction.LEFT, position))
            elif position[1] == 0:
                queue.append(State(Direction.DOWN, position))
            elif position[1] == max_y:
                queue.append(State(Direction.UP, position))
            if not queue:
                continue
            seen_states: set[State] = set()
            while queue:
                current = queue.pop()
                if current in seen_states:
                    continue
                seen_states.add(current)
                for next_state in current.next_states(grid[current.position]):
                    if next_state.position in grid:
                        queue.append(next_state)
            max_for_position = len({seen_state.position for seen_state in seen_states})
            largest_tiles = max(largest_tiles, max_for_position)
        return largest_tiles
