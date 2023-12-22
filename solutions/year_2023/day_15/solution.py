# puzzle prompt: https://adventofcode.com/2023/day/15
from collections import defaultdict

from ...base import StrSplitSolution, answer


def get_hash(step: str) -> int:
    step_value = 0
    for char in step:
        step_value += ord(char)
        step_value *= 17
        step_value %= 256
    return step_value


class Solution(StrSplitSolution):
    separator = ","
    _year = 2023
    _day = 15

    @answer(511257)
    def part_1(self) -> int:
        return sum(get_hash(step) for step in self.input)

    @answer(239484)
    def part_2(self) -> int:
        boxes: dict[int, dict[str, int]] = defaultdict(dict)
        for step in self.input:
            if "=" in step:
                label, focal = step.split("=")
                boxes[get_hash(label)][label] = int(focal)
            else:
                label = step[:-1]
                boxes[get_hash(label)].pop(label, None)
        return sum(
            sum(
                (box_num + 1) * slot_num * focal_length
                for slot_num, focal_length in enumerate(lenses.values(), start=1)
            )
            for box_num, lenses in sorted(boxes.items())
        )
