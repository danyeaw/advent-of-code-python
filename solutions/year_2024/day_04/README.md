# Day 4 (2024)

`CERES SEARCH` ([prompt](https://adventofcode.com/2024/day/4))

## Part 1

I originally tried to use string search for the horizontal words, and flip the puzzle to get the vertical.
Unfortunately, this became really unwieldy with the diagonals.

I used grid parsing instead to search for neighbors around the Xs to see if they had the full word.

## Part 2

The grid parsing was adopted to search around the As only in the diagonals, and look for two diagonals to increment
the result.
