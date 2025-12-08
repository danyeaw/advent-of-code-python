# Day 7 (2025)

`LABORATORIES` ([prompt](https://adventofcode.com/2025/day/7))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

Part 1 was pretty straightforward using grids and sets since beams can't repeat in the same
location.

## Part 2

This was similar to part 1, but need to use depth first search to get the number of possible
combinations. A good tip is to use memoization, to ensure that if you visit a place on the
grid, that the value of the possible outcomes from there is stored.

