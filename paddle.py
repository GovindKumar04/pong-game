from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,postion):
        super().__init__()
        self.shape("square")
        self.penup()
        
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("navy blue")
        self.goto(postion)
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    
    

    

    