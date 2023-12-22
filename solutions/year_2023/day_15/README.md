# Day 15 (2023)

`Lens Library` ([prompt](https://adventofcode.com/2023/day/15))

## Part 1

This one was quick as long as you know about ord().

## Part 2

In modern Python, dictionaries keep order. So this solution became much more
straight forward using a defaultdict that had the box number as the key and as
the value another dict with the label as the key and the focal length as the
value. Otherwise, you have to do a lot of work checking for keys and replacing
values in lists.
