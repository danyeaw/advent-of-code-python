# puzzle prompt: https://adventofcode.com/2023/day/20
import math
from collections import Counter, deque

from ...base import StrSplitSolution, answer


def execute_button_press(
    src_to_dest: dict[str, set[str]],
    conjunctions_to_inputs: dict[str, dict[str, str]],
    conjunctions: list[str],
    flip_flops: list[str],
    flip_flops_on: set[str],
    loop_lengths: dict[str, int],
    count: Counter[str],
):
    queue: deque[tuple[str, str, str]] = deque()
    queue.append(("broadcaster", "button", "lo"))
    lcm = 0
    while queue:
        dest, src, signal = queue.popleft()
        if dest == "zg" and signal == "hi":
            loop_lengths[src] = count["part2"] - loop_lengths[src]
            if all(value != 0 for value in loop_lengths.values()):
                lcm = math.lcm(*loop_lengths.values())
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
    return count, lcm


def parse(
    line_input: list[str],
) -> tuple[
    dict[str, set[str]], dict[str, dict[str, str]], list[str], list[str], set[str]
]:
    lines = [line.split(" -> ") for line in line_input]
    conjunctions: list[str] = [line[0][1:] for line in lines if line[0][0] == "&"]
    flip_flops: list[str] = [line[0][1:] for line in lines if line[0][0] == "%"]
    flip_flops_on: set[str] = set()
    src_to_dest: dict[str, set[str]] = {
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
    return src_to_dest, conjunctions_to_inputs, conjunctions, flip_flops, flip_flops_on


class Solution(StrSplitSolution):
    _year = 2023
    _day = 20

    @answer(825896364)
    def part_1(self) -> int:
        (
            src_to_dest,
            conjunctions_to_inputs,
            conjunctions,
            flip_flops,
            flip_flops_on,
        ) = parse(self.input)
        count: Counter[str] = Counter(lo=0, hi=0)
        for _ in range(1000):
            count, _ = execute_button_press(
                src_to_dest,
                conjunctions_to_inputs,
                conjunctions,
                flip_flops,
                flip_flops_on,
                {},
                count,
            )
        return count["lo"] * count["hi"]

    @answer(243566897206981)
    def part_2(self) -> int:
        (
            src_to_dest,
            conjunctions_to_inputs,
            conjunctions,
            flip_flops,
            flip_flops_on,
        ) = parse(self.input)
        loop_lengths: dict[str, int] = {"fv": 0, "jd": 0, "vm": 0, "lm": 0}
        lcm = 0
        count = Counter(part2=1)
        while lcm == 0:
            _, lcm = execute_button_press(
                src_to_dest,
                conjunctions_to_inputs,
                conjunctions,
                flip_flops,
                flip_flops_on,
                loop_lengths,
                count,
            )
            count["part2"] += 1
        return lcm
