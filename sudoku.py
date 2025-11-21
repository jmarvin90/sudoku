import math

def _to_gridpos(width: int, index: int) -> tuple:
    return (index % width, index // width)
	
def _to_index(width: int, grid_pos: tuple) -> int:
    x, y = grid_pos
    return int((width * y) + x)
	

class Grid:
    def __init__(self, values: list):
        self.values = values
        self.width = int(math.sqrt(len(self.values)))

    def __str__(self) -> str:
        return "".join(
            [
                ", ".join([str(item) for item in self.values[n:n+self.width]]) + "\n"
                for n in range(0, self.width**2, self.width)
            ]
        )
		
    def __getitem__(self, pos: tuple) -> int:
        return self.values[_to_index(self.width, pos)]
    
    def __setitem__(self, pos: tuple, val: int) -> None:
        self.values[_to_index(self.width, pos)] = val
    
    @property
    def is_solved(self) -> bool:
        """Check whether the grid is solved."""
        return 0 not in self.values
		
    def next_blank(self) -> tuple | None:
        """Fetch the coordinates for the next blank cell."""
        if not self.is_solved:
            return _to_gridpos(self.width, self.values.index(0))
        return None
	
    def get_row(self, num: int) -> list:
        """Get the contents of a specified row as a list."""
        row_min = num * self.width
        row_max = row_min + self.width
        return self.values[row_min:row_max]
        
    def get_col(self, num: int) -> list:
        """Get the contents of a specified column as a list."""
        return [
            self.values[(self.width * val) + num]
            for val in range(0, self.width)
        ]
        
    def get_zone(self, pos: tuple) -> list:
        """Get the contents of the 'zone' for a coordinate position."""
        x, y = pos
        zone_width = int(math.sqrt(self.width))
        
        output = []
        
        for row in range(0, zone_width):
            min_x = x - (x % zone_width)
            min_y = y - (y % zone_width)  + row
            index = _to_index(self.width, (min_x, min_y))
            output.extend(
                self.values[index:index+zone_width]
            )
            
        return output
        
    def placement_is_valid(self, num: int, pos: tuple) -> bool:
        """Check validity of placement for a number in a given position."""
        x, y = pos
        return (
            self[pos] == 0 and
            num not in self.get_row(y) and
            num not in self.get_col(x) and
            num not in self.get_zone(pos)
        )
		
def solve(grid: Grid) -> Grid:
    """Update an input grid with the solution."""
    if grid.is_solved:
        return grid

    # Keep a trail of placements we've proposed
    track = [(grid.next_blank(), 1)]
    
    while not grid.is_solved:
        # Work with the most recent proposed placement
        pos, num = track[-1]

        # Move on to the next blank cell if that placement
        # is potentially valid
        if (grid.placement_is_valid(num, pos)):
            grid[pos] = num
            track.append((grid.next_blank(), 1))
            continue

        # Otherwise remove that placement from the track, 
        # reset the grid cell value and propose the next number
        track.pop()
        grid[pos] = 0
        num += 1
        if not num > grid.width:
            track.append((pos, num))

    return grid

        
my_vals = [
	2, 3, 0, 1, 9, 6, 0, 5, 4,
	0, 5, 7, 0, 0, 0, 0, 2, 9,
	0, 1, 0, 5, 7, 2, 0, 0, 0,
	0, 0, 9, 0, 0, 4, 0, 0, 0,
	1, 0, 5, 8, 0, 0, 0, 0, 0,
	3, 0, 6, 0, 0, 9, 0, 0, 8,
	0, 0, 0, 0, 0, 0, 5, 0, 0,
	0, 6, 0, 0, 0, 8, 2, 0, 0,
	7, 8, 2, 3, 0, 0, 0, 4, 0
]

"""
        [2, 3, 8, 1, 9, 6, 7, 5, 4],
        [6, 5, 7, 4, 8, 3, 1, 2, 9],
        [9, 1, 4, 5, 7, 2, 8, 6, 3],
        [8, 2, 9, 6, 1, 4, 3, 7, 5],
        [1, 4, 5, 8, 3, 7, 6, 9, 2],
        [3, 7, 6, 2, 5, 9, 4, 1, 8],
        [4, 9, 3, 7, 2, 1, 5, 8, 6],
        [5, 6, 1, 9, 4, 8, 2, 3, 7],
        [7, 8, 2, 3, 6, 5, 9, 4, 1]
"""

my_grid = Grid(my_vals)
print(my_grid)
print(solve(my_grid))
