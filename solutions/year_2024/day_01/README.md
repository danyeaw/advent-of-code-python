# Day 1 (2024)

`HISTORIAN HYSTERIA` ([prompt](https://adventofcode.com/2024/day/1))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1 and Part 2

I originally used a for loop and appended to two lists to create the columns of numbers.
I learned that I could use a list comprehension with map to turn the values in to pairs
of ints and then do a second comprehension to zip and sort the values per column.

Each solution was pretty straightforward from there, use sum to make the two final calculations.
