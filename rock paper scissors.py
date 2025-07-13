import tkinter as tk
import random

choices = ['rock', 'paper', 'scissors']


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")
root.resizable(False, False)


title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

user_label = tk.Label(root, text="", font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(root, text="", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=5)


root.mainloop()
