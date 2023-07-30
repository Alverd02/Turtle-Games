import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 1
        self.y = random.randint(-3, 3)

    def move_ball(self):
        while self.y == 0:
            self.y = random.randint(1, 5)
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def center_ball(self):
        self.goto(0, 0)
        self.x = -self.x
