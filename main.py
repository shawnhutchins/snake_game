from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snak!")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    snake_segments.append(new_segment)

screen.exitonclick()