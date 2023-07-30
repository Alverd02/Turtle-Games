import random
from turtle import Turtle


class Food:
    def __init__(self):
        self.apple_object = []
        self.generate()

    def generate(self):
        apple = Turtle()
        apple.color("red")
        apple.shape("circle")
        apple.pensize(10)
        apple.penup()
        apple.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.apple_object.append(apple)

    def go_to(self):
        self.apple_object[0].goto(random.randint(-280, 280), random.randint(-280, 280))
