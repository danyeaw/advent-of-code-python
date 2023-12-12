# puzzle prompt: https://adventofcode.com/2023/day/11
from ...base import StrSplitSolution, answer


def find_total(galaxies):
    total = 0
    for idx, galaxy in enumerate(galaxies):
        print(galaxies[(idx + 1) :])
        for next_point in galaxies[(idx + 1) :]:
            distance = abs(next_point[1] - galaxy[1]) + abs(next_point[0] - galaxy[0])
            total += distance
    return total


def find_expanded_galaxies(
    split_input: list[str], expansion_num: int
) -> list[list[int]]:
    image = [[char for char in line] for line in split_input]
    galaxies: list[list[int]] = []
    y_expansion = []
    x_expansion = []
    for row_num, row in enumerate(image):
        if "#" not in row:
            y_expansion.append(row_num)
    for col_num, col in enumerate(list(rows) for rows in zip(*image)):
        if "#" not in col:
            x_expansion.append(col_num)
    for y, line in enumerate(split_input):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append([x, y])
    print(galaxies)
    expansion = 0
    for y in y_expansion:
        for galaxy in galaxies:
            if galaxy[1] > (y + expansion):
                galaxy[1] += expansion_num
        expansion += expansion_num
    expansion = 0
    for x in x_expansion:
        for galaxy in galaxies:
            if galaxy[0] > (x + expansion):
                galaxy[0] += expansion_num
        expansion += expansion_num
    return galaxies


class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    @answer(9418609)
    def part_1(self) -> int:
        galaxies = find_expanded_galaxies(self.input, 1)
        return find_total(galaxies)

    # @answer(1234)
    def part_2(self) -> int:
        galaxies = find_expanded_galaxies(self.input, 100)
        print(galaxies)
        return find_total(galaxies)
