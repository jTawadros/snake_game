from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, turtle_list):
        super().__init__()
        self.color("coral")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.move_food(turtle_list)

    def move_food(self, turtle_list):
        bad_position = True
        while bad_position:
            new_x = random.randint(-270, 270)
            new_y = random.randint(-270, 270)
            for i in turtle_list:
                if i.distance(new_x, new_y) < 12:
                    bad_position = True
                    print("food on snake... Trying again")
                    break
                else:
                    bad_position = False

            self.setpos(new_x, new_y)

