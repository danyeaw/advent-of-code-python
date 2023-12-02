from string import digits

from ...base import StrSplitSolution, answer


def find_calibration_value(line: str) -> int:
    first = None
    last = None
    for char in line:
        if char in digits:
            if first is None:
                first = char
            last = char
    return int(f"{first}{last}")


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(55447)
    def part_1(self) -> int:
        return sum(find_calibration_value(line) for line in self.input)
