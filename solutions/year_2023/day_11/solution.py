# puzzle prompt: https://adventofcode.com/2023/day/11
from ...base import StrSplitSolution, answer


def find_total(galaxies):
    total = 0
    for idx, galaxy in enumerate(galaxies):
        for next_point in galaxies[(idx + 1) :]:
            distance = abs(next_point[1] - galaxy[1]) + abs(next_point[0] - galaxy[0])
            total += distance
    return total


def find_expanded_galaxies(
    split_input: list[str], expansion_num: int
) -> list[list[int]]:
    image = [list(line) for line in split_input]
    galaxies: list[list[int]] = []
    y_expansion = [row_num for row_num, row in enumerate(image) if "#" not in row]
    x_expansion = [
        col_num
        for col_num, col in enumerate(list(rows) for rows in zip(*image))
        if "#" not in col
    ]
    for y, line in enumerate(split_input):
        galaxies.extend([x, y] for x, char in enumerate(line) if char == "#")
    expansion = 0
    for y in y_expansion:
        for galaxy in galaxies:
            if galaxy[1] > (y + expansion):
                galaxy[1] += expansion_num - 1
        expansion += expansion_num - 1
    expansion = 0
    for x in x_expansion:
        for galaxy in galaxies:
            if galaxy[0] > (x + expansion):
                galaxy[0] += expansion_num - 1
        expansion += expansion_num - 1
    return galaxies


class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    @answer(9418609)
    def part_1(self) -> int:
        galaxies = find_expanded_galaxies(self.input, 2)
        return find_total(galaxies)

    @answer(593821230983)
    def part_2(self) -> int:
        galaxies = find_expanded_galaxies(self.input, 1000000)
        return find_total(galaxies)
