import random


"""
Global Variables
"""
playground = 10
nums_ships = 5
ships = []

"""
Creating the grid for the game
"""
grid = []
for i in range(playground):
    row = []
for a in range(playground):
    row.append('-')
grid.append(row)

"""
Function to start the game grid
"""
def game_grid():
    for i in range(playground):
        for a in range(plaground):
            grid[i][a] = '_'

"""
Function to print the game grid onto terminal
"""
def print_grid():
    for row in grid:
        print(''.join(row))


