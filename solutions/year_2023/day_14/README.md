# Day 14 (2023)

`Parabolic Reflector Dish` ([prompt](https://adventofcode.com/2023/day/14))

## Part 1

This definitely wasn't the most efficient solution, but it was fast enough and
simple. It loops through the map of rocks and moves each rounded rock one to
the North as long as there isn't a cub-shaped rock above it. This could be
optimized to search for each rounded rock and then move each one as far as they
can go to the North.

## Part 2

I used the same strategy for Part 1, but I added the other directions. The
trick with part 2 is that the pattern repeats itself and going through
1,000,000 cycles takes way too long. For each cycle parse the map of rocks to
get the location of each rounded rock as a frozenset. We then check if this set
has been seen before and save it to a dict of seen sets. If it has been seen,
then calculate the loop length by subtracting the current cycle from the
previously found one looked up in the seen sets. The find the distance to the
goal by subtracting the current cycle from the total number of cycles. Finally,
jump forward by setting the current cycle to the difference between the total
cycles and the distance to the goal modulo the repeat cycle.
