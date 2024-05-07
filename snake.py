from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.t = []
        self.create_snake()
        self.head = self.t[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            temp = Turtle(shape="square")
            temp.penup()
            temp.color("white")
            temp.setpos(i)
            self.t.append(temp)

    def move(self):
        for pos in range(len(STARTING_POSITION) - 1, 0, -1):
            new_x = self.t[pos - 1].xcor()
            new_y = self.t[pos - 1].ycor()
            self.t[pos].setpos(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
