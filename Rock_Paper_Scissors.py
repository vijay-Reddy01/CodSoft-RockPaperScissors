
import tkinter as tkin
import random
from tkinter import messagebox

class Rock_Paper_Scissor:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissor")
        self.root.geometry("450x350")

        self.player1 = ""
        self.player2 = ""
        self.player1Scr = 0
        self.player2Scr = 0
        self.choices = ["Rock", "Paper", "Scissor"]

        self.createWindow()

    def createWindow(self):
        self.root.configure(bg="light yellow")
        self.name_Frm = tkin.Frame(self.root, bg="light yellow")
        self.name_Frm.pack(pady=20)

        gameLabel=tkin.Label(self.name_Frm, text="ROCK-PAPER-SCISSORS", font=("Algerian", 14), bg="light yellow")
        gameLabel.grid(row=0, column=0, columnspan=2, pady=10)
        
        player1Label=tkin.Label(self.name_Frm, text="Player 1 Name:", font=("Elephant", 10), bg="light yellow")
        player1Label.grid(row=1, column=0, pady=10)
        self.player1data = tkin.Entry(self.name_Frm)
        self.player1data.grid(row=1, column=1)

        player2Label=tkin.Label(self.name_Frm, text="Player 2 Name:", font=("Elephant", 10), bg="light yellow")
        player2Label.grid(row=2, column=0, pady=10)
        self.player2data = tkin.Entry(self.name_Frm)
        self.player2data.grid(row=2, column=1)

        startGameBtn=tkin.Button(self.name_Frm, text="Start Game", command=self.startGame)
        startGameBtn.grid(row=3, column=0, columnspan=2, pady=20)

    def startGame(self):
        self.player1 = self.player1data.get()
        self.player2 = self.player2data.get()

        if not self.player1 or not self.player2:
            messagebox.showwarning("Warning", "Please enter the names.")
            return

        self.name_Frm.pack_forget()
        self.setupGame()

    def setupGame(self):
        self.score_frame = tkin.Frame(self.root, bg="orange")
        self.score_frame.pack(pady=10)

        self.player1_label = tkin.Label(self.score_frame, text=f"{self.player1}: 0", bg="orange", font=("Arial", 12))
        self.player1_label.grid(row=0, column=0, padx=20)

        self.player2_label = tkin.Label(self.score_frame, text=f"{self.player2}: 0", bg="orange", font=("Arial", 12))
        self.player2_label.grid(row=0, column=1, padx=20)

        self.gameFrm = tkin.Frame(self.root, bg="orange")
        self.gameFrm.pack(pady=20)

        self.player1Btn = tkin.Button(self.gameFrm, text="Play Player 1", command=self.playPlayer1Btn, bg="lightblue")
        self.player1Btn.grid(row=1, column=0, padx=20)

        self.player2Btn = tkin.Button(self.gameFrm, text="Play Player 2", command=self.playPlayer2Btn, bg="lightblue")
        self.player2Btn.grid(row=1, column=1, padx=20)

        self.resultBoard = tkin.Label(self.root, text="", bg="orange", font=("Arial", 14))
        self.resultBoard.pack(pady=20)

        self.continueFrm = tkin.Frame(self.root, bg="orange")
        self.continueFrm.pack(pady=10)

    def playPlayer1Btn(self):
        self.player1Option = random.choice(self.choices)
        self.resultBoard.config(text=f"{self.player1} chose {self.player1Option}")
        self.check_both_played()

    def playPlayer2Btn(self):
        self.player2Option = random.choice(self.choices)
        self.resultBoard.config(text=f"{self.player2} chose {self.player2Option}")
        self.check_both_played()

    def check_both_played(self):
        if hasattr(self, 'player1Option') and hasattr(self, 'player2Option'):
            self.determine_winner()

    def determine_winner(self):
        player1Option = self.player1Option
        player2Option = self.player2Option

        if player1Option == player2Option:
            relsult = "It's a tie!"
        elif (player1Option == "Rock" and player2Option == "Scissor") or \
             (player1Option == "Paper" and player2Option == "Rock") or \
             (player1Option == "Scissor" and player2Option == "Paper"):
            relsult = f"{self.player1} won!"
            self.player1Scr += 1
        else:
            relsult = f"{self.player2} won!"
            self.player2Scr += 1

        messagebox.showinfo("Result", relsult)
        self.newScoreBoard()
        self.show_continue_options()

    def newScoreBoard(self):
        self.player1_label.config(text=f"{self.player1}: {self.player1Scr}")
        self.player2_label.config(text=f"{self.player2}: {self.player2Scr}")

    def show_continue_options(self):
        self.continueFrm.pack()
        tkin.Button(self.continueFrm, text="Continue", command=self.continueGame, bg="lightgreen").grid(row=0, column=0, padx=10)
        tkin.Button(self.continueFrm, text="End Game", command=self.end, bg="lightcoral").grid(row=0, column=1, padx=10)

    def continueGame(self):
        self.resultBoard.config(text="")
        self.continueFrm.pack_forget()
        delattr(self, 'player1Option')
        delattr(self, 'player2Option')

    def end(self):
        self.score_frame.pack_forget()
        self.gameFrm.pack_forget()
        self.resultBoard.pack_forget()
        self.continueFrm.pack_forget()
        self.player1Scr = 0
        self.player2Scr = 0
        self.createWindow()

if __name__ == "__main__":
    root = tkin.Tk()
    app = Rock_Paper_Scissor(root)
    root.mainloop()
