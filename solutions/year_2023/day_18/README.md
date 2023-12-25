# Day 18 (2023)

`Lavaduct Lagoon` ([prompt](https://adventofcode.com/2023/day/18))

## Part 1

I first tried to take advantage of the vector graphics drawing from day 10,
which I got the test sample to give the right answer, but I couldn't get it to
work with the real data. I then applied the Shoelace Theorem to calculate the
area inside the figure, and added some for 1/2 the width of the line for
perimeter and one more for 4 1/4 corners.

## Part 2

To convert from hex to decimal you can do int(hex_string, 16) which is new to
me for this challenge.
