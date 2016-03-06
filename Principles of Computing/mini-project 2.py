"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = []
    mergeable = False
    for num in line:
        if num == 0:
            continue
        if mergeable == True and num == result[-1]:
            result[-1] += num
            mergeable = False
        else:
            result.append(num)
            mergeable = True
    while len(result) < len(line):
        result.append(0)
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

        self._init_tiles = {}
        self._init_tiles[UP] = [(0, i) for i in range(self._grid_width)]
        self._init_tiles[DOWN] = [(self._grid_height - 1, i) for i in range(self._grid_width)]
        self._init_tiles[LEFT] = [(i, 0) for i in range(self._grid_height)]
        self._init_tiles[RIGHT] = [(i, self._grid_width - 1) for i in range(self._grid_height)]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0] * self._grid_width for dummy_i in range(self._grid_height)]
        self.new_tile(True)
        self.new_tile(True)

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved = False
        direct = OFFSETS[direction]
        print direct, self._init_tiles[direction]
        for init in self._init_tiles[direction]:
            row, col = init[0], init[1]
            line = []
            while row >= 0 and row < self._grid_height and col >= 0 and col < self._grid_width:
                line.append(self.get_tile(row, col))
                row += direct[0]
                col += direct[1]
            merged = merge(line)
            if merged != line:
                row, col = init[0], init[1]
                for num in merged:
                    self.set_tile(row, col, num)
                    row += direct[0]
                    col += direct[1]
                moved = True    
        if moved:
            self.new_tile(False)

    def new_tile(self, init = False):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(self._grid_height)
        col = random.randrange(self._grid_width)
        while(self._grid[row][col] != 0):
            row = random.randrange(self._grid_height)
            col = random.randrange(self._grid_width)
        self.set_tile(row, col, 2 if init or random.random() < .9 else 4)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
