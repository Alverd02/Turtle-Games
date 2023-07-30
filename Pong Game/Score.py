from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.score_position = (x, y)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.score_position)
        self.write(f"{self.score}", False, align="center", font=("Arial", 60, "normal"))

