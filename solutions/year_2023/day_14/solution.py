# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution, answer


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
                        if col_num < len(row):
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
                        if row_num < len(rock_map):
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
        for row in rock_map:
            print(row)
        return sum(
            distance * row.count("O")
            for distance, row in enumerate(reversed(list(rock_map)), start=1)
        )

    # @answer(1234)
    def part_2(self) -> int:
        rock_map = [list(row) for row in self.input]
        cycle_pattern = ("north", "west", "south", "east")
        cycles = 0
        cycles_to_run = 1_000_000
        while cycles < cycles_to_run + 1:
            for direction in cycle_pattern:
                rock_map = tilt(rock_map, direction)
                cycles += 1
        return sum(
            distance * row.count("O")
            for distance, row in enumerate(reversed(list(rock_map)), start=1)
        )
