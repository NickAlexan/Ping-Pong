import time
from turtle import Screen
from bat import Bat
from ball import Ball
from scoreboard import Scoreboard

# Bats starting positions L - left, R - Right.
STARTING_POSITION_L = [(-320, -40), (-320, -20), (-320, 0), (-320, 20), (-320, 40)]
STARTING_POSITION_R = [(320, -40), (320, -20), (320, 0), (320, 20), (320, 40)]

# Set up the game screen.
screen = Screen()
screen.setup(700, 500)
screen.tracer(0)

# Create Bats.
bat_l = Bat()  # Left.
bat_l.goto(-336, 0)

bat_r = Bat()  # Right.
bat_r.goto(330, 0)
# bat_r.create_bat(STARTING_POSITION_R)

# Create a Ball.
ball = Ball()

# Create Scoreboard
scoreboard = Scoreboard()

screen.update()

# Bats Control
screen.listen()
screen.onkey(bat_l.up, "w")
screen.onkey(bat_l.down, "s")
screen.onkey(bat_r.up, "Up")
screen.onkey(bat_r.down, "Down")

game_is_on = True

x = 1
y = 1

while game_is_on:
    ball.move(x, y)
    if ball.ycor() > 230:
        y = -1
    if ball.ycor() < -230:
        y = 1
    if ball.distance(bat_r) < 45 and ball.xcor() > 300:
        x = -1
    if ball.distance(bat_l) < 45 and ball.xcor() < -305:
        x = 1

    if ball.xcor() > 355:
        ball.goto(0, 0)
        x = -1
        scoreboard.increase_l_score()
        scoreboard.update_scoreboard()

    if ball.xcor() < -355:
        ball.goto(0, 0)
        x = 1
        scoreboard.increase_r_score()
        scoreboard.update_scoreboard()

    screen.update()
    time.sleep(0.1)


screen.exitonclick()
