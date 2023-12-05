# puzzle prompt: https://adventofcode.com/2023/day/4
from ...base import StrSplitSolution, answer


def parse(line: str) -> tuple[list[int], list[int]]:
    _, numbers = line.replace("  ", " ").split(": ")
    winners, my_numbers = numbers.split(" | ")
    winners = winners.split(" ")
    my_numbers = my_numbers.split(" ")
    winners = [int(num) for num in winners]
    my_numbers = [int(num) for num in my_numbers]
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
                total_worth.append(2 ** (len(intersect) - 1))
        return sum(total_worth)

    @answer(10212704)
    def part_2(self) -> int:
        scorecards = []
        scorecards.extend(len(self.input) * [1])
        for idx, line in enumerate(self.input):
            winners, my_numbers = parse(line)
            if intersect := set(winners).intersection(my_numbers):
                stop = min(idx + len(intersect), len(self.input)) + 1
                for _ in range(scorecards[idx]):
                    for next_cards in range(idx + 1, stop):
                        scorecards[next_cards] += 1
        return sum(scorecards)
