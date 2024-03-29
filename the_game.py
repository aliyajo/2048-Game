import turtle
from grid import Grid
from moving_grid import Moving_Grid
'''
    Aliya Jordan
    CS 5002
    Project

The point of this file is to combine the classes together
in a way that makes them efficient to making the game of 2048.
It also includes the needed parameters.
'''

screen = turtle.Screen()
banner = turtle.Turtle()
turtle.tracer(0)
turtle.speed(0)
Grid.title()

# Global parameters that are to be used throughout functions
cell_locations = [[(-200, 100), (-100, 100), (0, 100), (100, 100)],
                  [(-200, 0), (-100, 0), (0, 0), (100, 0)],
                  [(-200, -100), (-100, -100), (0, -100), (100, -100)],
                  [(-200, -200), (-100, -200), (0, -200), (100, -200)]]
grid = [[None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]]

# Assigning global variables to each function
game_grid = Grid(cell_locations, grid)
moving_game = Moving_Grid(grid)

def shift_left():
    '''
    Function: shift_left(), the purpose of this function
    is to take the combination of classses/functions and
    makes it work for the purpose of shifting the grid
    left, alongside keeping score, drawing the grid,
    random selection of inputting new integer, and
    checking if game lost or won.
    Parameters: None
    Returns: shift_left functionality.
    '''
    global game_grid
    global moving_game
    moving_game.shift_grid_left()
    game_grid.randomize_cell()
    game_grid.get_score()
    game_grid.drawing_grid()
    you_lose()

def shift_right():
    '''
    Function: shift_right(), the purpose of this function
    is to take the combination of classses/functions and
    makes it work for the purpose of shifting the grid
    right, alongside keeping score, drawing the grid,
    random selection of inputting new integer, and
    checking if game lost or won.
    Parameters: None
    Returns: shifting right functionality
    '''
    global game_grid
    global moving_game
    moving_game.shift_grid_right()
    game_grid.randomize_cell()
    game_grid.get_score()
    game_grid.drawing_grid()
    you_lose()

def shift_up():
    '''
    Function: shift_up(), the purpose of this function
    is to take the combination of classses/functions and
    makes it work for the purpose of shifting the grid
    up, alongside keeping score, drawing the grid,
    random selection of inputting new integer, and
    checking if game lost or won.
    Parameters: None
    Returns: shifting up functionality
    '''
    global game_grid
    global moving_game
    moving_game.shift_grid_up()
    game_grid.randomize_cell()
    game_grid.get_score()
    game_grid.drawing_grid()
    you_lose()

def shift_down():
    '''
    Function: shift_down), the purpose of this function
    is to take the combination of classses/functions and
    makes it work for the purpose of shifting the grid
    down, alongside keeping score, drawing the grid,
    random selection of inputting new integer, and
    checking if game lost or won.
    Parameters: None
    Returns: shifting down functionality. 
    '''
    global game_grid
    global moving_game
    moving_game.shift_grid_down()
    game_grid.randomize_cell()
    game_grid.get_score()
    game_grid.drawing_grid()
    you_lose()


def you_lose():
    '''
    Function: you_lose(), the purpose of this function
    is to use the Grid class methods of checking if game
    won or lost, and combine turtle directions
    to display whether game or lost once conditions are met.
    Parameters: None
    Returns: checking if game won/lost.
    '''
    banner.penup()
    banner.pencolor("dark slate gray")
    boolean_lose = game_grid.checking_game_lose()
    boolean_win = game_grid.checking_game_win()
    if boolean_lose is True:
        banner.goto(-170, 0)
        banner.write("YOU LOST", font = ("Arial", 50, "bold"))
        banner.goto(-250, -70)
        banner.write("RESTART GAME", font = ("Arial", 50, "bold"))
    if boolean_win is True:
        banner.goto(-240,0)
        banner.write("YOU WIN..YAY!", font = ("Arial", 50, "bold"))
        banner.goto(-250, -70)
        banner.write("RESTART GAME", font = ("Arial", 50, "bold"))

def restart():
    '''
    Function: restart(), the purpose of this function
    is to take the combination of classses/functions and
    makes it work for the purpose of restarting the game,
    alongside restarting the score, drawing the grid, and
    random selection of inputting new integer.
    Parameters: None
    Returns: restarting the game functionality.
    '''
    global grid
    banner.clear()
    game_grid.restart_game()
    game_grid.get_score()
    game_grid.randomize_cell()
    game_grid.drawing_grid()

def starting_game():
    '''
    Function: starting_game(), the purpose of this function
    is to take the combination of classes/functions and
    start the game to be player ready.
    '''
    game_grid.get_score()
    game_grid.randomize_cell()
    game_grid.drawing_grid()
    turtle.listen()
    turtle.mainloop()
    screen.update()
def exit_game():
    '''
    Function: exit_game(), the purpose of this function
    is to quit the turtle screen. Be paired with a keyboard
    shortcut. 
    '''
    screen.bye()
