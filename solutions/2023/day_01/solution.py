from ...base import StrSplitSolution, answer

str_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_calibration_value(line: str) -> int:
    digits = [digit for digit in line if digit.isdigit()]
    return int(f"{digits[0]}{digits[-1]}") if digits else 0


def replace_words(line: str) -> str:
    for word, digit in str_to_digit.items():
        # Don't remove the first and last letters since words can overlap
        line = line.replace(word, f"{word[0]}{digit}{word[-1]}")
    return line


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(55447)
    def part_1(self) -> int:
        return sum(find_calibration_value(line) for line in self.input)

    @answer(54706)
    def part_2(self) -> int:
        return sum(find_calibration_value(replace_words(line)) for line in self.input)
