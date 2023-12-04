# Day 4 (2023)

`Scratchcards` ([prompt](https://adventofcode.com/2023/day/4))

## Part 1

The string parsing for part 1 was a little tricky because the data on the scratchcards is arranged in rows,
so one-digit numbers have two spaces in front of them. I tried to develop a regex to parse these lines, but
I was struggling with having a repetitive match group of the numbers, while ignoring the whitespaces. I ended
up just replacing the two spaaces with one, and then using `str.split` to process them.

## Part 2

