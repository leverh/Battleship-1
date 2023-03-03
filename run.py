import random


"""
Global Variables:
playground: the size of the game grid
nums_ships: number of ships on the grid
player_ships: a list for player's ships
computer_ships: a list for the computer's ships
computer guesses: to store the position of the computer's guesses
"""
playground = 10
nums_ships = 5
player_ships = []
computer_ships = []
computer_guesses = []

"""
Creating the grid for the game
player_grid: list of list to store player's game grid
computer_grid: list of lists to store the computer's grid
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
Function to initialize the player's game grid with empty spaces - the underscores _
"""


def game_grid():
    for i in range(playground):
        for a in range(playground):
            player_grid[i][a] = '_'


"""
Function to initialize the computers's game grid with underscores
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
Function that randomly positions player's ships on grid and mark the positions with a circle (or rather, a capital O)
"""


def player_position_ships():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        player_ships.append([ship_row, ship_column])
        player_grid[ship_row][ship_column] = 'O'


"""
Function that randomly positions the computer's ships on grid and mark the positions with a circle (or rather, a capital O)
"""


def computer_position_ships():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        computer_ships.append([ship_row, ship_column])
        computer_grid[ship_row][ship_column] = 'O'


"""
Function to prompt the player to enter row and column of choice and return them as a list
list will contain the row and column of guess
"""


def get_player_input():
    while True:
        try:
            guess_row = int(input("Guess row (numbers 1  to 10): "))
            guess_column = int(input("Guess Column (numbers 1  to 10): "))
            return [guess_row - 1, guess_column - 1]
        except ValueError:
            print("Please enter a number between 1 and 10")


"""
Randomly generate the computer's choice in a list of rows and columns.
list will contain the row and column of guess
"""


def computer_guess():
    while True:
        guess_row = random.randint(0, playground - 1)
        guess_column = random.randint(0, playground - 1)
        if [guess_row, guess_column] not in computer_guesses:
            break
    computer_guesses.append([guess_row, guess_column])
    return [guess_row, guess_column]


"""
Function that checks if the player's guess is a hit or a miss and update the game grid
True if the guess is a hit and False otherwise
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


"""
check if the computer's guess is a hit or not and update the game grid
"""


def check_computer_guess(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in player_ships:
        print("Oh noes! The computer has sunk one of your battleships!")
        player_ships.remove([guess_row, guess_column])
        player_grid[guess_row][guess_column] = 'X'


"""
Function to start the main game and alternate turns until player or computer finish sinking all ships
template literals to inform player of state of game and win message
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
            computer_guess_location = computer_guess()
            if not player_ships:
                print(f"The computer sunk all of your ships in {num_guesses} turns! You lose!")
                break
            check_computer_guess(computer_guess_location)
            print((f"The computer guessed row {computer_guess_location[0] + 1} and column {computer_guess_location[1] + 1}."))
        print_grid()


"""
Calling the main game function to start the game
"""


play_game()
