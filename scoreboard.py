from turtle import Turtle

ALIGNMENT = "Center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 225)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.score = 0
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)
