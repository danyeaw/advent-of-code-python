# Day 6 (2024)

`GUARD GALLIVANT` ([prompt](https://adventofcode.com/2024/day/6))

## Part 1

This part had us track the guard's movements and I used a set to keep track of visited locations. I also kept track of
the direction using a string with a dictionary used to lookup the offset to the next point moved to.

## Part 2

Now we need to keep track of both the locations visited and the direction when visiting each location. If we
find a duplicate, then we know we are in a loop and can add this position to the number of possible obstructions.

Additionally, we only need to try to add an obstruction to points on the path from part 1.
