# puzzle prompt: https://adventofcode.com/2023/day/9

from ...base import StrSplitSolution, answer


def differences(pyramid_row: list[int]) -> list[int]:
    return [
        pyramid_row[idx + 1] - pyramid_row[idx] for idx in range(len(pyramid_row) - 1)
    ]


def total_extrapolated(input: list[str], reverse: bool) -> int:
    extrapolated = []
    for history_line in input:
        pyramid = [[int(value) for value in history_line.split()]]
        if reverse:
            pyramid[0] = list(reversed(pyramid[0]))
        pyramid[0].append(0)
        pyramid.extend(differences(pyramid[idx]) for idx in range(len(pyramid[0]) - 1))
        extrapolated.append(pyramid[-1][-1] * -1)
    return sum(extrapolated)


class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    @answer(1757008019)
    def part_1(self) -> int:
        return total_extrapolated(self.input, reverse=False)

    @answer(995)
    def part_2(self) -> int:
        return total_extrapolated(self.input, reverse=True)
