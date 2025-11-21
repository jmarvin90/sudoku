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
		
	def __getitem__(self, pos: tuple) -> int:
		return self.values[_to_index(self.width, pos)]
		
	def next_blank(self) -> tuple | None:
    """Fetch the coordinates for the next blank cell."""
    try:
		  return _to_gridpos(self.width, self.values.index(0))
    except ValueError:
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

my_grid = Grid(my_vals)
print(my_grid.placement_is_valid(7, (2, 0)))
