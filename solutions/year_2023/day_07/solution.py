# puzzle prompt: https://adventofcode.com/2023/day/7

from collections import Counter

from ...base import StrSplitSolution, answer


def hand_type_to_value(hand: str, with_joker: bool = False) -> int:
    hand_values = sorted(Counter(hand).values())
    if with_joker:
        num_j = hand.count("J")
        print(num_j)
        if num_j and num_j < 5:
            hand_values.remove(num_j)
            hand_values[-1] += num_j

    match hand_values:
        case [5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case [1, 1, 1, 1, 1]:
            return 1
        case _:
            raise ValueError(f"Unknown hand: {hand}")


def get_card_values(hand: str, card_values: str) -> tuple[int, ...]:
    return tuple(card_values.index(card) for card in hand)


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    def _solve(self, with_joker: bool = False) -> int:
        card_values = "J23456789TJQKA" if with_joker else "23456789TJQKA"
        scored_hand = []
        for line in self.input:
            hand, bid = line.split()
            scored_hand.append(
                (
                    hand_type_to_value(hand, with_joker),
                    get_card_values(hand, card_values),
                    int(bid),
                )
            )
        return sum(
            (idx + 1) * bid for idx, (_, _, bid) in enumerate(sorted(scored_hand))
        )

    @answer(248105065)
    def part_1(self) -> int:
        return self._solve(with_joker=False)

    # @answer(1234)
    def part_2(self) -> int:
        return self._solve(with_joker=True)
