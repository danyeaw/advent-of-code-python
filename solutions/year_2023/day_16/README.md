# Day 16 (2023)

`The Floor Will be Lava` ([prompt](https://adventofcode.com/2023/day/16))

## Part 1

This is a great opportunity to make use of a dataclass to store state
information. Also, I heavily used the case match statement for all the
different mirror and splitter combos.

## Part 2

I didn't realize that the standard Enum hashes on the whole string, so an
IntEnum was much faster.
