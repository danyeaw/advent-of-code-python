# puzzle prompt: https://adventofcode.com/2023/day/9

from ...base import answer, StrSplitSolution


def differences(pyramid_row: list[int]) -> list[int]:
    return [
        pyramid_row[idx + 1] - pyramid_row[idx]
        for idx in range(len(pyramid_row) - 1)
    ]


class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    # @answer(1234)
    def part_1(self) -> int:
        extrapolated = []
        for line in self.input:
            pyramid = [[int(value) for value in line.split()]]
            # pyramid[0].append(0)
            row_num = 0
            while True:
                pyramid.append(differences(pyramid[row_num]))
                if sum(pyramid[row_num + 1]) == 0:
                    break
                row_num += 1
            print(pyramid)
            pyramid = list(reversed(pyramid))
            for idx in range(len(pyramid)):
                if idx == 0:
                    pyramid[idx].append(0)
                else:
                    pyramid[idx].append(pyramid[idx - 1][-1] + pyramid[idx][-1])
            extrapolated.append(pyramid[-1][-1])
            print(pyramid)
        print(extrapolated)
        return sum(extrapolated)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
