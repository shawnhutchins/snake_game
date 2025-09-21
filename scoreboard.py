import os.path
from turtle import Turtle

SCORE_CORDS = (0, 270)
SCORE_COLOR = "white"
FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.goto(SCORE_CORDS)
        self.score = 0
        self.highscore = 0
        self.init_highscore()
        self.load_highscore()

    def init_highscore(self):
        if not os.path.exists("highscore.txt"):
            with open("highscore.txt", mode="w") as file:
                file.write("0")

    def load_highscore(self):
        with open("highscore.txt") as file:
            highscore = file.read()
            self.highscore = int(highscore)

    def save_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

    def show_score(self):
        self.clear()
        self.goto(SCORE_CORDS)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", move=True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        self.score = 0
        self.show_score()

    def increment_score(self):
        self.score += 1

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score