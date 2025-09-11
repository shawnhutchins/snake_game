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

    def show_score(self):
        self.clear()
        self.goto(SCORE_CORDS)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", move=True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score