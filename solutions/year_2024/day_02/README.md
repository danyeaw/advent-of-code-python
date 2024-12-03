# Day 2 (2024)

`RED-NOSE REPORTS` ([prompt](https://adventofcode.com/2024/day/2))

Good practice with list comprehensions, all, sum, and pairwise.

## Part 1

Good practice with nested list comprehension to parse the input.

`itertools.pairwise` was new for me, but made calculating differences in values
in the lists very easy. The `all()` function doesn't require a list comprehension
inside of it to check all values.

## Part 2

I was able to reuse a lot from part 1. A couple of things I got caught up on is
that you need to make sure to use `list.copy()` while modifying a copy of a list
since otherwise you modify the original list you are looping through. I was also
removing the first value of the level from the list, but with the real input the
answer was off by a couple. Instead I needed to one by one remove each value.
