import turtle
import the_game
'''
    Aliya Jordan
    CS 5001
    Project

The purpose of this is to be the main driver for the game 2048.
'''
screen = turtle.Screen()

# Attatching functions established in the_game file
# to keyboard functions 
screen.onkey(the_game.shift_left, "Left")
screen.onkey(the_game.shift_right, "Right")
screen.onkey(the_game.shift_up, "Up")
screen.onkey(the_game.shift_down, "Down")
screen.onkey(the_game.restart, "r")
screen.onkey(the_game.exit_game, "q")

def main():
    the_game.starting_game()
    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    main()
