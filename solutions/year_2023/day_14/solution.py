# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14

    # @answer(1234)
    def part_1(self) -> int:
        map = [list(line) for line in self.input]
        for line in map:
            print(line)
        print()
        map_by_cols = list(zip(*map))
        north_tilted = []
        for col in map_by_cols:
            if "#" not in col:
                rounded = col.count("O")
                empty = len(col) - rounded
                north_tilted.append(
                    [c for c in rounded * "O"] + [c for c in empty * "."]
                )
            else:
                pass
            print(col)
        print(north_tilted)
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        return 0
