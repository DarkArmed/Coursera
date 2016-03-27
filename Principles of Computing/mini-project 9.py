"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods
    
    def position_tile (self, target_row, target_col, dest_row, dest_col):
        """
        Move target tile to specified position
        """
        pre_move_string = ""
        current_row, current_col = self.current_position(target_row, target_col)
        row, col = dest_row, dest_col

        while row > current_row:
            pre_move_string += "u"
            row -= 1
        while col > current_col:
            pre_move_string += "l"
            col -= 1
        while col < current_col:
            pre_move_string += "r"
            col += 1
        self.update_puzzle(pre_move_string)
        
        move_string =""
        current_row, current_col = self.current_position(target_row, target_col)
        
        if current_row == 0 and (current_col != dest_col or col > current_col):
            if current_col < dest_col:
                move_string += "drurdl"
                col += 1
                current_col += 1
            elif current_col > dest_col:
                move_string += "dluldr"
                col -= 1
                current_col -= 1
            elif col > current_col:
                move_string += "dluld"
                col -= 2
            row += 1
            current_row += 1
        while current_col < dest_col:
            move_string += "urrdl"
            col += 1
            current_col += 1
        while current_col > dest_col:
            move_string += "ulldr"
            col -= 1
            current_col -= 1
        if col > current_col:
            move_string += "ulld"
            col -= 2
        elif col == current_col:
            move_string += "ld"
            row += 1
            col -= 1

        assert col + 1 == current_col, "zero tile position error"
        while current_row < dest_row:
            move_string += "druld"
            current_row += 1
        self.update_puzzle(move_string)
        assert self.current_position(target_row, target_col) == (dest_row, dest_col), "target tile position error" 

        return pre_move_string + move_string

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self._grid[target_row][target_col] != 0:
            return False
        row, col = target_row, target_col + 1
        while row < self._height:
            while col < self._width:
                if self._grid[row][col] != row * self._width + col:
                    return False
                col += 1
            col = 0
            row += 1
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        move_string = self.position_tile(target_row, target_col, target_row, target_col)
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        move_string = "ur"
        self.update_puzzle("ur")
        if self._grid[target_row][0] != target_row * self._width:
            move_string += self.position_tile(target_row, 0, target_row - 1, 1)
            move_string += "ruldrdlurdluurddlur"
            self.update_puzzle("ruldrdlurdluurddlur")
        for dummy_col in range(1, self._width - 1):
            move_string += "r"
            self.update_puzzle("r")
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[0][target_col] != 0:
            return False
        for col in range(target_col + 1, self._width):
            if self._grid[0][col] != col:
                return False
        row, col = 1, target_col
        while row < self._height:
            while col < self._width:
                if self._grid[row][col] != row * self._width + col:
                    return False
                col += 1
            col = 0
            row += 1
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[1][target_col] != 0:
            return False
        row, col = 1, target_col + 1
        while row < self._height:
            while col < self._width:
                if self._grid[row][col] != row * self._width + col:
                    return False
                col += 1
            col = 0
            row += 1
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        move_string = "ld"
        self.update_puzzle("ld")
        if self._grid[0][target_col] != target_col:
            move_string += self.position_tile(0, target_col, 1, target_col - 1)
            move_string += "urdlurrdluldrruld"
            self.update_puzzle("urdlurrdluldrruld")
        return move_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        move_string = self.position_tile(1, target_col, 1, target_col)
        move_string += "ur"
        self.update_puzzle("ur")
        return move_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        if self.current_position(0, 1) == (0, 0):
            move_string = "ul"
        elif self.current_position(0, 1) == (0, 1):
            move_string = "lu"
        else:
            move_string = "uldrul"
        self.update_puzzle(move_string)
        return move_string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        move_string = ""

        for dummy_row in range(self.current_position(0, 0)[0], self._height - 1):
            move_string += "d"
            self.update_puzzle("d")
        for dummy_col in range(self.current_position(0, 0)[1], self._width - 1):
            move_string += "r"
            self.update_puzzle("r")

        for row in range(self._height - 1, 1, -1):
            for col in range(self._width - 1, 0, -1):
                assert self.lower_row_invariant(row, col), "wrong situation"
                move_string += self.solve_interior_tile(row, col)
                assert self.lower_row_invariant(row, col - 1), "wrong situation"
            assert self.lower_row_invariant(row, 0), "wrong situation"
            move_string += self.solve_col0_tile(row)
            assert self.lower_row_invariant(row - 1, self._width - 1), "wrong situation"

        for col in range(self._width - 1, 1, -1):
            assert self.row1_invariant(col), "wrong situation"
            move_string += self.solve_row1_tile(col)
            assert self.row0_invariant(col), "wrong situation"
            move_string += self.solve_row0_tile(col)
            assert self.row1_invariant(col - 1), "wrong situation"
        assert self.row1_invariant(1), "wrong situation"
        move_string += self.solve_2x2()
        assert self.row0_invariant(0), "wrong situation"

        return move_string

# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))


