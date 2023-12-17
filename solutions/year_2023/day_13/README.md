# Day 13 (2023)

`Point of Incidence` ([prompt](https://adventofcode.com/2023/day/13))

## Part 1

I was originally finding the reflection point and then comparing each row out
from that point. This required a lot of checks for finding the max and min row.
Zip does this automatically because it stops with the shortest iterable. So you
can zip the rows in both directions and check that they are all equal.

## Part 2

Instead of checking all the lines are the same on the reflection, we now look
for smudge. We find the distance between the two would be 1. To find the
distance we zip up the two rows and sum the differences.
