from turtle import Turtle
import math

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.goto(0,0)
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.01
        # self.speed("slow")
    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x,new_y)
    def c_reflection(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_cor *= -1
    def bounce(self):
        self.x_cor *= -1
        self.move_speed *= 0.001
    # def game_over(self):
    #     if self.xcor() > 360 or self.xcor() < -360:
    #         self.write(arg="Game Over", font=("Arial", 28, "normal"))
    #         return True
    def refresh(self):
        self.move_speed *= 0.9
        self.speed("fastest")
        self.goto(0,0)
        self.x_cor *= -1
        self.y_cor *= -1
    def inc_speed(self):
        self.x_cor *= 1.5
        self.y_cor *= 1.5

        
