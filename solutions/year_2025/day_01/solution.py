# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


def move_dial(current_location: int, direction: str, distance: int) -> tuple[int, int]:
    """
    Calculate the dial's final position and count how many times it passes through zero.

    Uses mathematical calculation instead of simulation for O(1) performance.
    Returns: (final_position, zero_crossings_count)
    """
    step_size = -1 if direction == "L" else 1
    final_location = (current_location + step_size * distance) % 100

    # Count zero crossings: we cross zero when position equals a multiple of 100
    if direction == "R":
        # Moving right: visit positions current_location+1 to current_location+distance
        start_pos = current_location + 1
        end_pos = current_location + distance
    else:
        # Moving left: visit positions current_location-1 down to current_location-distance
        # Note: Even though start_pos < end_pos seems backwards, we're just finding
        # the range of numeric values (before modulo) that we pass through.
        # Example: from 50 moving left 60 steps visits positions 49, 48, ..., 0, 99, ..., 90
        # In numeric terms (before % 100): 49, 48, ..., 1, 0, -1, -2, ..., -10
        # So the range is [-10, 49], and we count multiples of 100 in that range (just 0)
        start_pos = current_location - distance
        end_pos = current_location - 1

    # Count multiples of 100 in the range [start_pos, end_pos]
    # first_multiple: smallest multiple of 100 >= start_pos (using ceiling division)
    # last_multiple: largest multiple of 100 <= end_pos (using floor division)
    first_multiple = (start_pos + 99) // 100
    last_multiple = end_pos // 100
    zero_crossings = max(0, last_multiple - first_multiple + 1)

    return final_location, zero_crossings


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer((1084, 6475))
    def solve(self) -> tuple[int, int]:
        """
        Part 1: Count how many times the dial ends at position 0 after each rotation.
        Part 2: Count the total number of times the dial passes through position 0
                during all movements (not just at the end).
        """
        dial_position = 50
        times_ended_at_zero = 0
        total_zero_crossings = 0

        for line in self.input:
            direction, distance = line[0], int(line[1:])
            dial_position, zero_crossings = move_dial(
                dial_position, direction, distance
            )
            if dial_position == 0:
                times_ended_at_zero += 1
            total_zero_crossings += zero_crossings

        return times_ended_at_zero, total_zero_crossings
