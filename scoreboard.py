from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", font=("Arial", 25, "bold"), align="center")

    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1
