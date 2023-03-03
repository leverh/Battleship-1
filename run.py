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
        grid[ship_row][ship_column] = 'O'

def get_input():
    while True:
        try:
            guess_row = int(input("Guess row (integer): "))
            guess_column = int(input("Guess Column (integer): "))
            return[guess_row, guess_column]
        except ValueError:
            print("I'm sure you meant to type a number, so please enter a damned number!!")

get_input()

def check_input(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in ships:
        print("Congrats! You've sunk a bloody battleship! How did you do that?!?")
        grid[guess_row][guess_column] = 'X'
        return True
    else:
        print("Pathetic! you've missed!")
