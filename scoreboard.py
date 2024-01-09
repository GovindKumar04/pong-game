from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(-150, 270)
        self.l_score = 0
        self.r_score = 0
    def score_count(self):
        
        self.write(arg=f"Left Score: {self.l_score}  Right score: {self.r_score}", font=("Arial", 18 , "normal"))
    def l_point(self):
        self.l_score +=1
        
    def r_point(self):
        self.r_score +=1
        

