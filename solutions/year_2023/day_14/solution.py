# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution, answer

NUM_CYCLES = 1_000_000


def parse_grid(
    raw_grid: list[list[str]], ignore_chars: str
) -> dict[tuple[int, int], str]:
    result = {}
    for row, line in enumerate(raw_grid):
        for col, c in enumerate(line):
            if c not in ignore_chars:
                result[row, col] = c
    return result


def tilt(rock_map: list[list[str]], direction: str):
    changed = True
    while changed:
        changed = False
        for row_num, row in enumerate(rock_map):
            if "O" not in row:
                continue
            for col_num, char in enumerate(row):
                if char == "O":
                    if direction == "east":
                        if col_num > len(row) - 2:
                            continue
                        elif rock_map[row_num][col_num + 1] == ".":
                            rock_map[row_num][col_num + 1] = "O"
                            rock_map[row_num][col_num] = "."
                            changed = True
                    elif direction == "north":
                        if row_num == 0:
                            continue
                        elif rock_map[row_num - 1][col_num] == ".":
                            rock_map[row_num - 1][col_num] = "O"
                            rock_map[row_num][col_num] = "."
                            changed = True
                    elif direction == "south":
                        if row_num > len(rock_map) - 2:
                            continue
                        elif rock_map[row_num + 1][col_num] == ".":
                            rock_map[row_num + 1][col_num] = "O"
                            rock_map[row_num][col_num] = "."
                            changed = True
                    elif direction == "west":
                        if col_num == 0:
                            continue
                        elif rock_map[row_num][col_num - 1] == ".":
                            rock_map[row_num][col_num - 1] = "O"
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
            if state in states:
                distance_to_goal = NUM_CYCLES - cycle
                loop_length = cycle - states[state]
                cycle = NUM_CYCLES - distance_to_goal % loop_length
            states[state] = cycle
            cycle += 1
        return sum(
            distance * row.count("O")
            for distance, row in enumerate(reversed(list(rock_map)), start=1)
        )
