from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")

    def move(self, x, y):
        self.setx(self.xcor() + (10 * x))
        self.sety(self.ycor() + (10 * y))
