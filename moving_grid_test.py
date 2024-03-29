from moving_grid import Moving_Grid
import unittest
'''
    Aliya Jordan
    CS 5002
    Project

This file is to test the moving_grid class.
'''

class Moving_Grid_Test(unittest.TestCase):
    def test_shift_grid_left(self):
        '''
        Test 1 of the shift_grid_left() function
        It is to look at how it will function normally,
        no special circumstances.
        '''
        grid = [[None, None, None, None],
                [None, None, 2, None],
                [None, None, 4, None],
                [None, None, None, None]]
        test1 = Moving_Grid(grid)
        grid_result = [[None, None, None, None],
                [2, None, None, None],
                [4, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test1.shift_grid_left(), grid_result)
        '''
        Test 2 of the shift_grid_left() function
        It is to look into how it reacts if there are the same
        numbers in a row when shifting left.
        Altered the spacing between the each to see if it will
        accurately merge correctly.
        '''
        grid = [[4, None, 16, 16],
                [None, 2, 2, None],
                [None, None, 4, None],
                [8, None, None, 8]]
        test2 = Moving_Grid(grid)
        grid_result = [[4, 32, None, None],
                [4, None, None, None],
                [4, None, None, None],
                [16, None, None, None]]
        self.assertEqual(test2.shift_grid_left(), grid_result)
        '''
        Test 3 of the shift_grid_left() function
        It is to look into how it reacts if a row is full,
        make sure the order's integrity is kept.
        Also to see if the whole row is filled with the same
        numbers, if it will merge correctly.
        '''
        grid = [[4, 2, 4, 2],
                [None, 2, None, 4],
                [None, None, None, None],
                [8, 8, 8, 8]]
        test3 = Moving_Grid(grid)
        grid_result = [[4, 2, 4, 2],
                [2, 4, None, None],
                [None, None, None, None],
                [16, 16, None, None]]
        self.assertEqual(test3.shift_grid_left(), grid_result)

    def test_shift_grid_right(self):
        '''
        Test 1 of the shift_grid_right() function
        It is to look at how it will functional normally,
        no special circumstances.
        '''
        grid = [[2, None, None, None],
                [None, None, 4, None],
                [None, None, None, None],
                [None, None, None, None]]
        test1 = Moving_Grid(grid)
        grid_result = [[None, None, None, 2],
                [None, None, None, 4],
                [None, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test1.shift_grid_right(), grid_result)
        '''
        Test 2 of the shift_grid_right() function
        It is to look at how numbers will merge
        if they are the same in the row.
        '''
        
        grid = [[2, 2, None, None],
                [None, None, None, None],
                [None, None, 16, None],
                [None, None, 16, None]]
        test2 = Moving_Grid(grid)
        grid_result = [[None, None, None, 4],
                [None, None, None, None],
                [None, None, None, 16],
                [None, None, None, 16]]
        self.assertEqual(test2.shift_grid_right(), grid_result)
        '''
        Test 3 of the shift_grid_right() function
        It is to look at how the function will react
        if multiple mergable numbers are in a row.
        Looks into different spacing when merging.
        '''
        grid = [[2, 2, 2, 2],
                [None, None, None, None],
                [None, 16, None, 16],
                [None, 8, None, 2]]
        test3 = Moving_Grid(grid)
        grid_result = [[None, None, 4, 4],
                [None, None, None, None],
                [None, None, None, 32],
                [None, None, 8, 2]]
        self.assertEqual(test3.shift_grid_right(), grid_result)

    def test_shift_grid_up(self):
        '''
        Test 1 of the shift_grid_up() function
        It is to look at how the function will
        perform normally, no special circumstances.
        '''
        grid = [[None, None, None, None],
                [2, None, None, None],
                [None, None, None, 4],
                [None, None, None, None]]
        test1 = Moving_Grid(grid)
        grid_result = [[2, None, None, 4],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test1.shift_grid_up(), grid_result)
        '''
        Test 2 of the shift_grid_up() function
        It is to look at how the function will perform
        when mergable numbers are aligned together.
        Have different spacing between numbers.
        '''
        grid = [[None, None, 4, 16],
                [2, None, 16, None],
                [2, None, 4, None],
                [None, None, 8, 16]]
        test2 = Moving_Grid(grid)
        grid_result = [[4, None, 4, 32],
                [None, None, 16, None],
                [None, None, 4, None],
                [None, None, 8, None]]
        self.assertEqual(test2.shift_grid_up(), grid_result)
        '''
        Test 3 of the shift_grid_up() function
        It is to look at how the function will perform
        when multiple same numbers in the column.
        '''
        grid = [[None, 2, 8, 2],
                [None, 2, None, 2],
                [None, 16, 8, 2],
                [None, 16, None, 2]]
        test3 = Moving_Grid(grid)
        grid_result = [[None, 4, 16, 4],
                [None, 32, None, 4],
                [None, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test3.shift_grid_up(), grid_result)

    def test_shift_grid_down(self):
        '''
        Test 1 of the shift_grid_down() function
        It is to look at how the function will perform
        normally without any special circumstances.
        '''
        grid = [[None, None, None, None],
                [2, None, None, None],
                [None, None, 8, None],
                [None, None, None, None]]
        test1 = Moving_Grid(grid)
        grid_result = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [2, None, 8, None]]
        self.assertEqual(test1.shift_grid_down(), grid_result)
        '''
        Test 2 of the shift_grid_down() function
        It is going to test the function when
        mergable numbers in the column. Checked
        with different spacing in between.
        '''
        grid = [[2, None, 8, None],
                [None, None, None, 8],
                [None, None, 8, 16],
                [2, None, None, None]]
        test2 = Moving_Grid(grid)
        grid_result = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, 8],
                [4, None, 16, 16]]
        self.assertEqual(test2.shift_grid_down(), grid_result)
        '''
        Test 3 of the shift_grid_down() function
        It is going to test the function when multiple
        mergable numbers in the column.
        '''
        grid = [[None, 16, 8, None],
                [None, 16, None, 2],
                [None, 16, None, 2],
                [None, 16, 4, None]]
        test3 = Moving_Grid(grid)
        grid_result = [[None, None, None, None],
                [None, None, None, None],
                [None, 32, 8, None],
                [None, 32, 4, 4]]
        self.assertEqual(test3.shift_grid_down(), grid_result)

def main():
    unittest.main(verbosity=3)

if __name__ == '__main__':
     main()
