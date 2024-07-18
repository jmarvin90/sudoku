from typing import NoReturn
from __future__ import annotations
import math
import copy

class Grid:
    def __init__(self, grid: list):
        self.__grid = grid
        self.solution = None

    def __str__(self) -> st:
        """String representation of the grid."""
        rows = []
        for row in self.grid:
            rows.append("".join([str(item) for item in row]))

        return "\n".join(rows)

    @property
    def grid(self) -> list:
        return self.__grid

    @grid.setter
    def grid(self, grid: list) -> NoReturn:
        self.__grid = grid

    @property
    def width(self) -> int:
        """Return width of the grid."""
        return len(self.__grid[0])

    @property
    def is_solved(self) -> bool:
        """Check whether the grid has been solved."""
        if self.solution or not self.next_blank():
            return True

        return False

    @property
    def zone_width(self) -> int:
        """Return the width of each 'zone' in the grid."""
        return int(math.sqrt(self.width))

    def set_val(self, x:int, y:int, val:int) -> NoReturn:
        """Set the value in the grid at the given coordinates."""
        self.grid[y][x] = val

    def get_column(self, column_number: int) -> list:
        """Return values from a specified column as a list."""
        return [row[column_number] for row in self.__grid]

    def get_zone(self, x: int, y: int) -> list:
        """Return values from a specified zone as a list of lists."""
        x_start = (x // self.zone_width) * self.zone_width
        x_end = x_start + self.zone_width

        y_start = (y // self.zone_width) * self.zone_width
        y_end = y_start + self.zone_width

        return [
            row[x_start:x_end] for row in self.__grid[y_start:y_end]
        ]

    def proposed_number_is_valid(self, x: int, y: int, number: int) -> bool:
        """Check validity of a specified number in the given coordinates."""
        in_row = number in self.__grid[y]
        in_col = number in self.get_column(x)
        in_zone = any([number in row for row in self.get_zone(x, y)])

        if any([in_row, in_col, in_zone]):
            return False

        return True

    def next_blank(self) -> tuple | None:
        """Find the next (from top left) blank space in the grid."""
        for y in range(self.width):
            for x in range(self.width):
                if self.__grid[y][x] == 0:
                    return (x, y)

        return None

    @staticmethod
    def solve(grid: Grid, origin: Grid = None) -> bool:
        """Update an input grid with the solution."""

        if not origin:
            origin = grid
        
        if grid.is_solved:
            origin.grid = grid.grid
            return True

        for number in range(1, grid.width + 1):
            if grid.proposed_number_is_valid(*grid.next_blank(), number):
                new_grid = Grid(copy.deepcopy(grid.grid))
                new_grid.set_val(*grid.next_blank(), number)
                if Grid.solve(new_grid, origin):
                    return True

        return False
