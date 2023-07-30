import random
from turtle import Screen
from Paddle import Paddle
from PongBall import Ball
from turtle import Turtle
import time
from Score import Score

window = Screen()
window.setup(800, 600)
window.bgcolor("black")
window.title("Pong Game")
window.listen()
window.tracer(0)


def generate_table():
    table = Turtle()
    table.hideturtle()
    table.penup()
    table.goto(0, 300)
    table.pensize(7)
    table.color("white")
    table.setheading(270)

    for i in range(6):
        table.pendown()
        table.forward(50)
        table.penup()
        table.forward(50)


def winner_message(z, k):
    message = Turtle()
    message.hideturtle()
    message.penup()
    message.goto(z, 0)
    message.color("yellow")
    message.write(f"Player {k} wins!!!!", False, align="center", font=("Arial", 15, "normal"))


paddle1 = Paddle(-370, 0)
paddle2 = Paddle(370, 0)
ball = Ball()
score1 = Score(-50, 210)
score2 = Score(50, 210)

window.onkey(fun=paddle1.up, key="w")
window.onkey(fun=paddle1.down, key="s")
window.onkey(fun=paddle2.up, key="Up")
window.onkey(fun=paddle2.down, key="Down")

generate_table()


def game():
    play = True
    while play:
        window.update()
        time.sleep(0.01)
        ball.move_ball()

        if ball.xcor() < -350 and ball.distance(paddle1) < 50:
            ball.x = -ball.x + 1
        if ball.xcor() > 350 and ball.distance(paddle2) < 50:
            ball.x = -ball.x - 1

        if ball.position()[0] > 390:
            score1.score += 1
            score1.clear()
            score1.write(score1.score, False, align="center", font=("Arial", 60, "normal"))
            ball.y = random.randint(1, 5)
            ball.center_ball()
            paddle1.goto(-370, 0)
            paddle2.goto(370, 0)
            ball.x = 1
        if ball.position()[0] < -390:
            score2.score += 1
            score2.clear()
            score2.write(score2.score, False, align="center", font=("Arial", 60, "normal"))
            ball.y = random.randint(1, 5)
            ball.center_ball()
            paddle1.goto(-370, 0)
            paddle2.goto(370, 0)
            ball.x = 1

        if ball.position()[1] < -280 or ball.position()[1] > 280:
            ball.y = -ball.y

        if score1.score == 5:
            winner_message(-200, 1)
            play = False
        if score2.score == 5:
            winner_message(200, 2)
            play = False


game()

window.exitonclick()
