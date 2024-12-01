# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from collections import Counter

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer((2086478, 24941624))
    def solve(self) -> tuple[int, int]:
        pairs = [map(int, line.split()) for line in self.input]
        first_ids, second_ids = [sorted(col) for col in zip(*pairs)]
        total_distance = sum(
            abs(first_ids[num] - second_ids[num]) for num in range(len(first_ids))
        )
        counter = Counter(second_ids)
        similarity_score = sum(first_id * counter[first_id] for first_id in first_ids)
        return total_distance, similarity_score
