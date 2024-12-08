# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
# puzzle prompt: https://adventofcode.com/2024/day/5
from graphlib import TopologicalSorter

from ...base import TextSolution, answer
from ...utils.parsing import parse_int_list


def adheres_to_rules(rule: list[int], update: list[int]) -> bool:
    left, right = rule
    if left in update and right in update:
        return update.index(left) < update.index(right)
    return True


def middle_element(array: list[int]) -> int:
    return array[len(array) // 2]


class Solution(TextSolution):
    _year = 2024
    _day = 5

    @answer((7024, 4151))
    def solve(self) -> tuple[int, int]:
        input_rules, input_updates = self.input.split("\n\n")
        rules = [parse_int_list(rule.split("|")) for rule in input_rules.splitlines()]
        part1, part2 = 0, 0
        updates = [
            parse_int_list(raw_update.split(","))
            for raw_update in input_updates.splitlines()
        ]
        for update in updates:
            if all(adheres_to_rules(rule, update) for rule in rules):
                part1 += middle_element(update)
            else:
                topo_sorter: TopologicalSorter = TopologicalSorter()
                for left, right in rules:
                    if left in update and right in update:
                        topo_sorter.add(left, right)
                fixed_update = list(topo_sorter.static_order())
                part2 += middle_element(fixed_update)

        return part1, part2
