from turtle import Turtle

class Player:
    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.speed("fastest")
        for player1 in range(3):
            self.player = Turtle("square")
            self.player.color("white")
            self.player.penup()
            self.player.speed("fastest")
            self.player1.append(self.player)
        for player2 in range(3):
            self.player = Turtle("square")
            self.player.color("white")
            self.player.penup()
            self.player.speed("fastest")
            self.player2.append(self.player)
    def postion_player1(self):
        
        self.player1[0].goto(380,20)
        self.player1[1].goto(380,0)
        self.player1[2].goto(380,-20)
    def postion_player2(self):
        self.player2[0].goto(-390,20)
        self.player2[1].goto(-390,0)
        self.player2[2].goto(-390,-20)
    def partion(self):
        self.ball.penup()
        self.ball.goto(0,250)
        self.ball.right(90)
        while self.ball.ycor() != -250:
            self.ball.forward(10)
            self.ball.penup()
            self.ball.forward(10)
            self.ball.pendown()
        self.ball.penup()
        self.ball.goto(0,0)

            
