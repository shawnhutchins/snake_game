from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snak!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.listen()

game_is_on = True
while game_is_on:
    scoreboard.show_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        scoreboard.update_highscore()
        scoreboard.reset_score()

    #Detect collision with tail using slicing
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.update_highscore()
            scoreboard.reset_score()

screen.exitonclick()