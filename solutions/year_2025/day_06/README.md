# Day 6 (2025)

`TRASH COMPACTOR` ([prompt](https://adventofcode.com/2025/day/6))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

`list(zip(*rows))` was useful for transposing the rows in to columns.

## Part 2

For this solution I used a grid. Process all the columns right to left, but iterate
from the max x value to 0. For each column we then process all characters top to bottom.
If we find an empty column, it's a separator and then you calculate the result for the
next problem. Finally at the last column we process it since it doesn't have a separator.
