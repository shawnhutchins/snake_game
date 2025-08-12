from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            next_segment_pos = self.snake_segments[seg_num - 1].pos()
            self.snake_segments[seg_num].goto(next_segment_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
