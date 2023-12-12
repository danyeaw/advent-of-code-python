# Day 4 (2023)

`Scratchcards` ([prompt](https://adventofcode.com/2023/day/4))

## Part 1

The string parsing for part 1 was a little tricky because the data on the scratchcards is arranged in rows,
so one-digit numbers have two spaces in front of them. I tried to develop a regex to parse these lines, but
I was struggling with having a repetitive match group of the numbers, while ignoring the whitespaces. I ended
up just replacing the two spaaces with one, and then using `str.split` to process them.

## Part 2

This was a tough one to figure out, since I was originally thinking that the problem was asking for recursion.
Once I talked through it again, I created a list that held the number of cards of each card number. Then as I looped
through the cards, I added the extra cards earned to the list. The number of cards added to each future card type
depends on the number of current cards like `scorecards[next_card_id] += scorecards[card_id]`.
