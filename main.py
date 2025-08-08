from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snak!")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    snake_segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_segments) - 1, 0, -1):
        next_segment_pos = snake_segments[seg_num - 1].pos()
        snake_segments[seg_num].goto(next_segment_pos)
    snake_segments[0].forward(20)

screen.exitonclick()