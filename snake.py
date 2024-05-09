from turtle import Turtle


class Snake:
    def __init__(self):
        # List of turtles
        self.t = []
        self.update_snakes(3)
        self.head = self.t[0]

    def update_snakes(self, amount_snakes):
        for i in range(amount_snakes):
            new_t = Turtle(shape="square")
            if not self.t:
                new_t.color("white")
                new_t.penup()
                new_t.setpos(0, 0)
            else:
                new_t.color("white")
                new_t.penup()
                new_t.setpos(self.t[-1].xcor(), self.t[-1].ycor())
            self.t.append(new_t)

    def move(self):
        for i in range(len(self.t) - 1, 0, -1):
            new_x = self.t[i - 1].xcor()
            new_y = self.t[i - 1].ycor()
            self.t[i].setpos(new_x, new_y)
        self.head.fd(20)



    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.seth(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.seth(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.seth(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.seth(0)
