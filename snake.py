from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_SPEED = 12
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_len=0.6, stretch_wid=0.6)
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def add_tail(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_SPEED)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def is_dead(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        # body_location = self.body_list()
        if self.head.xcor() > 240 or self.head.xcor() < -240 or self.head.ycor() > 240 or self.head.ycor() < -240:
            return True
        else:
            return False
