import tkinter as tk

# main window

root = tk.Tk()
root.title("Rock Paper Scissors")

# Choice buttons

rock_button = tk.Button(root, text="Rock")
rock_button.pack()

paper_button = tk.Button(root, text='Paper')
paper_button.pack()

scissor_button = tk.Button(root, text='Scissor')
scissor_button.pack()

# label to display
result_label = tk.Label(root, text="")
result_label.pack()

# game function


def play(player_choice):
    computer_choice = "Rock"

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        result_label.config(text="You Win!")
    elif player_choice == "Paper" and computer_choice == "Rock":
        result_label.config(text="You Win!")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        result_label.config(text="You Win!")
    else:
        result_label.config(text="Computer Wins!")

# bind the choice buttons to the 'play' function


rock_button.config(command=lambda: play("Rock"))
paper_button.config(command=lambda: play("Paper"))
scissor_button.config(command=lambda: play("Scissors"))

root.mainloop()
