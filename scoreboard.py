from turtle import Turtle

SCORE_CORDS = (0, 270)
SCORE_COLOR = "white"
SCORE_FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.goto(SCORE_CORDS)
        self.score = 0

    def show_score(self):
        self.clear()
        self.goto(SCORE_CORDS)
        self.write(f"Score: {self.score}", move=True, align="center", font=SCORE_FONT)

    def increment_score(self):
        self.score += 1

