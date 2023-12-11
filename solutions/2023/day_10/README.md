# Day 10 (2023)

`Pipe Maze` ([prompt](https://adventofcode.com/2023/day/10))

## Part 1

Initial solution created maze in x, y coordinates with a dictionary of pipe
position as the key and values of the character at position and a list of
neighboring pipe positions that are connected. Since the route in unweighted
and there is only one valid loop, I just did a Breadth First Search to find the
path, and the farthest breadth is the answer.

## Part 2

I took advantage of how vector graphics are drawn. You can iterate through the
line and find polarity based on vertical pipes you intersect, odd is inside the
loop. I iterated over each row kept a `is_inside` variable that starts false.
We then iterate for each tile, and for each pipe that has a side pointing north
and is in the list of pipes in the loop from part 1, we invert `is_inside`.

For any positions that are inside and not pipes, we add these positions to the
enclosed list and then find the length of that to get the solution.
