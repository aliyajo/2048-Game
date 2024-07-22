from grid import Grid
import unittest
'''
    Aliya Jordan
    CS 5001
    Project

This file is to test certain functions of the Grid class.
'''
class Grid_Test(unittest.TestCase):
    def test_restart_game(self):
        cell_locations = [[(-200, 100), (-100, 100), (0, 100), (100, 100)],
                  [(-200, 0), (-100, 0), (0, 0), (100, 0)],
                  [(-200, -100), (-100, -100), (0, -100), (100, -100)],
                  [(-200, -200), (-100, -200), (0, -200), (100, -200)]]
        '''
        Test 1 of the restart_game() function
        It is to just do a normal testing on the function,
        no special circumstances.
        '''
        grid = [[None, None, None, None],
                [None, None, 2, None],
                [None, None, 4, None],
                [None, None, None, None]]
        test1 = Grid(cell_locations, grid)
        grid_result = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test1.restart_game(), grid_result)
        '''
        Test 2 of the restart_game() function
        Again, no special circumstances, just testing
        the function to see if it will accurately restart the game.
        '''
        grid = [[None, 16, None, 2],
                [None, None, 2, None],
                [4, 1024, 4, None],
                [None, None, None, None]]
        test2 = Grid(cell_locations, grid)
        grid_result = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test2.restart_game(), grid_result)
        '''
        Test 3 of the restart_game() function.
        '''
        grid = [[8, 16, 4, 8],
                [4, 32, 2, 8],
                [4, 64, 4, 8],
                [None, 8, None, 16]]
        test3 = Grid(cell_locations, grid)
        grid_result = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]
        self.assertEqual(test3.restart_game(), grid_result)

    def test_checking_game_lose(self):
        cell_locations = [[(-200, 100), (-100, 100), (0, 100), (100, 100)],
                  [(-200, 0), (-100, 0), (0, 0), (100, 0)],
                  [(-200, -100), (-100, -100), (0, -100), (100, -100)],
                  [(-200, -200), (-100, -200), (0, -200), (100, -200)]]
        '''
        Test 1 for testing the checking_game_lose() function
        Normal testing of the function.
        '''
        grid = [[None, None, None, None],
                [None, None, 2, None],
                [None, None, 4, None],
                [None, None, None, None]]
        test1 = Grid(cell_locations, grid)
        self.assertEqual(test1.checking_game_lose(), False)
        '''
        Test 2 for testing the checking_game_lose() function.
        Setting up grid where there are mergable cells even
        if grid is all the way full.
        '''
        grid = [[2, 32, 2, 4],
                [8, 64, 2, 8],
                [16, 128, 4, 16],
                [48, 1024, 32, 64]]
        test2 = Grid(cell_locations, grid)
        self.assertEqual(test2.checking_game_lose(), False)
        '''
        Test 3 for testing the checking_game_lose() function.
        Filling up the grid where there are no mergable cells.
        '''
        grid = [[8, 16, 4, 8],
                [4, 32, 2, 16],
                [8, 64, 4, 8],
                [4, 8, 32, 16]]
        test3 = Grid(cell_locations, grid)
        self.assertEqual(test3.checking_game_lose(), True)
    def test_checking_game_win(self):
        cell_locations = [[(-200, 100), (-100, 100), (0, 100), (100, 100)],
                  [(-200, 0), (-100, 0), (0, 0), (100, 0)],
                  [(-200, -100), (-100, -100), (0, -100), (100, -100)],
                  [(-200, -200), (-100, -200), (0, -200), (100, -200)]]
        '''
        Test 1 for the checking_game_win() fuction.
        Normal testing.
        '''
        grid = [[None, None, None, None],
                [None, None, 2, None],
                [None, None, 4, None],
                [None, None, None, None]]
        test1 = Grid(cell_locations, grid)
        self.assertEqual(test1.checking_game_win(), False)
        '''
        Test 2 for the checking_game_win() function.
        Seeing how it will react with 2048 on the board.
        '''
        grid = [[None, None, None, None],
                [None, None, 2048, None],
                [None, None, 4, None],
                [None, None, None, None]]
        test2 = Grid(cell_locations, grid)
        self.assertEqual(test2.checking_game_win(), True)
def main():
    unittest.main(verbosity=3)

if __name__ == '__main__':
     main()

       
