import random
import time
import sys

"""
To creates a slow typing effect
"""


def type_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


"""
To create a faster typing effect
"""


def type_faster(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


"""
Battleship ASCII pattern using -
"""


def print_ascii_art():
    print("\033[95m ____        _   _   _           _     _           \033[0m")
    print("\033[95m|  _ \      | | | | | |         | |   (_)          \033[0m")
    print("\033[95m| |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___\033[0m")
    print("\033[95m|  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|\033[0m")
    print("\033[95m| |_) | (_| | |_| |_| |  __/\__ \ | | | "
          "| |_) \__ \\\033[0m")
    print("\033[95m|____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/\033[0m")
    print("\033[95m                                         | |        "
          "\033[0m")
    print("\033[95m                                         |_|        "
          "\033[0m")


"""
Global Variables:
playground: the size of the game grid
nums_ships: number of ships on the grid
player_ships: a list for player's ships
computer_ships: a list for the computer's ships
computer guesses: to store the position of the computer's guesses
col_numbers: a dictionary to translate the column coordinates into numbers
"""


playground = 5
nums_ships = 5
player_ships = []
computer_ships = []
computer_guesses = []
col_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4
}


"""
Creating the grid for the game
player_grid: list of lists to store player's game grid
computer_grid_hidden_ships: list of lists to show where
the player hit or missed
"""


player_grid = []
computer_grid_hidden_ships = []
for i in range(playground):
    player_row = []
    computer_row_hidden_ships = []
    for a in range(playground):
        player_row.append('_')
        computer_row_hidden_ships.append('_')
    player_grid.append(player_row)
    computer_grid_hidden_ships.append(computer_row_hidden_ships)


"""
Function to print game grids onto terminal
"""


def print_grid():
    print("Your grid:        Computer's grid:")
    print("  A B C D E           A B C D E")
    for i in range(playground):
        print(str(i + 1) + '|' + '|'.join(player_grid[i]) + '|        ' +
              str(i + 1) + '|' + '|'.join(computer_grid_hidden_ships[i]) + '|')


"""
Function that randomly positions player's ships on grid
and mark the positions with a circle (or rather, a capital O)
"""


def player_position_ships():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        player_ships.append([ship_row, ship_column])
        player_grid[ship_row][ship_column] = 'O'


"""
Function that randomly positions the computer's ships on grid
and mark the positions with a circle (or rather, a capital O)
"""


def computer_position_ships():
    for i in range(nums_ships):
        ship_row = random.randint(0, playground - 1)
        ship_column = random.randint(0, playground - 1)
        computer_ships.append([ship_row, ship_column])


"""
Function to prompt the player to enter row and
column of choice and return them as a list
list will contain the row and column of guess
"""


def get_player_input():
    while True:
        try:
            guess_row = int(input("Please guess row (numbers 1  to 5): \n"))
            if guess_row < 1 or guess_row > 5:
                print("Your chosen numbers were out"
                      " of the specified range (1-5) \n")
            else:
                break
        except ValueError:
            print("Your chosen numbers were out of the specified range 1-5 \n")
    while True:
        try:
            column = input("Please guess column (letters A-E): \n").upper()
            if column not in 'ABCDE':
                print("Your chosen letter was out of"
                      " the specified range (A-E) \n")
            else:
                guess_column = col_numbers[column]
                break
        except KeyError:
            print("Your chosen letter was out of the specified range (A-E) \n")
    return [guess_row - 1, guess_column]


"""
Randomly generate the computer's choice in a
list of rows and columns.list will contain the
row and column of guess
"""


def computer_guess():
    while True:
        guess_row = random.randint(0, playground - 1)
        guess_column = random.randint(0, playground - 1)
        # See if the computer guessed these positions before,
        # if not then it can try out these positions
        if [guess_row, guess_column] not in computer_guesses:
            break
    computer_guesses.append([guess_row, guess_column])
    return [guess_row, guess_column]


"""
Function that checks if the player's guess is
a hit or a miss and update the game grid
True if the guess is a hit and False otherwise
"""


def check_player_input(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in computer_ships:
        print("Congrats! You've sunk a bloody battleship!"
              " How did you do that?!? \n")
        computer_ships.remove([guess_row, guess_column])
        computer_grid_hidden_ships[guess_row][guess_column] = 'X'
        return True
    else:
        print("Pathetic! You've missed! \n")
        computer_grid_hidden_ships[guess_row][guess_column] = 'M'


"""
check if the computer's guess is a hit or not
and update the game grid
"""


def check_computer_guess(guess):
    guess_row, guess_column = guess
    if [guess_row, guess_column] in player_ships:
        print("Oh noes! The computer has sunk one of your battleships! \n")
        player_ships.remove([guess_row, guess_column])
        player_grid[guess_row][guess_column] = 'X'
    else:
        print("Lucky! The computer missed! \n")
        player_grid[guess_row][guess_column] = 'M'


"""
Function containing game instructions
"""


def print_instructions():
    type_faster("To win the game, you need to sink all"
                " of the computer's battleships. \n\n")
    type_faster("Unfortunately for you, you don't exactly know"
                " where the ships are hidden on its grid. \n\n")
    type_faster("You will need to guess and destroy all the ships")
    type_faster(" as quickly as possible... \n\n")
    type_faster("Hurry, because while you are attacking its"
                " ships, yours are also being attacked! \n\n")
    type_faster("Good luck! \n\n")


"""
Function to start the main game and alternate
turns until player or computer finish sinking all ships
template literals to inform player of state of game and win message
"""


def play_game():
    player_position_ships()
    computer_position_ships()
    print_grid()
    num_guesses = 0
    while True:
        guess = get_player_input()
        num_guesses += 1
        if check_player_input(guess):
            if not computer_ships:
                print(f"It took you {num_guesses} turns to sink all  "
                      f"battleships! you're a genius!")
                break
        else:
            computer_guess_location = computer_guess()
            check_computer_guess(computer_guess_location)
            if not player_ships:
                print(f"The computer sunk all of your ships in {num_guesses} "
                      f"turns! You lose!")
                break
            print(f"The computer guessed row {computer_guess_location[0] + 1} "
                  f"and column {computer_guess_location[1] + 1}")
        print_grid()


"""
Calling: 1. The ASCII function to print name of game
         2. The prompt to ask player whether they would
         like the instructions for the game
         3. The main game function to start the game
"""


print_ascii_art()
type_slow("\033[1;35;40m WELCOME TO THE GAME OF YOUR LIFE! \n\n\n")

while True:
    instructions_prompt = input("Would you like to read the game"
                                " instructions? (yes or no): \n")
    if instructions_prompt.lower() == 'yes':
        print_instructions()
        break
    elif instructions_prompt.lower() == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
play_game()
