FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.level_number = 1
        super().__init__()
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.write(f"Level {self.level_number}", align="center", font = FONT)