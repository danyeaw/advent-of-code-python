# Day 1 (2023)

`TREBUCHET?!?` ([prompt](https://adventofcode.com/2023/day/1))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

For the initial solution, the idea is to use markers that point to the first
and last digit in each line. This was good, but required a for loop, a couple
of variables to hold the first and last values, and conditional statements.

The optimized solution uses a single list comprehension to put all the digits
in a list, and then use indexing to get the first and last digits.

## Part 2

Part two was a bit tricky, because in some of the lines the written out words overlap.
For example, eightwothree. If you search and replace it from low to high, you'll replace
the two and three with digits, and get eigh23. However, eight is the first digit, so the
answer should be 8wo3 or 83.

One way to resolve this is when replacing the word with the digit, keep the first and
last letters of the word, since those are the ones that could overlap.
