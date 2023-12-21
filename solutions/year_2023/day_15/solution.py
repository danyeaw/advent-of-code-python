# puzzle prompt: https://adventofcode.com/2023/day/15

from ...base import TextSolution, answer


def get_hash(step: str) -> int:
    step_value = 0
    for char in step:
        step_value += ord(char)
        step_value *= 17
        step_value %= 256
    return step_value


class Solution(TextSolution):
    _year = 2023
    _day = 15

    @answer(511257)
    def part_1(self) -> int:
        steps = self.input.split(",")
        return sum(get_hash(step) for step in steps)

    # @answer(1234)
    def part_2(self) -> int:
        return 0
