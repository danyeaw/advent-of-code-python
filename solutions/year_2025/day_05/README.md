# Day 5 (2025)

`CAFETERIA` ([prompt](https://adventofcode.com/2025/day/5))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

I was originally trying to expand the ranges in to a list of all the possible numbers. This
worked with the test data, but it took way too long with the full data set. You can directly
check if a number is in a tuple without expanding them.

## Part 2

I first tried to solve this by finding the length of a set with all the ranges expanded. Once
again this was too slow though. Instead I created a function that combines ranges when they
overlap. To do this it tracks the start and end we are at currently and first the next range.
We only update the current start if there is a gap between ranges.
