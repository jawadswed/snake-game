from turtle import Turtle
import random
from snake import Snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-225, 225)
        y = random.randint(-225, 225)
        self.goto(x, y)
