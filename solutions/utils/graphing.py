from operator import itemgetter

GridPoint = tuple[int, int]
Grid = dict[GridPoint, str]


def parse_grid(raw_grid: list[str], ignore_chars: str = "") -> Grid:
    result: Grid = {}
    for row, line in enumerate(raw_grid):
        for col, char in enumerate(line):
            if char == ignore_chars:
                continue
            result[col, row] = char
    return result


def add_points(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def subtract_points(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] - b[0], a[1] - b[1]


def draw_grid(grid: Grid, features: set[GridPoint]) -> None:
    width = max(grid, key=itemgetter(0))[0]
    for row_num in range(width):
        for col_num in range(width):
            if (col_num, row_num) in features:
                print("#", end="")
            else:
                print(grid[col_num, row_num], end="")
        print()
