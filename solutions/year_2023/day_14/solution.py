# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution, answer

NUM_CYCLES = 1_000_000


def parse_grid(raw_grid: list[list[str]], ignore_chars: str) -> set[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for row, line in enumerate(raw_grid):
        result.extend((row, col) for col, c in enumerate(line) if c not in ignore_chars)
    return set(result)


def tilt(rock_map: list[list[str]], direction: str):
    changed = True
    offset = {
        "east": (0, 1),
        "north": (-1, 0),
        "south": (1, 0),
        "west": (0, -1),
    }
    while changed:
        changed = False
        for row_num, row in enumerate(rock_map):
            if "O" not in row:
                continue
            for col_num, char in enumerate(row):
                if char == "O":
                    if (
                        (direction == "east" and col_num > len(row) - 2)
                        or (
                            direction != "east"
                            and direction == "north"
                            and row_num == 0
                        )
                        or (
                            direction not in ("east", "north")
                            and direction == "south"
                            and row_num > len(rock_map) - 2
                        )
                        or (
                            direction not in ("east", "north", "south")
                            and direction == "west"
                            and col_num == 0
                        )
                    ):
                        continue
                    row_offset, col_offset = offset[direction]
                    if rock_map[row_num + row_offset][col_num + col_offset] == ".":
                        rock_map[row_num + row_offset][col_num + col_offset] = "O"
                        rock_map[row_num][col_num] = "."
                        changed = True
    return rock_map


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14

    @answer(106648)
    def part_1(self) -> int:
        rock_map = [list(row) for row in self.input]
        rock_map = tilt(rock_map, "north")
        return sum(
            distance * row.count("O")
            for distance, row in enumerate(reversed(list(rock_map)), start=1)
        )

    @answer(87700)
    def part_2(self) -> int:
        rock_map = [list(row) for row in self.input]
        cycle_pattern = ("north", "west", "south", "east")
        states: dict[frozenset[tuple[int, int]], int] = {}
        cycle = 0
        while cycle < NUM_CYCLES:
            for direction in cycle_pattern:
                rock_map = tilt(rock_map, direction)
            state = frozenset(parse_grid(rock_map, ignore_chars=".#"))
            if state in states and cycle < 500:
                loop_length = cycle - states[state]
                distance_to_goal = NUM_CYCLES - cycle
                cycle = NUM_CYCLES - distance_to_goal % loop_length
                print(f"{NUM_CYCLES} - {distance_to_goal % loop_length} = {cycle}")
            states[state] = cycle
            cycle += 1
        return sum(
            distance * row.count("O")
            for distance, row in enumerate(reversed(list(rock_map)), start=1)
        )
