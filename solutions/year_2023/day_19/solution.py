# puzzle prompt: https://adventofcode.com/2023/day/19
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


def apply_less(r: range, value: int):
    if r.start > value:
        return range(0), r
    if r.stop > value:
        return range(r.start, value), range(value, r.stop)
    return r, range(0)


def apply_more(r: range, value: int):
    if r.stop < value:
        return range(0), r
    if r.start <= value:
        return range(value + 1, r.stop), range(r.start, value + 1)
    return r, range(0)


class RangePart:
    __slots__ = ["x", "m", "a", "s"]

    def __init__(self, x, m, a, s):
        self.x: range = x
        self.m: range = m
        self.a: range = a
        self.s: range = s

    def as_dict(self):
        return dict(x=self.x, m=self.m, a=self.a, s=self.s)

    @property
    def size(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)

    def _apply(self, func, name: str, value: int):
        a, b = self.as_dict(), self.as_dict()
        a[name], b[name] = func(a[name], value)
        return RangePart(**a), RangePart(**b)

    def apply_less(self, name: str, value: int):
        return self._apply(apply_less, name, value)

    def apply_more(self, name: str, value: int):
        return self._apply(apply_more, name, value)


def make_solver2(rules):
    def run(part: RangePart, name):
        if part.size == 0:
            return 0
        if name == "A":
            return part.size
        if name == "R":
            return 0
        result = 0
        for rule in rules[name]:
            if ":" in rule:
                cond, target = rule.split(":")
                if ">" in cond:
                    name, value = cond.split(">")
                    a, part = part.apply_more(name, int(value))
                    result += run(a, target)
                elif "<" in cond:
                    name, value = cond.split("<")
                    a, part = part.apply_less(name, int(value))
                    result += run(a, target)
                else:
                    assert 0, rule
            else:
                result += run(part, rule)
        return result

    return run


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

    @answer(121964982771486)
    def part_2(self) -> int:
        blocks = self.input.split("\n\n")
        workflows = {
            line.split("{")[0]: line.split("{")[1][:-1].split(",")
            for line in blocks[0].split("\n")
        }
        part = RangePart(
            x=range(1, 4001),
            m=range(1, 4001),
            a=range(1, 4001),
            s=range(1, 4001),
        )
        run = make_solver2(workflows)
        return run(part, "in")
