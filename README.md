# Battleships - Python based game

![Screenshot image of the Battleships game terminal on Heroku](/ASSETS/Images/Screenshot%202023-03-22%20at%2011-37-55%20Python%20Terminal%20by%20Code%20Institute.png)

Battleships is a turn based grid game that runs on Heroku, in which the player plays against the computer.

[Click here to play to game on Heroku](https://battleappli.herokuapp.com/).

# Game play

This is a turn-based game of battleships using Python 3. The games lets the human player guess the position of the computer's hidden ships on a 5x5 grid. Similarily, the computer will try to guess the positions of the player's ships. The aim is to eliminate all ships from the board. 

## How to play the game

To start the game, you will need to run the run.py file in your Python supported code editor (I used Visual Studio Code, Gitpod, and Heroku), or simply [click this link](https://battleappli.herokuapp.com/). The game will then start and prompt the player to guess where the computer has its ships on the grid.

## Winning the game

The game will be won once all ships (either the computer's or the player's) have been eliminated.

# The game system

- The game grid is a 5x5 grid, with rows numbered from 1-5 and columns with the letters A-E. Since the code for the grid is pretty straight forward, it should be easy to increase or decrease the grid if I felt that it was needed. 

- At the start of the game, the player's 5 ships are randomly positioned on the grid, and their positions are marked with a capital 'O'. The computer's five ships are also randomly positioned, but their locations are not shown to the player.

- On each turn, the player will enter their guess for a row and column to target. The player will first enter the row number (between 1-5), and then enter the column letter (between A-E). Should the player enter a number or letter that is out of the given range, they will be given an error message requesting them to re-enter their input.

- After the player enters their guess, the computer will also make a guess for a row and column to target. The computer's guess will be randomly generated.

- If the player's guess hits one of the computer's ships, the player will see an 'X' on the computer's grid where the ship was hit. If the player's guess misses, the player will see a 'M' on the computer's grid.

- If the computer's guess hits one of the player's ships, the player will see an 'X' on their own grid where the ship was hit. If the computer's guess misses, the player will see a 'M' on their own grid.

- The game will continue until either all of the computer's ships are sunk (i.e., hit by the player) or all of the player's ships are sunk (i.e., hit by the computer).

- If the player wins, a victory message will be displayed. If the computer wins, a loss message will be displayed.

# Technologies

## Language

- Python 3

## Frameworks, environments, and programs used

- __Gitpod__ 
    - Writing the code and using the terminal to test and play the game
- __Visual Studio Code__
    - Writing the code and using the terminal for testing and manipulating the code
- __GitHub__
    - Version control
- __Heroku__
    - Deployment

## Libraries/ Modules

- [random](https://docs.python.org/3/library/random.html) - Generate pseudo-random numbers 

- [time](https://docs.python.org/3/library/time.html) - Time access and conversions

- [sys](https://docs.python.org/3/library/sys.html) - System-specific parameters and functions

# Features

- A welcome message in the form of the game name made out of ASCII graphics.

- Two grid board of 5x5 - one for the user - and one for the computer. In addition, the characters 'O', 'M', and 'X' to indicate placement of ships, missed hits, and X for position of sunken ships respectively. 

- Allow the player to choose whether they would like to read the instructions for the game:

![screenshot of optional game instructions](/ASSETS/2023-03-23%20(3).png)

- Letting the player know how many turns it took them  or the computer to win:

![screenshot of terminal notifying player how many turns it took for them to win](/ASSETS/2023-03-23%20(2).png)

- Validation in the different stages to make sure the user inputs the correct data type (integars, character, etc.). for exmaple, the instructions require the player to type yes or no- if the wrong or incorrect data type is entered, the user will get an error message as seen in the screenshot below

![screenshot of terminal error message requesting the user to enter the correct data type](/ASSETS/Images/2023-03-23%20(6).png)

- Validation when user enters coordinates for ships and an error message when incorrect data is entered:

![screenshot of terminal error message requesting user to enter the correct data format](/ASSETS/Images/2023-03-23%20(8).png)


# Flowchart of game process

![flowchart graphic of game process](/ASSETS/Images/battleships.png)

# Testing

Every step of the code was tested using: 
- print statements  
- by trying to run the code over and over again until every little bug was fixed. 
- certain processes were also checked on the [Python Tutor](https://pythontutor.com/python-debugger.html#mode=edit) website 
- tests on [Jupyter](https://jupyter.org/) - which i discovered to be very valuable.
- I also used __Visual Studio Code__  (not in GitPod) to check my code and re-write it over and over again. I ended up with 9 versions of the files (run.py, run1.py, run2.py, run3.py etc.)- reduced slowly to 6 with every step of the way and every change I made


I started off with 258 issues found on [CI's Python Linter](https://pep8ci.herokuapp.com/)

![screenshot of validator result](/ASSETS/Images/Screenshot%202023-03-22%20at%2012-03-52%20CI%20Python%20Linter.png)

And the result after having dealt with most issues:

![screenshot of validator result](/ASSETS/Images/Screenshot%202023-03-22%20at%2016-49-54%20CI%20Python%20Linter.png)

The issues that remained on the list are to do with the ASCII graphics and not with the pure code in the editor.

Once these issues were sorted out, and throughout the process of building the game, i ran it and tried to play it multiple times- making sure that every aspect was working as expected and without bugs.


# Future development

- Allowing the player to choose the grid size.
- Connecting the game to a frontend enviornment with proper game graphics.

# Credits

- Code institute Gitpod Template
- [Ozzmaker](https://ozzmaker.com/) - for [Color in Python code](https://ozzmaker.com/add-colour-to-text-in-python/)
- [Patorjk](https://patorjk.com/) - for the ASCII artwork
- [Python 3.11.2 documentation](https://docs.python.org/3/)