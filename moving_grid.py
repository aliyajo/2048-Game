'''
    Aliya Jordan
    CS 5002
    Project

This file is to contain a class that shifts the grid around
that is appropriate to the game 2048.
'''
class Moving_Grid:
    '''
    Class Moving_Grid
    Attributes:
        grid = nested list that is where the numbers for the
        grid are stored.
    Methods:
        shift_grid_left: shift the column of the grid to the left, able
        to merge numbers if they are the same.
        shift_grid_right: shift the column of the grid to the right,
        able to merge numbers if they are the same.
        shift_grid_up: shift the grid rows up, be able to merge if the
        numbers are the same.
        shift_grid_down: shift the grid rows down, be able to merge
        if the numbers are the same.
    '''
    def __init__(self, grid):
        self.grid = grid

    def shift_grid_left(self):
        '''
        Function/return: shift_grid_left(), be able to shift the column
        of a grid to the left. Have the ability to merge numbers if they are
        the same number.
        '''
        for row in range(len(self.grid)):
            # Remove None values, and keep the order of the list
            row_values = [value for value in self.grid[row] if value is not None]
            # Merge the two numbers if they are the same
            i = 0
            # Use a while loop to go through this new list of numbers
            while i < len(row_values) - 1:
                # If the two adjacent indexes are the same, then merge them
                if row_values[i] == row_values[i + 1]:
                    row_values[i] += row_values[i]
                    row_values.pop(i + 1)
                i += 1
            # Add back the None values that were once removed
            row_values += [None] * (len(self.grid[row]) - len(row_values))
            self.grid[row] = row_values
        return self.grid

    def shift_grid_right(self):
        '''
        Function/return: shift_grid_right(), able to shift grid column
        to the right, and able to merge numbers during the shift
        if they are the same numbers.
        '''
        for row in range(len(self.grid)):
            # Remove None values, and keep order of the list
            row_values = [value for value in self.grid[row] if value is not None]
            # Merge two numbers if they are the same using while loop
            i = 0
            while i < len(row_values) - 1:
                # Look at the next number in following index, merge if the same
                if row_values[i] == row_values[i+1]:
                    row_values[i] += row_values[i]
                    row_values.pop(i + 1)
                i += 1
            # Add back any missing None values that were removed
            row_values = [None] * (len(self.grid[row]) - len(row_values)) + \
                         row_values
            self.grid[row] = row_values
        return self.grid

    def shift_grid_up(self):
        '''
        Function/Return: shift_grid_up(), be able to shift grid rows up,
        while shifting upwards, merge the two and leave the sum.
        '''
        # Shifting the grid up
        for col in range(len(self.grid[0])):
            # Remove any None values and keep the order of the list
            col_values = [self.grid[row][col] for row in range(len(self.grid)) if self.grid[row][col] is not None]
            # Merge the two numbers if they are the same using while loop
            i = 0
            while i < len(col_values) - 1:
                # Look at the next number in the following index, merge if the same
                if col_values[i] == col_values[i+1]:
                    col_values[i] += col_values[i]
                    col_values.pop(i+1)
                i += 1
            # Add back any missing None values to the top of the column that were removed
            # Do this with for loop
            for row in range(len(self.grid)):
                if row < len(col_values):
                    self.grid[row][col] = col_values[row]
                else:
                    self.grid[row][col] = None
        return self.grid


    def shift_grid_down(self):
        '''
        Function/return: shift_grid_down(), be able to shift rows down,
        while shifting downwards, merge the two and leave the sum.
        '''
        for j in range(len(self.grid[0])):
            # This loop sstarts from the second-to-last to shift
            for i in range(len(self.grid) - 2, -1, -1):
                # Looking for only numbers with this conditional
                if self.grid[i][j] is not None:
                    k = i
                    while k < len(self.grid) - 1 and (self.grid[k + 1][j] is None or self.grid[k + 1][j] == self.grid[i][j]):
                        k += 1
                    # Conditional to merge the two tiles if they are the same number
                    if k != i and self.grid[k][j] == self.grid[i][j]:
                        self.grid[k][j] *= 2
                        self.grid[i][j] = None
                    # If not same, move them to next available tile
                    elif k != i:
                        self.grid[k][j], self.grid[i][j] = self.grid[i][j], None
        return self.grid
