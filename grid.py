import turtle
import random

t = turtle.Turtle()

class Grid:
    '''
    Class Grid
    Attributes: -- both nested lists --
        cell_locations: nested list of cell_coordinates for
        a 4x4 grid that is going to be used by turtle.
        grid: nested list that contains the numbers
        to be drawn by turtle in the grid.
    Methods:
        cell_colors: return dictionary of colors
        drawing_grid: draw a grid based off of cell_locations
        and grid attributes.
        randomize_cell: input either 2 or 4 in a random tile
        using grid attribute.
    '''
    def __init__(self, cell_locations, grid):
        self.cell_locations = cell_locations
        self.grid = grid
        self.value ={
            2: 0,
            4: 4,
            8: 8,
            16: 16,
            32: 32,
            64: 64,
            128: 128,
            256: 256,
            512: 512,
            1024: 1024,
            2048: 2048 }
        t.speed(0)
        t.hideturtle()
        screen = turtle.Screen()
        screen.setup(700, 700)
        screen.bgcolor("powder blue")
        screen.title("2048")
        

    def title():
        '''
        Function/Return: use turtle to write a title
        and instructions on how to restart the game.
        '''
        title = turtle.Turtle()
        title.hideturtle()
        title.goto(-200, 200)
        title.pencolor("dark slate gray")
        title.write("2048", font = ("Arial", 50))
        title.penup()
        title.goto(-200, -220)
        title.write("To restart, "
                    "press r     "
                    "To quit, "
                    "press q", font = ("Arial", 10, "bold"))


    def cell_colors():
        '''
        Function: cell_colors(), helper function
        Parameters: None
        Returns: dictionary of colors for
        different tiles based on corresponding
        numbers.
        '''
        colors = {
            None: "honeydew",
            2: "pale turquoise",
            4: "medium aquamarine",
            8: "dark turquoise",
            16: "medium turquoise",
            32: "medium sea green",
            64: "light sea green",
            128: "cadet blue",
            256: "dark cyan",
            512: "sea green",
            1024: "teal",
            2048: "mint cream" }
        return colors
            
    def drawing_grid(self):
        '''
        Function/return: drawing_grid() the purpose
        is to draw a 4x4 grid based off of the attributes
        of cell locations and grid.
        Uses turtle.
        '''
        colors = Grid.cell_colors()
        for row in range(4):
            for num in range(4):
                x, y = self.cell_locations[row][num]
                number = self.grid[row][num]
                cell_color = colors[number]
                # Go to each cell_location
                t.penup()
                t.goto(x, y)
                t.pencolor("dark slate gray")
                t.width(4)
                t.pendown()
                t.fillcolor(cell_color)
                t.begin_fill()
                # Loop to draw a square
                for n in range(4):
                    t.forward(100)
                    t.left(90)
                t.end_fill()
                t.penup()
                # Once at the coordinate, write corresponding number from grid
                # This conditional is to ensure None isn't printed
                if number:
                    t.goto(x, y)
                    t.forward(50)
                    t.write(number, align = "center", font = ("Arial", 22, "bold"))             

    def randomize_cell(self):
        '''
        Function/return: randomize_cell() the purpose is to
        insert either a 2 or 4 at an open cell in the grid.
        Helper function
        '''
        # Initalizing a list to keep track of the None values
        empty_cells = []
        # Setting up for loop to iterate through grid
        for i in range(len(self.grid)):
            for x in range(len(self.grid[i])):
                # Conditional to look for values of None
                if self.grid[i][x] is None:
                    # If so, add it to the empty_cells list
                    empty_cells.append((i, x))
        # For this appended list, choose a random one
        if empty_cells:
            i, x = random.choice(empty_cells)
            # Once chosen, insert either 2 or 4
            self.grid[i][x] = random.choice([2, 4])
        return self.grid


    def restart_game(self):
        '''
        Function/return: restart_game() the purpose is to
        reinitialize the grid by making all of the values to
        None.
        '''
        # Setting up for loop to iterate through grid
        for i in range(len(self.grid)):
            for x in range(len(self.grid[i])):
                # Making each element in it to None
                self.grid[i][x] = None
        return self.grid

    def get_score(self):
        '''
        Function/return: get_score(), the purpose is to
        keep track of the grid score by using the dictionary
        values.
        '''
        # Initialize the variable score to keep track of
        score = 0
        # Using for loop to iterate through the grid
        for row in self.grid:
            for value in row:
                if value is not None:
                    # iterates through grid and sums numbers up
                    score += self.value[value]
        t.penup()
        t.goto(70, 220)
        t.clear()
        # using turtle to draw out the score
        t.write(f"Score: {score}", font = ("Arial", 20, "bold"))

    def checking_game_lose(self):
        '''
        Function/return: checking_game_lose(), the purpose is to
        check if all of the cells on the grid are full, AND
        are unable to merge to the adjacent cells.
        This will return a boolean on iff the above conditionals
        are True.
        '''
        # Using a for loop to iterate through the grid
        for i in range(len(self.grid)):
            for x in range(len(self.grid[i])):
                if self.grid[i][x] is None:
                    return False
                # Checking if adjacent cells are mergable or not
                if i > 0 and self.grid[i-1][x] == self.grid[i][x]:
                    return False
                if x > 0 and self.grid[i][x-1] == self.grid[i][x]:
                    return False
        return True

    def checking_game_win(self):
        '''
        Function/return: checking_game_win(), the purpose is to check
        the grid on if there is 2048. If there is, then return a boolean
        iff it is True.
        '''
        # Setting up a for loop to iterate through the grid.
        for row in self.grid:
            for element in row:
                if element == 2048:
                    return True
        return False              
