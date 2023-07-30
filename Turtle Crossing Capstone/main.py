import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
Screen().listen()


def board():
    timmy = Turtle()
    timmy.pensize(3)
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(-300, -260)
    timmy.pendown()
    timmy.forward(600)
    timmy.penup()
    timmy.goto(-300, 260)
    timmy.pendown()
    timmy.forward(600)


board()

score = Scoreboard()
tim = Player()
screen.onkey(fun=tim.move, key="w")
cars = []
increment = 0
game_is_on = True
while game_is_on:
    chance = random.randint(0, 4)
    if chance == 1:
        car = CarManager(increment)
        cars.append(car)
    for i in cars:
        i.move()
    time.sleep(0.1)
    screen.update()
    if tim.pos()[1] == 270 and len(cars) > 0:
        score.level_number += 1
        score.clear()
        score.write(f"Level {score.level_number}", align="center", font=("Courier", 24, "normal"))
        increment += 1
        for i in cars:
            i.hideturtle()
        cars.clear()
        tim.goto(0, -280)
    for i in cars:
        if tim.distance(i) < 30 and ((i.ycor() + 10) > tim.ycor() + 10 > (i.ycor() - 10)):
            game_is_on = False
            lose = Turtle()
            lose.hideturtle()
            lose.write("GAME OVER", align="center", font=("Courier", 60, "normal"))

screen.exitonclick()