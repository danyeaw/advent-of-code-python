# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
# from graphlib import TopologicalSorter

# puzzle prompt: https://adventofcode.com/2024/day/5
from ...base import TextSolution, answer
from ...utils.parsing import parse_int_list


def adheres_to_rules(rule: list[int], update: list[int]) -> bool:
    left, right = rule
    if left in update and right in update:
        return update.index(left) < update.index(right)
    return True


class Solution(TextSolution):
    _year = 2024
    _day = 5

    @answer(7024)
    def part_1(self) -> int:
        input_rules, input_updates = self.input.split("\n\n")
        rules = [parse_int_list(rule.split("|")) for rule in input_rules.splitlines()]
        total = 0
        updates = [
            parse_int_list(raw_update.split(","))
            for raw_update in input_updates.splitlines()
        ]
        for update in updates:
            if all(adheres_to_rules(rule, update) for rule in rules):
                total += update[(len(update) - 1) // 2]
        return total

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
