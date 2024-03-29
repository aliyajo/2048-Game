2048 Project Breakdown

Instructions:
In order to run this program, just open the main file and run it.

In order to move the grid around interactively, just use the keyboard functions: 
	"Up" to move the grid upwards
	"Down" to move the grid downwards
	"Left" to move the grid left
	"Right" to move the grid right
	"r" to restart the game
	"q" to quit the game

The features in this game include:
 - Ability to use keyboard shortcuts to move game cells around.
	Instructions on hwo to do this are listed above
- Track record of the score based on the moves players play with
  keyboard shortcuts.
- Different colors for when numbers merge into the new number

For my project, I decided to create 2 classes that had
different main functions. 

The files included for this project include:
 - grid.py
 - moving_grid.py
 - main_driver.py

grid.py:
In this file, it contains the class Grid. 
The main point of this class is to deal with the turtle components of 
the game. 
The functions included in this file are--
	* title()
	* cell_colors()
	* drawing_grid()
	* randomize_cell()
	* restart_game()
	* get_score()
	* checking_game_lose()
	* checking_game_win()

moving_grid.py:
In this file, it contains the class Moving_Grid.
The main point of this class is to be able to manipulate the grid parameter. 
The functions in this file are-- 
	* shift_grid_left()
	* shift_grid_right()
	* shift_grid_up()
	* shift_grid_down()

the_game.py:
In this file, it contains multiple functions that's purpose is to combine
the two functions above, in addition to turtle, and make it function 
properly to adhere to 2048 game. 
The functions in this file are--
	* shift_left()
	* shift_right()
	* shift_up()
	* shift_down()
	* you_lose()
	* restart()
	* starting_game()

main.py:
In this file, it is the main driver for the game.




