# Day 20 (2023)

`Pulse Propogation` ([prompt](https://adventofcode.com/2023/day/20))

## Part 1

I first tried to do this with pen and paper after I saw that the graphviz plot
showed that there were four 12 bit binary counters, which cycles every 12 bit
button press. I wasn't able to get the right answer though. Instead of doing
OOP techniques, I just stored the majority of the problem in dictionaries which
worked well.

## Part 2

This was another Least Common Multiple (LCM) program like day 8. Each of the 12
bit counters are slightly different with how many signals they send to the main
conjugator for the counter. This causes the main conjugation to getting the one
rx output all offset. LCM finds where all these repeating cycles come together
to output a single low pulse.
