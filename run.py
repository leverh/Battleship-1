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
        for a in range(playground):
            grid[i][a] = '_'

"""
Function to print the game grid onto terminal
"""
def print_grid():
    for row in grid:
        print(''.join(row))

"""
Function to place the ships on the grid
"""
def position():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        ships.append([ship_row, ship_column])
        grid[ship_row][ship_column] = 'O'


"""
Function to get the player's guesses 
"""

def get_input():
    while True:
        try:
            guess_row = int(input("Guess row (numbers 1  to 10): "))
            guess_column = int(input("Guess Column (numbers 1  to 10): "))
            return[guess_row, guess_column]
        except ValueError:
            print("I'm sure you meant to type a number, so please enter a damned number!!")


"""
Function that checks if the guess is a hit or a miss
"""

def check_input(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in ships:
        print("Congrats! You've sunk a bloody battleship! How did you do that?!?")
        grid[guess_row][guess_column] = 'X'
        return True
    else:
        print("Pathetic! you've missed!")

"""
Function to start the main game and printing using a template literal to inform player of how many moves it took to win the game
"""

def play_game():
    game_grid()
    position()
    print_grid()
    num_guesses = 0
    while True:
        guess = get_input()
        num_guesses += 1
        if check_input(guess):
            print(f"It took you {num_guesses} to sink all battleships! You're a genius!")
            break
        print_grid()


"""
Calling the main game function to start the game
"""

play_game()
