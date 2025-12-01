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

    # Count how many times we cross position 0 during the movement.
    # We cross zero when (current_location + step_size * step_number) % 100 == 0
    # This happens when the position equals a multiple of 100.
    if direction == "R":
        # Moving right: we cross zero when position wraps from 99 to 0.
        # Find the range of multiples of 100 we'll cross during this movement.
        # First multiple we might hit: ceil((current_location + 1) / 100)
        first_multiple_of_100 = (current_location + 1 + 99) // 100
        # Last multiple we might hit: floor((current_location + distance) / 100)
        last_multiple_of_100 = (current_location + distance) // 100
        # Count how many multiples fall within our movement range
        zero_crossings = (
            max(0, last_multiple_of_100 - first_multiple_of_100 + 1)
            if first_multiple_of_100 <= last_multiple_of_100
            else 0
        )
    else:
        # Moving left: we cross zero when position wraps from 0 to 99.
        # Find the range of multiples of 100 we'll cross during this movement.
        # First multiple we might hit: ceil((current_location - distance) / 100)
        first_multiple_of_100 = (current_location - distance + 99) // 100
        # Last multiple we might hit: floor((current_location - 1) / 100)
        last_multiple_of_100 = (current_location - 1) // 100
        # Count how many multiples fall within our movement range
        zero_crossings = (
            max(0, last_multiple_of_100 - first_multiple_of_100 + 1)
            if first_multiple_of_100 <= last_multiple_of_100
            else 0
        )

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
        instructions = [(line[0], int(line[1:])) for line in self.input]

        for direction, distance in instructions:
            dial_position, zero_crossings = move_dial(
                dial_position, direction, distance
            )
            if dial_position == 0:
                times_ended_at_zero += 1
            total_zero_crossings += zero_crossings

        return times_ended_at_zero, total_zero_crossings
