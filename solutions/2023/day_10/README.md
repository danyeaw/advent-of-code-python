# Day 10 (2023)

`Pipe Maze` ([prompt](https://adventofcode.com/2023/day/10))

## Part 1

Initial solution created maze in x, y coordinates with a dictionary of pipe
position as the key and values of the character at position and a list of
neighboring pipe positions that are connected. Since the route in unweighted
and there is only one valid loop, I just did a Breadth First Search to find the
path, and the farthest breadth is the answer.

## Part 2

