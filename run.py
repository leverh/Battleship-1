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

def game_grid():
    for i in range(playground):
        for a in range(plaground):
            grid[i][a] = '_'

def print_grid():
    for row in grid:
        print(''.join(row))

print_grid()
