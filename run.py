import random


"""
Global Variables
"""
playground = 10
nums_ships = 5
player_ships = []
computer_ships = []
computer_guesses = []

"""
Creating the grid for the game
"""
player_grid = []
computer_grid = []
for i in range(playground):
    player_row = []
    computer_row = []
    for a in range(playground):
        player_row.append('-')
        computer_row.append('-')
    player_grid.append(player_row)
    computer_grid.append(computer_row)

"""
Function to start the player's game grid
"""
def game_grid():
    for i in range(playground):
        for a in range(playground):
            player_grid[i][a] = '_'


"""
Function to start the computers's game grid
"""
def computer_game_grid():
    for i in range(playground):
        for a in range(playground):
            computer_grid[i][a] = '_'

"""
Function to print the game grid onto terminal
"""
def print_grid():
    for row in player_grid:
        print(''.join(row))

"""
Function to place the ships on player's grid
"""
def player_position_ships():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        player_ships.append([ship_row, ship_column])
        player_grid[ship_row][ship_column] = 'O'


"""
Function to place ships on the computer's grid
"""
def computer_position_ships(): 
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        computer_ships.append([ship_row, ship_column])
        computer_grid[ship_row][ship_column] = 'O'

"""
Function to get the player's guesses 
"""

def get_player_input():
    while True:
        try:
            guess_row = int(input("Guess row (numbers 1  to 10): "))
            guess_column = int(input("Guess Column (numbers 1  to 10): "))
            return[guess_row - 1, guess_column - 1]
        except ValueError:
            print("I'm sure you meant to type a number, so please enter a damned number!!")


def computer_guess():
    while True:
        guess_row = random.randint(0, playground - 1)
        guess_column = random.randint(0, playground - 1)
        if [guess_row, guess_column] not in computer_guesses:
            break
    computer_guesses.append([guess_row, guess_column])
    return [guess_row, guess_column]

"""
Function that checks if the player's guess is a hit or a miss
"""

def check_player_input(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in computer_ships:
        print("Congrats! You've sunk a bloody battleship! How did you do that?!?")
        computer_ships.remove([guess_row, guess_column])
        player_grid[guess_row][guess_column] = 'X'
        return True
    else:
        print("Pathetic! you've missed!")
        computer_grid[guess_row][guess_column] = 'M'


def check_computer_guess(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in player_ships:
        print("Oh noes! The computer has sunk one of your battleships!")
        player_ships.remove([guess_row, guess_column])
        player_grid[guess_row] [guess_column] = 'X'
        

"""
Function to start the main game and printing using a template literal to inform player of how many moves it took to win the game
"""

def play_game():
    game_grid()
    player_position_ships()
    computer_position_ships()
    print_grid()
    num_guesses = 0
    while True:
        guess = get_player_input()
        num_guesses += 1
        if check_player_input(guess):
            if not computer_ships:
                print(f"It took you {num_guesses} to sink all battleships! you're a genius!")
            break
        else:
            computer_guess = computer_guess()
            check_computer_guess(computer_guess)
            print((f"The computer guessed row {computer_guess[0] + 1} and column {computer_guess[1] + 1}."))
            if not player_ships:
                print(f"The computer sunk all of your ships in {num_guesses}" turns! You lose!)
                break
        print_grid()


"""
Calling the main game function to start the game
"""

play_game()
