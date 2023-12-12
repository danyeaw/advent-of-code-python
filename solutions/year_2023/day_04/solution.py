# puzzle prompt: https://adventofcode.com/2023/day/4
from ...base import StrSplitSolution, answer


def parse(line: str) -> tuple[list[int], list[int]]:
    _, numbers = line.replace("  ", " ").split(": ")
    first, second = numbers.split(" | ")
    first_list, second_list = first.split(), second.split()
    winners = [int(num) for num in first_list]
    my_numbers = [int(num) for num in second_list]
    return winners, my_numbers


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(28750)
    def part_1(self) -> int:
        total_worth = []
        for line in self.input:
            winners, my_numbers = parse(line)
            if intersect := set(winners).intersection(my_numbers):
                num_winners = len(intersect)
                total_worth.append(2 ** (num_winners - 1))
        return sum(total_worth)

    @answer(10212704)
    def part_2(self) -> int:
        scorecards = []
        scorecards.extend(len(self.input) * [1])
        for card_id, line in enumerate(self.input):
            winners, my_numbers = parse(line)
            if intersect := set(winners).intersection(my_numbers):
                num_winners = len(intersect)
                for next_card_id in range(card_id + 1, card_id + 1 + num_winners):
                    scorecards[next_card_id] += scorecards[card_id]
        return sum(scorecards)
