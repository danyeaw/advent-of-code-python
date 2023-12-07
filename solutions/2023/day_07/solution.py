# puzzle prompt: https://adventofcode.com/2023/day/7

from ...base import answer, StrSplitSolution

from collections import Counter


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        hands = [[Counter(line.split()[0]), line.split()[0], int(line.split()[1])] for line in self.input]
        hand_types = {
            "five_of_a_kind": [],
            "four_of_a_kind": [],
            "full_house": [],
            "three_of_a_kind": [],
            "two_pair": [],
            "one_pair": [],
            "high_card": [],
        }
        for hand in hands:
            card_count = hand[0].values()
            if 5 in card_count:
                hand_types["five_of_a_kind"].append(hand)
            elif 4 in card_count:
                hand_types["four_of_a_kind"].append(hand)
            elif 3 in card_count and 2 in card_count:
                hand_types["full_house"].append(hand)
            elif 3 in card_count:
                hand_types["three_of_a_kind"].append(hand)
            elif len(card_count) == 3:
                hand_types["two_pair"].append(hand)
            elif 2 in card_count:
                hand_types["one_pair"].append(hand)
            else:
                hand_types["high_card"].append(hand)
        print(hand_types.values())
        for values in hand_types.values():
            for value in values:
                if value:
                    print(value)
                    print(sorted(value))


    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
