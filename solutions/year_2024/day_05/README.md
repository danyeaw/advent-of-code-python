# Day 5 (2024)

`PRINT QUEUE` ([prompt](https://adventofcode.com/2024/day/5))

The graphlib TopologicalGraph really helped for this one in Python.

## Part 1

I was originally trying to make this one way too complicated. I originally was trying to create a dictionary
graph for the rules where the X part of the rule was the key and the Y parts were values added to a list.
I was then trying to create a sorted list of all numbers found in all the updates using this graph. It worked
for the test input, but I wasn't getting the right answer for the full input, probably due to issues with my
sorting algorithm.

Instead, we can run each update through each rule to see if it passes all of them.

## Part 2

I learned about graphlib TopologicalGraph for this one. This is similar to what I was trying to do in part1
initially, but it manages sorting for you. We also don't need to sort all numbers found in all updates, we
only need to sort each update that doesn't pass the rules using only the rules that have both their numbers
in the update.
