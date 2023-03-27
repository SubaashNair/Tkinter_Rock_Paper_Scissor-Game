# Tkinter_Rock_Paper_Scissor-Game

This is a simple Rock Paper Scissors game implemented in Python using the Tkinter library. 
The game consists of a graphical user interface where the player can choose Rock, Paper, or Scissors, and the computer generates a random choice. 
The game keeps track of the player's and computer's scores and displays the results.

## Libraries Used

- `tkinter`: Tkinter is the standard Python interface to the Tk GUI toolkit. It is used to create the graphical user interface for the game.
- `random`: The random module is part of the Python Standard Library and is used to generate pseudo-random numbers for various purposes. In this game, it is used to generate the computer's choice.

## Code Explanation

1. Import necessary libraries: `tkinter` for the GUI and `random` for generating the computer's choice.
2. Define the `play` function, which is the main game logic. This function takes the player's choice as an argument, generates the computer's choice, updates the choice labels, and compares the choices to determine the winner.
3. Create the main window using `tk.Tk()` and set its title.
4. Create the choice buttons (Rock, Paper, and Scissors) and pack them into the main window.
5. Create labels for displaying the result, computer's choice, and scores, and pack them into the main window.
6. Initialize the player's and computer's scores.
7. Start the main loop with `root.mainloop()`, which keeps the application running.

## How to Run the Game

To run the Rock Paper Scissors game, follow these steps:

1. Ensure that you have Python installed on your system. This code is compatible with Python 3.6 or later versions.
2. Copy the code into a Python file, e.g., `rock_paper_scissors.py`.
3. Open a terminal or command prompt and navigate to the directory containing the Python file.
4. Run the game by typing `python rock_paper_scissors.py` (or `python3 rock_paper_scissors.py` on some systems) and pressing Enter.

A window will open, displaying the Rock Paper Scissors game interface. Click on the Rock, Paper, or Scissors buttons to make your choice, and the game will automatically update the scores and display the results.
