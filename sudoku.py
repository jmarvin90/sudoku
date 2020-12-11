from copy import deepcopy
from math import sqrt

class Grid:
    """
    A class to represent a the sudoku grid to be solved.
    
    Attributes
    ----------
    grid:array
        array of arrays (rows) comprising the grid
    x_size:int
        length of the first row in the grid; depicts the grid zone_width
    zone_width:int
        width of the zones (squares) each grid is made up of (e.g. 3 in a 9x9 grid)
        
    Methods
    -------
    get_columns(self)
        Returns a transposed version of the grid to enable operations by column 
        vs. by row
    get_zone(self, x, y)
        Identifies the grid 'zone' for a given set of coordinates, and returns values 
        for all coordinates in that zone as a single contiguous array
    show(self)
        Prints the current grid to terminal
    propose(self, x, y, value)
        Determines the validity for placement of a given value in the provided 
        coordinates according to whether the given value is already in the same
        row, column, or zone; returns boolean outcome
    set_value(self, x, y, value)
        Assigns the provided value to the given x, y coordinate position in the grid
    next_blank(self)
        Identifies the 'first' blank (0) coordinate position in the grid when starting 
        from the top left and working left:right through each row. Returns the coordinates 
        for the next blank coordinate position.
    """
    
    def __init__(self, grid):
        self.grid = grid
        self.x_size = len(self.grid[0])
        self.zone_width = int(sqrt(self.x_size))
        
    def get_columns(self):
        """Returns a transposed version of the grid to enable operations by column 
        vs. by row   
        """ 

        columns = list(zip(*self.grid))
        return columns
        
    def get_zone(self, x, y): 
        """Identifies the grid 'zone' for a given set of coordinates, and returns values 
        for all coordinates in that zone as a single contiguous array
        """

        x_start = int(x/self.zone_width)*self.zone_width
        y_start = int(y/self.zone_width)*self.zone_width
        
        zone = []
        
        for i in range(0, self.zone_width): 
            zone = zone + self.grid[y_start+i][x_start:x_start+self.zone_width]
        
        return zone                  
        
    def show(self):
        """Prints the current grid to terminal
        """

        for row in self.grid: 
            print(f"{row}")
        print("\n")
            
    def propose(self, x, y, value):
        """Determines the validity for placement of a given value in the provided 
        coordinates according to whether the given value is already in the same
        row, column, or zone; returns boolean outcome
        """

        in_row = value in self.grid[y]
        in_column = value in self.get_columns()[x]
        in_zone = value in self.get_zone(x, y)
        return((not in_row) and (not in_column) and (not in_zone))
        
    def set_value(self, x, y, value):
        """Assigns the provided value to the given x, y coordinate position 
        in the grid
        """

        self.grid[y][x] = value
        
    def next_blank(self): 
        """Identifies the 'first' blank (0) coordinate position in the grid when 
        starting from the top left and working left:right through each row. 
        Returns the coordinates for the next blank coordinate position.
        """

        for y in range(0, len(self.grid)): 
            for x in range (0, len(self.grid[y])): 
                if self.grid[y][x] == 0: 
                    return {'x':x, 'y':y} 
        return None

def solve(grid, cycle=0):
    next_blank = grid.next_blank()
    if not next_blank: 
        grid.show()
        return grid
    else: 
        grid2=Grid(deepcopy(grid.grid))
        for number in range (1, grid.x_size + 1): 
            if grid.propose(next_blank['x'], next_blank['y'], number): 
                grid2.set_value(next_blank['x'], next_blank['y'], number)
                solve(grid2, cycle+1)                	
                
                     

"""grid = Grid([
                [2, 3, 0, 1, 9, 6, 0, 5, 4], 
                [0, 5, 7, 0, 0, 0, 0, 2, 9], 
                [0, 1, 0, 5, 7, 2, 0, 0, 0], 
                [0, 0, 9, 0, 0, 4, 0, 0, 0],
                [1, 0, 5, 8, 0, 0, 0, 0, 0],
                [3, 0, 6, 0, 0, 9, 0, 0, 8],
                [0, 0, 0, 0, 0, 0, 5, 0, 0],
                [0, 6, 0, 0, 0, 8, 2, 0, 0], 
                [7, 8, 2, 3, 0, 0, 0, 4, 0]
            ])"""
            
"""grid = Grid([
                [5, 3, 0, 0, 7, 0, 0, 0, 0], 
                [6, 0, 0, 1, 9, 5, 0, 0, 0], 
                [0, 9, 8, 0, 0, 0, 0, 6, 0], 
                [8, 0, 0, 0, 6, 0, 0, 0, 3], 
                [4, 0, 0, 8, 0, 3, 0, 0, 1], 
                [7, 0, 0, 0, 2, 0, 0, 0, 6], 
                [0, 6, 0, 0, 0, 0, 2, 8, 0], 
                [0, 0, 0, 4, 1, 9, 0, 0, 5], 
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ])"""
            
grid = Grid([
                [5, 3, 0, 0, 7, 0, 0, 0, 0], 
                [6, 0, 0, 1, 9, 5, 0, 0, 0], 
                [0, 9, 8, 0, 0, 0, 0, 6, 0], 
                [8, 0, 0, 0, 6, 0, 0, 2, 3], 
                [4, 2, 0, 8, 5, 3, 7, 9, 1], 
                [7, 1, 3, 0, 2, 0, 8, 5, 6], 
                [9, 6, 0, 5, 3, 7, 2, 8, 0], 
                [2, 8, 7, 4, 1, 9, 6, 3, 5], 
                [0, 0, 0, 0, 8, 0, 1, 7, 9]
            ])
         
         
grid.show()
solve(grid)