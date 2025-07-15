from tkinter import *
import random

class RPSGame:
    def __init__(self, master):
        self.window = master
        self.window.title("Rock Paper Scissors Game - Task 4")
        self.window.geometry("420x530")
        self.window.resizable(False, False)

        self.player_points = 0
        self.computer_points = 0

        self.setup_ui()

    def setup_ui(self):
        Label(self.window, text="ROCK PAPER SCISSORS GAME", font=("Arial", 18, "bold"), fg="brown").pack(pady=15)
        Label(self.window, text="SELECT ONE", font=("Arial", 14, "bold")).pack(pady=5)

        self.choice_frame = Frame(self.window)
        self.choice_frame.pack(pady=10)

        Button(self.choice_frame, text="Rock", width=8, font=("Arial", 12, "bold"),
               bg="yellow", relief="solid", bd=2,
               command=lambda: self.play_round("Rock")).grid(row=0, column=0, padx=10)

        Button(self.choice_frame, text="Paper", width=8, font=("Arial", 12, "bold"),
               bg="yellow", relief="solid", bd=2,
               command=lambda: self.play_round("Paper")).grid(row=0, column=1, padx=10)

        Button(self.choice_frame, text="Scissors", width=8, font=("Arial", 12, "bold"),
               bg="yellow", relief="solid", bd=2,
               command=lambda: self.play_round("Scissors")).grid(row=0, column=2, padx=10)

        self.user_choice_text = Label(self.window, text="Your Choice: ", font=("Arial", 12))
        self.user_choice_text.pack(pady=10)

        self.cpu_choice_text = Label(self.window, text="Computer's Choice: ", font=("Arial", 12))
        self.cpu_choice_text.pack(pady=5)

        self.result_text = Label(self.window, text="", font=("Arial", 14, "bold"), fg="green")
        self.result_text.pack(pady=10)

        self.score_text = Label(self.window, text="Score - You: 0  Computer: 0", font=("Arial", 12), fg="brown")
        self.score_text.pack(pady=10)

        self.play_again_btn = Button(self.window, text="Play Again", font=("Arial", 12),
                                     bg="grey", fg="white", command=self.reset_game)
        self.play_again_btn.pack(pady=10)
        self.play_again_btn.config(state=DISABLED)

        Button(self.window, text="Exit Game", font=("Arial", 12),
               bg="red", fg="white", command=self.window.quit).pack(pady=10)

    def play_round(self, user_pick):
        options = ["Rock", "Paper", "Scissors"]
        comp_pick = random.choice(options)

        self.user_choice_text.config(text=f"Your Choice: {user_pick}")
        self.cpu_choice_text.config(text=f"Computer's Choice: {comp_pick}")

        if user_pick == comp_pick:
            outcome = "It's a Tie!"
        elif (user_pick == "Rock" and comp_pick == "Scissors") or \
             (user_pick == "Paper" and comp_pick == "Rock") or \
             (user_pick == "Scissors" and comp_pick == "Paper"):
            outcome = "You Win!"
            self.player_points += 1
        else:
            outcome = "Computer Wins!"
            self.computer_points += 1

        self.result_text.config(text=outcome)
        self.score_text.config(text=f"Score - You: {self.player_points}  Computer: {self.computer_points}")
        self.play_again_btn.config(state=NORMAL)

    def reset_game(self):
        self.player_points = 0
        self.computer_points = 0
        self.user_choice_text.config(text="Your Choice: ")
        self.cpu_choice_text.config(text="Computer's Choice: ")
        self.result_text.config(text="")
        self.score_text.config(text="Score - You: 0  Computer: 0")
        self.play_again_btn.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    app = RPSGame(root)
    root.mainloop()
