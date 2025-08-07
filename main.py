from turtle import Turtle, Screen

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

screen.update()

game_is_on = True
while game_is_on:
    for segment in snake_segments:
        segment.forward(10)
    screen.update()

screen.exitonclick()