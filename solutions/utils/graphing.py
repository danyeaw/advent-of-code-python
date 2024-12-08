GridPoint = tuple[int, int]
Grid = dict[GridPoint, str]


def parse_grid(raw_grid: list[str], ignore_chars: str = "") -> Grid:
    result: Grid = {}
    for row, line in enumerate(raw_grid):
        for col, char in enumerate(line):
            if char == ignore_chars:
                continue
            result[row, col] = char
    return result


def add_points(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]
