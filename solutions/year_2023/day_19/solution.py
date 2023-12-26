# puzzle prompt: https://adventofcode.com/2023/day/19
from ...base import TextSolution, answer


def is_approved(ratings, workflows: dict[str, str], next_workflow: str) -> bool:
    workflow = workflows[next_workflow]
    x, m, a, s = ratings
    for step in workflow.split(","):
        if step == "R":
            return False
        if step == "A":
            return True
        if ":" not in step:
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
        return 0
