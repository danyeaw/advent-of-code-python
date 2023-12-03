# Day 3 (2023)

`Gear Ratios` ([prompt](https://adventofcode.com/2023/day/3))

## Part 1

My initial solution was to use 3 rows, the previous row, the current row, and
the next row. I then on each current row I found the numbers on the engine
schematic using a `re.finditer` which returns all the matches including the
start and end indexes of the numbers and the values themselves. I then created
an area around each returned number and summed up any numbers that had a symbol
in this area.

The updated solution is using a couple of data structures which uses a little
bit more memory, but greatly simplifies the solution. This is possible since
the schematic is 140x140 and we can treat it like a board with rows and
columns. The first data structure, a dictionary, puts all symbols on the board,
and saves it with the key being the coordinate to the symbol and the value
being a list of adjacent numbers. When initializing the dictionary, the values
start out being blank lists. We still find the numbers in each row the same
way, but we build the area using a set of tuple coordinates. We then use the
bit-wise and `&` to overlay the set with the keys of the dictionary. Finally,
we sum up the sum of the dictionary values.

## Part 2

My initial solution for this was similar to part 1, except I started with
finding the * symbols in each row instead of the numbers. I then created an
area like part 1, and found the indexes of the numbers in the area. I then
found the full numbers by searching back through all three full rows for that
index.

The updated solution for part 2 matches the part 1 updated solution almost
exactly. It happened to be that no two numbers were adjacent to a symbol,
except for * symbols. So the result is the same as part 1, except looking for
dictionary values with exactly two values and doing the product of them.
