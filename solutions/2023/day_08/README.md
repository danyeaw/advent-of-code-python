# Day 8 (2023)

`Haunted Wasteland` ([prompt](https://adventofcode.com/2023/day/8))

## Part 1

I learned about `itertools.cycle` for repeating an iterator. Also, it seems like it is easier to create a list
in the format you want for a dict, and then creating the dict with `dict()` rather than trying to create a complex
dictionary comprehension.

## Part 2

The change in this one to do 6 calculations at once was pretty straight forward. Unfortunately, the answer is in the
trillions, and would have taken a very long time to brute force.

Each of the 6 paths gets stuck in a very large loop that repeat themselves after 10,000+ counts through the possible
combinations. Once you find the loop length for each input, you can take the Least Common Multiple (LCM) of the
6 loop lengths to find the solution.
