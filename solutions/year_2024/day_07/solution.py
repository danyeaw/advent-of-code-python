# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
# puzzle prompt: https://adventofcode.com/2024/day/7
from collections.abc import Callable, Sequence
from itertools import product
from operator import add, mul

from ...base import StrSplitSolution, answer
from ...utils.parsing import parse_int_list


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def process_ops(nums: list[int], ops: Sequence[Callable[[int, int], int]]) -> int:
    if len(nums) == 1:
        return nums[0]
    left, right, *rest = nums
    cur_op, *remaining_ops = ops
    return process_ops([cur_op(left, right), *rest], remaining_ops)


def process_line(line: str, enable_concat=False) -> int:
    target, *inputs = parse_int_list(line.replace(":", "").split())
    ops = [add, mul]
    if enable_concat:
        ops.append(concat)
    if any(
        process_ops(inputs, op_combo) == target
        for op_combo in product(ops, repeat=len(inputs) - 1)
    ):
        return target
    return 0


class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    @answer(882304362421)
    def part_1(self) -> int:
        return sum(process_line(calibration) for calibration in self.input)

    # @answer(1234)
    def part_2(self) -> int:
        return sum(
            process_line(calibration, enable_concat=True) for calibration in self.input
        )
