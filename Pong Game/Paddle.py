from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.paddle_position = (x, y)
        self.goto(self.paddle_position)

    def up(self):
        if not self.position()[1] > 230:
            self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        if not self.position()[1] < -230:
            self.goto(self.xcor(), self.ycor() - 30)
