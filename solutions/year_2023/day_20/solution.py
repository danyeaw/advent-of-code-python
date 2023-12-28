# puzzle prompt: https://adventofcode.com/2023/day/20
from collections import Counter, deque

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 20

    @answer(825896364)
    def part_1(self) -> int:
        lines = [line.split(" -> ") for line in self.input]
        conjunctions = [line[0][1:] for line in lines if line[0][0] == "&"]
        flip_flops = [line[0][1:] for line in lines if line[0][0] == "%"]
        flip_flops_on = set()
        src_to_dest = {
            src.replace("&", "").replace("%", ""): set(destinations.split(", "))
            for src, destinations in lines
        }
        conjunctions_to_inputs: dict[str, dict[str, str]] = {}
        for src, destinations in src_to_dest.items():
            for dest in destinations:
                if dest in conjunctions:
                    if dest not in conjunctions_to_inputs.keys():
                        conjunctions_to_inputs[dest] = {}
                    conjunctions_to_inputs[dest][src] = "lo"
        queue: deque[tuple[str, str, str]] = deque()
        count: Counter[str] = Counter(lo=0, hi=0)
        for _ in range(1000):
            queue.append(("broadcaster", "button", "lo"))
            while queue:
                dest, src, signal = queue.popleft()
                if dest in flip_flops and signal == "lo":
                    if dest in flip_flops_on:
                        flip_flops_on.discard(dest)
                        new_signal = "lo"
                    else:
                        flip_flops_on.add(dest)
                        new_signal = "hi"
                    for new_dest in src_to_dest[dest]:
                        queue.append((new_dest, dest, new_signal))
                elif dest in conjunctions:
                    conjunctions_to_inputs[dest][src] = signal
                    new_signal = (
                        "lo"
                        if all(
                            input_signal == "hi"
                            for input_signal in conjunctions_to_inputs[dest].values()
                        )
                        else "hi"
                    )
                    for new_dest in src_to_dest[dest]:
                        queue.append((new_dest, dest, new_signal))
                elif dest == "broadcaster":
                    for new_dest in src_to_dest[dest]:
                        queue.append((new_dest, dest, signal))
                count[signal] += 1
        return count["lo"] * count["hi"]

    # @answer(1234)
    def part_2(self) -> int:
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
