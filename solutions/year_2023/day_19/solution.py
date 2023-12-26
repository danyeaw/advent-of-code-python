# puzzle prompt: https://adventofcode.com/2023/day/19
from functools import reduce

from ...base import TextSolution, answer


def is_approved(ratings, workflows: dict[str, str], next_workflow: str) -> bool:
    workflow = workflows[next_workflow]
    x, m, a, s = ratings
    for step in workflow.split(","):
        if step == "R":
            return False
        elif step == "A":
            return True
        elif ":" not in step:
            return is_approved(ratings, workflows, step)
        cond = step.split(":")[0]
        if eval(cond):
            if step.split(":")[1] == "R":
                return False
            return (
                True
                if step.split(":")[1] == "A"
                else is_approved(ratings, workflows, step.split(":")[1])
            )
    return False


def add_ranges(ranges: dict[str, range], cond: str) -> dict[str, range] | None:
    category, op, value = cond[0], cond[1], int(cond[2:])
    rng = ranges.get(category, range(1, 4001))
    if op == "<" and value <= rng.start or op == ">" and value > (rng.stop - 1):
        return None
    elif op == "<":
        return {category: range(rng.start, value)}
    return {category: range(value + 1, rng.stop)}


def inverse(cond: str) -> str:
    category, op, value = cond[0], cond[1], int(cond[2:])
    return f"{category}>{value - 1}" if op == "<" else f"{category}<{value + 1}"


def trace_path(workflows: dict[str, str], state: tuple[str, dict[str, range]]):
    workflow_name, ranges = state
    print(state)
    workflow = workflows[workflow_name]
    for step in workflow.split(","):
        if step == "A":
            yield ranges
        elif ":" not in step and step != "R":
            yield from trace_path(workflows, (step, ranges))
        elif ":" in step:
            cond, next_workflow = step.split(":")
            if next_workflow != "R":
                if first_ranges := add_ranges(ranges, inverse(cond)):
                    if step.split(":")[1] == "A":
                        yield first_ranges
                    else:
                        yield from trace_path(
                            workflows, (step.split(":")[1], first_ranges)
                        )
                if second_ranges := add_ranges(ranges, cond):
                    if step.split(":")[1] == "A":
                        yield second_ranges
                    else:
                        yield from trace_path(
                            workflows, (step.split(":")[1], second_ranges)
                        )


def count_paths(paths):
    print(paths)
    return sum(
        reduce(int.__mul__, [len(rng) + 1 for rng in path.values()]) for path in paths
    )


class Solution(TextSolution):
    _year = 2023
    _day = 19

    @answer(399284)
    def part_1(self) -> int:
        blocks = self.input.split("\n\n")
        workflows = {
            line.split("{")[0]: line.split("{")[1][:-1]
            for line in blocks[0].split("\n")
        }
        parts = (
            rating.replace("{", "").replace("}", "").split(",")
            for rating in blocks[1:][0].split("\n")
        )
        parts = (tuple(int(value[2:]) for value in part) for part in parts)
        return sum(sum(part) for part in parts if is_approved(part, workflows, "in"))

    # @answer(1234)
    def part_2(self) -> int:
        blocks = self.input.split("\n\n")
        workflows = {
            line.split("{")[0]: line.split("{")[1][:-1]
            for line in blocks[0].split("\n")
        }
        state = ("in", {category: range(1, 4001) for category in "xmas"})
        return count_paths(trace_path(workflows, state))
