# Day 21 (2023)

`Step Counter` ([prompt](https://adventofcode.com/2023/day/21))

## Part1

I tried to implement this as both Depth First Search and Breadth First Search.
They worked with the test input, but with the real input, the reachable
positions were taking too long to calculate. The trick here was that when
looking at each step of searching, if the parity of the step matches the step
length, then it will be part of the reachable steps at that step length. You
can then only search each grid position once, instead of searching over and
over again for the next breadth.

## Part 2

