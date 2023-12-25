# puzzle prompt: https://adventofcode.com/2023/day/19
import collections
from collections import namedtuple

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 19

    @answer(399284)
    def part_1(self) -> int:
        blocks = self.input.split("\n\n")
        workflows_list = [
            workflow.replace("}", "").split("{") for workflow in blocks[0].split("\n")
        ]
        workflows = {workflow[0]: workflow[1].split(",") for workflow in workflows_list}
        for workflow_name, workflow in workflows.items():
            for idx, step in enumerate(workflow):
                if ":" in step:
                    split_step = step.split(":")
                    workflows[workflow_name][idx] = split_step

        Rating = namedtuple("Rating", ["x", "m", "a", "s"])
        ratings = [
            rating.replace("{", "").replace("}", "").split(",")
            for rating in blocks[1:][0].split("\n")
        ]
        ratings = [Rating(*[int(value[2:]) for value in rating]) for rating in ratings]
        accepted = []
        for rating in ratings:
            queue = collections.deque(["in"])
            while queue:
                workflow = queue.pop()
                for step in workflows[workflow]:
                    if step == "A":
                        accepted.append(rating)
                        queue.clear()
                        break
                    elif step == "R":
                        queue.clear()
                        break
                    elif ">" in step[0]:
                        field, value = step[0].split(">")
                        if getattr(rating, field) > int(value):
                            if step[1] == "A":
                                accepted.append(rating)
                                queue.clear()
                            elif step[1] == "R":
                                queue.clear()
                            else:
                                queue.append(step[1])
                            break
                    elif "<" in step[0]:
                        field, value = step[0].split("<")
                        if getattr(rating, field) < int(value):
                            if step[1] == "A":
                                accepted.append(rating)
                                queue.clear()
                            elif step[1] == "R":
                                queue.clear()
                            else:
                                queue.append(step[1])
                            break
                    else:
                        queue.append(step)
        return sum(sum(rating) for rating in accepted)

    # @answer(1234)
    def part_2(self) -> int:
        return 0
