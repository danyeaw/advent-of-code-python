# puzzle prompt: https://adventofcode.com/2023/day/20
import math
from collections import Counter, deque

from ...base import StrSplitSolution, answer


def execute_button_press_part1(
    src_to_dest: dict[str, set[str]],
    conjunctions_to_inputs: dict[str, dict[str, str]],
    conjunctions: list[str],
    flip_flops: list[str],
    flip_flops_on: set[str],
):
    queue: deque[tuple[str, str, str]] = deque()
    queue.append(("broadcaster", "button", "lo"))
    count: Counter[str] = Counter()
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
    return count


class Solution(StrSplitSolution):
    _year = 2023
    _day = 20

    @answer(825896364)
    def part_1(self) -> int:
        lines = [line.split(" -> ") for line in self.input]
        conjunctions = [line[0][1:] for line in lines if line[0][0] == "&"]
        flip_flops = [line[0][1:] for line in lines if line[0][0] == "%"]
        flip_flops_on: set[str] = set()
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
        count: Counter[str] = Counter(lo=0, hi=0)
        for _ in range(1000):
            count += execute_button_press_part1(
                src_to_dest,
                conjunctions_to_inputs,
                conjunctions,
                flip_flops,
                flip_flops_on,
            )
        return count["lo"] * count["hi"]

    @answer(243566897206981)
    def part_2(self) -> int:
        lines = [line.split(" -> ") for line in self.input]
        conjunctions = [line[0][1:] for line in lines if line[0][0] == "&"]
        flip_flops = [line[0][1:] for line in lines if line[0][0] == "%"]
        flip_flops_on: set[str] = set()
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
        loop_lengths: dict[str, int] = {"fv": 0, "jd": 0, "vm": 0, "lm": 0}
        lcm = 0
        cnt = 1
        while lcm == 0:
            queue: deque[tuple[str, str, str]] = deque()
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
                    if dest == "zg" and signal == "hi":
                        loop_lengths[src] = cnt - loop_lengths[src]
                        if all(value != 0 for value in loop_lengths.values()):
                            lcm = math.lcm(*loop_lengths.values())
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
            cnt += 1
        return lcm
