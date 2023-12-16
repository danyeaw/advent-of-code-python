# puzzle prompt: https://adventofcode.com/2023/day/12
import itertools
import re

from ...base import StrSplitSolution, answer


def valid_arrangement(record: str, group_sizes: list[int]) -> bool:
    actual_groups = re.findall(r"#+", record)
    actual_group_sizes = [len(group) for group in actual_groups]
    return actual_group_sizes == group_sizes


class Solution(StrSplitSolution):
    _year = 2023
    _day = 12

    @answer(7251)
    def part_1(self) -> int:
        total_arrangements = 0
        for line in self.input:
            record, pattern_str = line.split()
            group_sizes = [int(value) for value in pattern_str.split(",")]
            record = re.sub(r"\.+", ".", record)
            record = re.sub(r"^\.|\.$", r"", record)
            total_springs = sum(group_sizes)
            broken_springs = record.count("#")
            unassigned_springs = total_springs - broken_springs
            unassigned_positions = [
                idx for idx, char in enumerate(record) if char == "?"
            ]

            for assignment in itertools.combinations(
                unassigned_positions, unassigned_springs
            ):
                record_characters = list(record)
                for position in assignment:
                    record_characters[position] = "#"
                if valid_arrangement("".join(record_characters), group_sizes):
                    total_arrangements += 1
        return total_arrangements

    # @answer(1234)
    def part_2(self) -> int:
        return 0
