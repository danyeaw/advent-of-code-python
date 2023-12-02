from ...base import StrSplitSolution, answer


def find_calibration_value(line: str) -> int:
    digits = [digit for digit in line if digit.isdigit()]
    return int(f"{digits[0]}{digits[-1]}")


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(55447)
    def part_1(self) -> int:
        return sum(find_calibration_value(line) for line in self.input)
