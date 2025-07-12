import tkinter as tk
from tkinter import messagebox

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "tie"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissors" and choice2 == "paper"):
        return "friend1"
    else:
        return "friend2"

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.friend1_score = 0
        self.friend2_score = 0

        self.current_player = 1
        self.friend1_choice = ""
        self.friend2_choice = ""

        self.label = tk.Label(root, text="Friend 1: Make your choice!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.rock_btn = tk.Button(self.button_frame, text="Rock", width=10, command=lambda: self.make_choice("rock"))
        self.paper_btn = tk.Button(self.button_frame, text="Paper", width=10, command=lambda: self.make_choice("paper"))
        self.scissors_btn = tk.Button(self.button_frame, text="Scissors", width=10, command=lambda: self.make_choice("scissors"))

        self.rock_btn.grid(row=0, column=0, padx=5)
        self.paper_btn.grid(row=0, column=1, padx=5)
        self.scissors_btn.grid(row=0, column=2, padx=5)

        self.score_label = tk.Label(root, text="Score -> Friend 1: 0 | Friend 2: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.play_again_btn = tk.Button(root, text="Play Again", state=tk.DISABLED, command=self.reset_game)
        self.play_again_btn.pack(pady=5)

    def make_choice(self, choice):
        if self.current_player == 1:
            self.friend1_choice = choice
            self.label.config(text="Friend 2: Make your choice!")
            self.current_player = 2
        else:
            self.friend2_choice = choice
            self.show_result()

    def show_result(self):
        winner = determine_winner(self.friend1_choice, self.friend2_choice)
        result_msg = f"Friend 1 chose: {self.friend1_choice}\nFriend 2 chose: {self.friend2_choice}\n"

        if winner == "tie":
            result_msg += "It's a tie!"
        elif winner == "friend1":
            result_msg += "Friend 1 wins this round!"
            self.friend1_score += 1
        else:
            result_msg += "Friend 2 wins this round!"
            self.friend2_score += 1

        self.score_label.config(text=f"Score -> Friend 1: {self.friend1_score} | Friend 2: {self.friend2_score}")
        messagebox.showinfo("Round Result", result_msg)

        self.play_again_btn.config(state=tk.NORMAL)
        self.disable_buttons()

    def reset_game(self):
        self.current_player = 1
        self.friend1_choice = ""
        self.friend2_choice = ""
        self.label.config(text="Friend 1: Make your choice!")
        self.enable_buttons()
        self.play_again_btn.config(state=tk.DISABLED)

    def disable_buttons(self):
        self.rock_btn.config(state=tk.DISABLED)
        self.paper_btn.config(state=tk.DISABLED)
        self.scissors_btn.config(state=tk.DISABLED)

    def enable_buttons(self):
        self.rock_btn.config(state=tk.NORMAL)
        self.paper_btn.config(state=tk.NORMAL)
        self.scissors_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()


