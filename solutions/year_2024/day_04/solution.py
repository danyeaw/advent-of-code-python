# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer


def rotate_string_rows(list_of_str: list[str]) -> list[str]:
    grid = [list(row) for row in list_of_str]
    rotated_grid = list(map(list, zip(*grid)))
    return ["".join(row) for row in rotated_grid]


def find_indexes(search_str: str, char: str):
    idx = -1
    while True:
        idx = search_str.find(char, idx + 1)
        if idx == -1:
            break
        else:
            yield idx


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        ROW_SIZE = len(self.input[0])

        total_horizontal_fwd = sum(row.count("XMAS") for row in self.input)
        total_horizontal_bwd = sum(row[::-1].count("XMAS") for row in self.input)
        vertical_strings = rotate_string_rows(self.input)
        total_vertical_fwd = sum(row.count("XMAS") for row in vertical_strings)
        total_vertical_bwd = sum(row[::-1].count("XMAS") for row in vertical_strings)
        x_indices, m_indices, a_indices, s_indices = [], [], [], []
        total_diagonal_fwd = 0
        for line in self.input:
            x_indices.append(find_indexes(line, "X"))
            m_indices.append(find_indexes(line, "M"))
            a_indices.append(find_indexes(line, "A"))
            s_indices.append(find_indexes(line, "S"))
        for x_row_idx, row in enumerate(x_indices):
            for idx in row:
                if (
                    x_row_idx + 3 < ROW_SIZE - 1
                    and idx + 1 in m_indices[x_row_idx + 1]
                    and idx + 2 in a_indices[x_row_idx + 2]
                    and idx + 3 in s_indices[x_row_idx + 3]
                ):
                    total_diagonal_fwd += 1
        return (
            total_horizontal_fwd
            + total_horizontal_bwd
            + total_vertical_fwd
            + total_vertical_bwd
            + total_diagonal_fwd
        )

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
