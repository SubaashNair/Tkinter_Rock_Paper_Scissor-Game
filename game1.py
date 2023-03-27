import tkinter as tk
import random

# Define the game logic


def play(player_choice):
    # Generate computer's choice
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    # Update the computer's choice label
    computer_choice_label.config(text=f"Computer chose {computer_choice}")

    # Compare the choices
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text="You win!")
        # Update the player's score
        global player_score
        player_score += 1
        player_score_label.config(text=f"Player: {player_score}")
    else:
        result_label.config(text="Computer wins!")
        # Update the computer's score
        global computer_score
        computer_score += 1
        computer_score_label.config(text=f"Computer: {computer_score}")


# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the choice buttons
rock_button = tk.Button(root, text="Rock", command=lambda: play('Rock'))
rock_button.pack(side=tk.LEFT, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play('Paper'))
paper_button.pack(side=tk.LEFT, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors",
                            command=lambda: play('Scissors'))
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the result label
result_label = tk.Label(root, text="", font=('Arial', 16))
result_label.pack(side=tk.BOTTOM, pady=20)

# Create the computer's choice label
computer_choice_label = tk.Label(root, text="", font=('Arial', 12))
computer_choice_label.pack(side=tk.TOP, pady=10)

# Create the score labels
player_score = 0
computer_score = 0

player_score_label = tk.Label(root, text="Player: 0", font=('Arial', 12))
player_score_label.pack(side=tk.LEFT, padx=10)

computer_score_label = tk.Label(root, text="Computer: 0", font=('Arial', 12))
computer_score_label.pack(side=tk.RIGHT, padx=10)

# Start the main loop
root.mainloop()
