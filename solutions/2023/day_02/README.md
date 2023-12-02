# Day 2 (2023)

`Cube Conundrum` ([prompt](https://adventofcode.com/2023/day/2))

## Part 1

My initial solution was to parse the string, use Enums for the Colors, and loop through each color in each draw
to see if they were too large.

The Enums weren't really helping here and a simple dictionary can hold the max values. `re.findall` is also a nice
way to parse the string because it returns a list of tuples. This works because we don't care which draw the color
was from, only that it is too high so this flattens the data structure. Finally, using `all()` significantly reduced
the code to check that all counts were below their max values using the dictionary lookup.

## Part 2

My initial part 2 solution was similar to my part 1. With the refactorings I did for part 1, a `defaultdict` was used
to store the maximums per color.
