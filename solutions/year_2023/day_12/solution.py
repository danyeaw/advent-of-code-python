# puzzle prompt: https://adventofcode.com/2023/day/12
import functools
import itertools
import re

from ...base import StrSplitSolution, answer


@functools.cache
def valid_arrangement(record: str, pattern: str) -> bool:
    group_sizes = [int(value) for value in pattern.split(",")]
    actual_groups = re.findall(r"#+", record)
    actual_group_sizes = [len(group) for group in actual_groups]
    return actual_group_sizes == group_sizes


@functools.cache
def number_of_arrangements(record: str, groups: tuple[int]) -> int:
    if not groups:
        no_broken_strings_remaining = "#" not in record
        return 1 if no_broken_strings_remaining else 0
    group_min_start = 0
    group_max_start = len(record) - sum(groups) - len(groups) + 1
    if "#" in record:
        group_max_start = min(group_max_start, record.index("#"))
    remaining_groups: list[int]
    first_group_size, *remaining_groups = groups
    num_arrangements = 0
    for group_start in range(group_min_start, group_max_start + 1):
        group_end = group_start + first_group_size
        group = record[group_start:group_end]

        is_group_possible = all(char in "#?" for char in group)
        is_end_of_record = group_end >= len(record)
        is_group_separated = is_end_of_record or record[group_end] in ".?"
        if not is_group_possible or not is_group_separated:
            continue
        remaining_record_after_sep = record[group_end + 1 :]
        num_arrangements += number_of_arrangements(
            remaining_record_after_sep, tuple(remaining_groups)
        )
    return num_arrangements


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
                if valid_arrangement("".join(record_characters), pattern_str):
                    total_arrangements += 1
        return total_arrangements

    @answer(2128386729962)
    def part_2(self) -> int:
        total_arrangements = 0
        for line in self.input:
            record, pattern_str = line.split()
            record = f"{record}?" * 4 + record
            pattern_str = f"{pattern_str}," * 4 + pattern_str
            group_sizes = [int(value) for value in pattern_str.split(",")]
            record = re.sub(r"\.+", ".", record)
            record = re.sub(r"^\.|\.$", r"", record)
            total_arrangements += number_of_arrangements(record, tuple(group_sizes))

        return total_arrangements
