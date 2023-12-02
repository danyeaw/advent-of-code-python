from __future__ import annotations

from enum import Enum

from ...base import StrSplitSolution, answer


class Colors(Enum):
    red = 0
    green = 1
    blue = 2


class MaxColors(Enum):
    red = 12
    green = 13
    blue = 14


def parse(line: str) -> tuple[int, list[str]]:
    game_num: int = int(line.split(":")[0].split(" ")[1])
    game_record: list[str] = line.split(": ")[1].split("; ")
    return game_num, game_record


def game_possible(game_record: list[str]) -> bool:
    for subset in game_record:
        subset_colors: list[str] = subset.split(", ")
        for color in Colors:
            for num_by_color in subset_colors:
                if color.name in num_by_color:
                    block_count = int(num_by_color.split(" ")[0])
                    if block_count > MaxColors[color.name].value:
                        return False
    return True


def get_min_blocks_by_color(game_record: list[str]) -> list[int]:
    min_blocks = [0, 0, 0]
    for subset in game_record:
        subset_colors: list[str] = subset.split(", ")
        for color in Colors:
            for num_by_color in subset_colors:
                if color.name in num_by_color:
                    block_count = int(num_by_color.split(" ")[0])
                    color_index = Colors[color.name].value
                    min_blocks[color_index] = max(block_count, min_blocks[color_index])
    return min_blocks


def power_of_numbers(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2528)
    def part_1(self) -> int:
        valid_sum = 0
        for line in self.input:
            game_num, game_record = parse(line)
            if game_possible(game_record):
                valid_sum += game_num
        return valid_sum

    @answer(67363)
    def part_2(self) -> int:
        result = 0
        for line in self.input:
            game_num, game_record = parse(line)
            min_blocks_by_color = get_min_blocks_by_color(game_record)
            result += power_of_numbers(min_blocks_by_color)
        return result
