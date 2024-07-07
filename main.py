from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.turn_right, key="Right")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.add_tail()
        scoreboard.inc_score()
    if snake.is_dead():
        scoreboard.game_over()
        snake.reset()

screen.exitonclick()
