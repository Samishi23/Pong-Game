from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounceX()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()