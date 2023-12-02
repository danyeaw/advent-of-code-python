from __future__ import annotations

import re
from collections import defaultdict

from ...base import StrSplitSolution, answer


def power_of_numbers(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result


def get_count_color(game_record: str) -> list[tuple[str, str]]:
    return re.findall(r"(\d+) (\w+)", game_record)


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2528)
    def part_1(self) -> int:
        valid_sum = 0
        for game_num, line in enumerate(self.input, start=1):
            _, game_record = line.split(": ")
            if all(
                    int(count) <= {"red": 12, "green": 13, "blue": 14}[color]
                    for count, color in get_count_color(game_record)
            ):
                valid_sum += int(game_num)
        return valid_sum

    @answer(67363)
    def part_2(self) -> int:
        result = 0
        for game_num, line in enumerate(self.input, start=1):
            _, game_record = line.split(": ")
            min_per_color: dict[str, int] = defaultdict(int)

            for count, color in get_count_color(game_record):
                min_per_color[color] = max(min_per_color[color], int(count))
            result += power_of_numbers(list(min_per_color.values()))

        return result
