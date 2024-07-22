# 2048 Game
This is is my own implementation of the 2048 game, a game originally created by Gabriele Cirulli.

2048 is a single-player puzzle game played on a 4x4 grid. The game starts with two numbers, either 2 or 4, placed randomly on the grid. Players shift all numbers on the grid in one of four directions: up, down, left, or right.

Shift Example: 
    A row with [2, 2, 4] shifted left becomes [4, 4, 0, 0].
  
Merging: When two identical numbers collide, they merge into one cell with their sum.
After each shift, a new number (2 or 4) appears in a random empty cell. 

The goal is to create a tile with the number 2048. The game ends when no moves are possible. The player's score increases with each merge, and the challenge is to reach 2048 with the lowest score.

## How to Install & Run
Must have compiler that able to run Python code. 

Run the *main.py* file.

## How to use the game
In order to move the grid around interactively, use the keyboard functions:
![image](https://github.com/user-attachments/assets/4761aa0b-0ce0-4325-b6f8-f443b9d205aa)

- "Up": Moves the grid upwards
![image](https://github.com/user-attachments/assets/c5e175c0-47ec-4713-a96c-f3003a2ec29b)

- "Down": Moves the grid downards
![image](https://github.com/user-attachments/assets/d01c2d64-2083-4add-9ef3-66cf46fb7328)

- "Left": Moves the grid to the left
![image](https://github.com/user-attachments/assets/d45c2933-b3ba-4e6e-9a84-5ba5829b2cb3)

- "Right": Moves the grid to the right
![image](https://github.com/user-attachments/assets/10ad40aa-1b06-4d99-b194-b41f1bee8691)

- "r": Will restart the game
- "q": Will quit the game

### Features in this game 
- Can use keyboard shortcuts to move game cells around
- Teack record of the score based on the moves players play with keyboard shortcuts
- Different colors for when numbers merge into the new number.

## File Details
The other files in the game are classes for the main functions the game needs for functionality
- **grid.py**

  This file contains the *Grid* class. This class maintains the functionality of the turtle components of the game.

  <a href=https://docs.python.org/3/library/turtle.html>Turtle</a>: Built-in Python library that allows users to create graphics.

- **moving_grid.py**

    This file contains the *Moving_Grid* class. THis class maintains the functionality of being able to manipulate grid parameter.

- **the_game.py**

    This file merges the classes of *Moving_Grid* and *Grid*. These two paired allow the functionality of the 2048 game.

- **main.py**
  This file is the main driver for the game

## Credits
This game was created during CS5001 class @NEU Spring 2023. 
  
