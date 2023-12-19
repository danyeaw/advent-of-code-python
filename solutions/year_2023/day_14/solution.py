# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14

    @answer(106648)
    def part_1(self) -> int:
        rock_map = [list(row) for row in self.input]
        changed = True
        while changed:
            changed = False
            for row_num, row in enumerate(rock_map):
                if row_num == 0:
                    continue
                for col_num, char in enumerate(row):
                    if char == "O" and rock_map[row_num - 1][col_num] == ".":
                        rock_map[row_num - 1][col_num] = "O"
                        rock_map[row_num][col_num] = "."
                        changed = True
        return sum(
            distance * row.count("O")
            for distance, row in enumerate(reversed(list(rock_map)), start=1)
        )

    # @answer(1234)
    def part_2(self) -> int:
        return 0
