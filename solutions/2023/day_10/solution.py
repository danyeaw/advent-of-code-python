# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/10

from collections import deque

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 10

    @answer(6613)
    def part_1(self) -> int:
        valid_up = "|7FS"
        valid_down = "|LJS"
        valid_left = "-LFS"
        valid_right = "-J7S"
        maze_size = [0, 0]
        maze = {}
        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char != ".":
                    maze[(x, y)] = char, []
                if x > maze_size[0] or y > maze_size[1]:
                    maze_size = [x, y]
        start = ()
        for space, (char, connected_neighbors) in maze.items():
            x, y = space
            if (
                char in valid_down
                and maze.get((x, y - 1))
                and maze[x, y - 1][0] in valid_up
            ):
                maze[x, y][1].append((x, y - 1))
            if (
                char in valid_up
                and maze.get((x, y + 1))
                and maze[x, y + 1][0] in valid_down
            ):
                maze[x, y][1].append((x, y + 1))
            if (
                char in valid_right
                and maze.get((x - 1, y))
                and maze[x - 1, y][0] in valid_left
            ):
                maze[x, y][1].append((x - 1, y))
            if (
                char in valid_left
                and maze.get((x + 1, y))
                and maze[x + 1, y][0] in valid_right
            ):
                maze[x, y][1].append((x + 1, y))
            if char == "S":
                start = space

        search_queue = deque()
        breadth = 0
        search_queue.append((maze[start][1][0], breadth))
        searched = []
        while search_queue:
            pipe, breadth_new = search_queue.popleft()
            if pipe not in searched:
                breadth = breadth_new
                searched.append(pipe)
                for neighbor in maze[pipe][1]:
                    search_queue.append((neighbor, breadth + 1))
        return breadth

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
