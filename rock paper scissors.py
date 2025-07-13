
import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock Paper Scissors")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f7")  

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 20, "bold"),
            bg="#f0f4f7",
            fg="#2b2d42"
        ).pack(pady=10)

        
        self.score_label = tk.Label(
            self.root,
            text="You: 0 | Computer: 0",
            font=("Arial", 14, "bold"),
            bg="#f0f4f7",
            fg="#1d3557"
        )
        self.score_label.pack(pady=5)

        
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 16, "bold"),
            fg="#e63946",
            bg="#f0f4f7"
        )
        self.result_label.pack(pady=10)

        
        self.choice_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg="#f0f4f7",
            fg="#333"
        )
        self.choice_label.pack(pady=5)

        
        btn_frame = tk.Frame(self.root, bg="#f0f4f7")
        btn_frame.pack(pady=20)

        btn_colors = {
            "Rock": "#ff9f1c",
            "Paper": "#2ec4b6",
            "Scissors": "#e71d36"
        }

        for i, choice in enumerate(self.choices):
            btn = tk.Button(
                btn_frame,
                text=choice,
                font=("Arial", 14),
                width=10,
                bg=btn_colors[choice],
                fg="white",
                activebackground="#ccc",
                command=lambda c=choice: self.play_round(c)
            )
            btn.grid(row=0, column=i, padx=10)

        
        self.play_again_btn = tk.Button(
            self.root,
            text="Play Again",
            font=("Arial", 12, "bold"),
            bg="#457b9d",
            fg="white",
            command=self.reset_game,
            state=tk.DISABLED
        )
        self.play_again_btn.pack(pady=20)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        
        if result == "win":
            self.user_score += 1
            result_text = " You Win!"
            result_color = "#38b000"
        elif result == "lose":
            self.computer_score += 1
            result_text = " You Lose!"
            result_color = "#d00000"
        else:
            result_text = " It's a Draw!"
            result_color ="#ffb703"

        
        self.score_label.config(text=f"You: {self.user_score} | Computer: {self.computer_score}")
        self.result_label.config(text=result_text, fg=result_color)
        self.choice_label.config(
            text=f"You chose: {user_choice} | Computer chose: {computer_choice}"
        )

        self.play_again_btn.config(state=tk.NORMAL)

    def determine_winner(self, user, computer):
        if user == computer:
            return "draw"
        elif (
            (user == "Rock" and computer == "Scissors") or
            (user == "Paper" and computer == "Rock") or
            (user == "Scissors" and computer == "Paper")
        ):
            return "win"
        else:
            return "lose"

    def reset_game(self):
        self.result_label.config(text="", fg="#e63946")
        self.choice_label.config(text="")
        self.play_again_btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
