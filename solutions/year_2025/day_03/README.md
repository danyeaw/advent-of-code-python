# Day 3 (2025)

`LOBBY` ([prompt](https://adventofcode.com/2025/day/3))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

Since we only need 2 digits, we can use nested for loops with taking the
second loop one to the right of the first and iterating through the whole
battery bank.

## Part 2

I first tried to do the same method, but this requires combinational
possibilities to brute force. Instead, a greedy algorithm can be used
to find the max value from the start until the end with room for the
number of digits needed. Then find the first index with that max value,
and then keep going through all the digits by putting the start for the
next one after the index from the previous one.

