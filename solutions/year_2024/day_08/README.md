# Day 8 (2024)

`RESONANT COLLINEARITY` ([prompt](https://adventofcode.com/2024/day/8))

The main thing that I learned is I need to graph grid to troubleshoot issues. I added a draw_grid utility to
help with this going forward.

I also got stuck for a while because I was using itertools pairwise, when I should have been using
combinations. Pairwise always returns 1 less that the total number of items.
