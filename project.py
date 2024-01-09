from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800,600)
screen.bgcolor("orange")
screen.title("Pong")
screen.listen()
screen.tracer()

score = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.0001)
    screen.update()
    # ball.speed("slow")
    ball.move()
    score.score_count()
    ball.c_reflection()

    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce()
        ball.move_speed *= 0.001
    if ball.xcor() > 400:
        score.clear()
        score.l_point() 
        ball.refresh()
    if ball.xcor() < -400:
        score.clear()
        score.r_point() 
        ball.refresh()


       
        

    
    
    


screen.exitonclick()
