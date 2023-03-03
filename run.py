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


def position():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        ships.append([ship_row, ship_column])
        grid[ship_row][ship_column] = 'X'

def get_input():
    guess_row = input("Guess row: ")
    guess_column = input("Guess Column: ")
    return[guess_row, guess_column]
