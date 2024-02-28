import pytest
from sudoku import Grid

@pytest.fixture
def starting_grid() -> Grid:
    return Grid(
        [   
            [2, 3, 0, 1, 9, 6, 0, 5, 4], 
            [0, 5, 7, 0, 0, 0, 0, 2, 9], 
            [0, 1, 0, 5, 7, 2, 0, 0, 0], 
            [0, 0, 9, 0, 0, 4, 0, 0, 0],
            [1, 0, 5, 8, 0, 0, 0, 0, 0],
            [3, 0, 6, 0, 0, 9, 0, 0, 8],
            [0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 6, 0, 0, 0, 8, 2, 0, 0], 
            [7, 8, 2, 3, 0, 0, 0, 4, 0]
        ]
    )

@pytest.fixture
def solved_grid() -> list:
    return [
        [2, 3, 8, 1, 9, 6, 7, 5, 4],
        [6, 5, 7, 4, 8, 3, 1, 2, 9],
        [9, 1, 4, 5, 7, 2, 8, 6, 3],
        [8, 2, 9, 6, 1, 4, 3, 7, 5],
        [1, 4, 5, 8, 3, 7, 6, 9, 2],
        [3, 7, 6, 2, 5, 9, 4, 1, 8],
        [4, 9, 3, 7, 2, 1, 5, 8, 6],
        [5, 6, 1, 9, 4, 8, 2, 3, 7],
        [7, 8, 2, 3, 6, 5, 9, 4, 1]
    ]

def test_set_val(starting_grid: Grid) -> None:
    starting_grid.set_val(0, 1, 9)
    assert(starting_grid.grid[1][0] == 9)

def test_width(starting_grid: Grid) -> None:
    assert starting_grid.width == 9

def test_zone_width(starting_grid: Grid) -> None:
    assert starting_grid.zone_width == 3

def test_is_solved(starting_grid: Grid) -> None:
    assert not starting_grid.is_solved

def test_get_column(starting_grid: Grid) -> None:
    assert (
        starting_grid.get_column(0) == 
        [2, 0, 0, 0, 1, 3, 0, 0, 7]
    )

def test_get_zone(starting_grid: Grid) -> None:
    assert (
        starting_grid.get_zone(3, 4) == 
        [[0, 0, 4], [8, 0, 0], [0, 0, 9]]
    )

def test_solve_grid(starting_grid: Grid, solved_grid: list) -> None:
    Grid.solve(starting_grid)
    assert (
        starting_grid.is_solved and
        starting_grid.grid == solved_grid
    )