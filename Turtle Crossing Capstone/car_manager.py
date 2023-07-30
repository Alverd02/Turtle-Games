import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle


class CarManager(Turtle):
    def __init__(self, increment=0):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.increment = increment
        super().__init__()
        self.shape("square")
        self.shapesize(1, 3)
        self.penup()
        self.color(random.choice(COLORS))
        self.right(180)
        self.goto(330, random.randint(-250, 250))
    def move(self):
        self.move_distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.increment
        self.forward(self.move_distance)
