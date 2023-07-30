from turtle import Turtle, Screen

class Lives(Turtle):
    def __init__(self):
        screen = Screen()
        self.full_heart = "full_heart.gif"
        self.empty_heart = "empty_heart.gif"
        screen.addshape(self.empty_heart)
        screen.addshape(self.full_heart)
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-150, 295)
        self.write("Lives:", move=False, align='left', font=('Arial', 25, 'normal'))
        self.lives = []
        self.generating_lives()

    def generating_lives(self):
        for i in range(3):
            heart = Turtle()
            heart.penup()
            heart.shape(self.full_heart)
            heart.goto(-40 + 40 * i, 310)
            self.lives.append(heart)

    def fail(self):
        self.lives[0].shape(self.empty_heart)
        self.lives.pop(0)
