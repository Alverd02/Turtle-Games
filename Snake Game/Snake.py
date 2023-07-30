from turtle import Turtle


class Snake:
    def __init__(self):
        self.high_score = 0
        self.squares = []
        self.snake_body()
        self.find_border = False
        with open("data") as data:
            self.high_score = data.read()
        self.food_eaten = 0
        self.score = 0
        self.score_message = []
        self.write_score()

    def write(self):
        if self.find_border == 1:
            if self.score > int(self.high_score):
                with open("data", "w") as data:
                    self.high_score = self.score
                    data.write(f"{self.high_score}")
                # message = Turtle()
                # message.goto(0, 150)
                # message.write("You lose!!", False, align="center", font=("Arial", 60, "normal"))
            # else:
            #     message = Turtle()
            #     message.goto(0, 150)
            #     message.write("You lose!!", False, align="center", font=("Arial", 60, "normal"))
            self.score = 0

    def write_score(self):
        message = Turtle()
        self.score_message.clear()
        self.score_message.append(message)
        message.penup()
        message.hideturtle()
        message.goto(0, 275)
        message.write(f"Score = {self.score} High Score = {self.high_score}", False, align="center",
                      font=("Arial", 15, "normal"))

    def snake_body(self):
        for i in range(3):
            if i == 0:
                body = Turtle()
                body.color(0, 51, 0)
                body.shape("square")
                body.penup()
                body.goto(0, 0)
                self.squares.append(body)
            else:
                body = Turtle()
                body.color(0, 102, 51)
                body.shape("square")
                body.penup()
                body.goto(-20 * i, 0)
                self.squares.append(body)

    def move(self):
        for j in reversed(range(len(self.squares))):
            if j == 0:
                self.squares[0].forward(20)
                for k in self.squares[1:]:
                    if k.distance(self.squares[0]) < 10:
                        self.find_border = True
                if self.squares[0].xcor() > 295 or self.squares[0].xcor() < -295:
                    self.find_border = True
                elif self.squares[0].ycor() > 295 or self.squares[0].ycor() < -295:
                    self.find_border = True
            else:
                x, y = self.squares[j - 1].position()
                self.squares[j].goto(x, y)

    def more_body(self):
        for i in range(self.food_eaten):
            body = Turtle()
            body.color(0, 102, 51)
            body.shape("square")
            body.penup()
            body.goto(self.squares[-1].position())
            self.squares.append(body)
            self.food_eaten = 0

    def up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)

    def right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)

    def left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)

    def down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)

    def reset(self):
        for i in self.squares:
            i.hideturtle()
        self.squares.clear()
        self.snake_body()
        self.find_border = False
        self.food_eaten = 0
