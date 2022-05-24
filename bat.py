from turtle import Turtle


class Bat(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def up(self):
            if self.ycor() < 190:
                self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -190:
            self.sety(self.ycor() - 20)
