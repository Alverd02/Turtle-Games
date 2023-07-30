from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, -310)
        self.score = 0

    def write_score(self):
        self.write(f"Score = {self.score}/50", move=False, align='center', font=('Arial', 25, 'normal'))

    def lose(self):
        self.goto(0, 0)
        self.color("red")
        self.write("You lose!!!", move=False, align='center', font=('Arial', 25, 'normal'))

    def win(self):
        self.goto(0, 0)
        self.color("green")
        self.write("You win!!!", move=False, align='center', font=('Arial', 25, 'normal'))