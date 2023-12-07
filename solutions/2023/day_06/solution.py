# puzzle prompt: https://adventofcode.com/2023/day/6
import math
import re

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 6

    @answer(219849)
    def part_1(self) -> int:
        lines = self.input.split("\n")
        times = re.sub(r"\W+", " ", lines[0][4:])[1:].split()
        times = [int(time) for time in times]
        distances = re.sub(r"\W+", " ", lines[1][8:])[1:].split()
        distances = [int(distance) for distance in distances]

        winners = []
        for race, time in enumerate(times):
            race_winners = [
                button
                for button in range(time)
                if button * (time - button) > distances[race]
            ]
            winners.append(len(race_winners))
        return math.prod(winners)

    @answer(71503)
    def part_2(self) -> int:
        lines = self.input.split("\n")
        time = int(re.sub(r"\W+", "", lines[0][4:]))
        distance = int(re.sub(r"\W+", "", lines[1][8:]))
        winners = [
            button for button in range(time) if button * (time - button) > distance
        ]
        return len(winners)
