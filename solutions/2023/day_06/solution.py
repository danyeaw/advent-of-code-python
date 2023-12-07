# puzzle prompt: https://adventofcode.com/2023/day/6
import math

from ...base import StrSplitSolution, answer


def get_num_winners(time: int, distance: int) -> int:
    return len([1 for button in range(time) if button * (time - button) > distance])


class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    @answer(219849)
    def part_1(self) -> int:
        races = zip(
            *[[int(value) for value in line.split()[1:]] for line in self.input]
        )
        winners = [get_num_winners(time, distance) for time, distance in races]
        return math.prod(winners)

    @answer(29432455)
    def part_2(self) -> int:
        time, distance = [int("".join(line.split()[1:])) for line in self.input]
        return get_num_winners(time, distance)
