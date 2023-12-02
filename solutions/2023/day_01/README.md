# Day 1 (2023)

`TREBUCHET?!?` ([prompt](https://adventofcode.com/2023/day/1))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

For the initial solution, the idea is to use markers that point to the first
and last digit in each line. This was good, but required a for loop, a couple
of variables to hold the first and last values, and conditional statements.

The optimized solution uses a single list comprehension to put all the digits
in a list, and then use indexing to get the first and last digits.
