# Day 2 (2025)

`GIFT SHOP` ([prompt](https://adventofcode.com/2025/day/2))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

Using strings was key to this one.

## Part 2

If s = "101010", it will repeat if s is in (s + s)[1:-1], which doubles
the string and removes the first and last. This checks for repeated
substrings.
