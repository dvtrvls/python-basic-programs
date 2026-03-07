from turtle import Turtle

class Paddle():
    def __init__(self, x_loc, y_loc):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_loc, y_loc)
    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+50) 
    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()-50) 
    


