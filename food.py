from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("coral")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.move_food()

    def move_food(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)
        self.setpos(new_x, new_y)

