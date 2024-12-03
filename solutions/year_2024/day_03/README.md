# Day 3 (2024)

`MULL IT OVER` ([prompt](https://adventofcode.com/2024/day/3))

Today was fun with regex!

## Part 1

I took the approach of using the re module, and doing re.finditer to search through the string.

## Part 2

I originally explored this part by seeing if I could easily use a negative lookbehind to see if
there was a don't() prior to the match. However, a lookbehind needs to immediately proceed the match.
Also, the problem has do() and don't() stay enabled until the next one.

So I matched for do() and don't() as part of the pattern, and then kept track of whether summing is
enabled as I looped through all the matches and only added to the total if summing is enabled.
