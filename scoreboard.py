from turtle import Turtle


class ScoreBd(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.setpos(0, 280)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, 'normal'))

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 24, 'normal'))


