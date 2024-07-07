from turtle import Turtle

ALIGNMENT = "Center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 225)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 225)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
