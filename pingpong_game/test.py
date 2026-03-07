from turtle import Screen, Turtle
from paddle import Paddle
import time
import random

screen = Screen()
screen.bgcolor('black')
screen.title("ping pong game")
screen.setup(height=600, width=900)
screen.listen()
screen.tracer(0)



def draw_line():
    pen = Turtle()
    pen.color('white')
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 250)
    pen.pensize(8)
    pen.setheading(270)

    for _ in range(5):
        pen.pendown()
        pen.forward(50)
        pen.penup()
        pen.forward(50)
    

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):

        self.forward(5)

        if self.xcor() > 430 or self.distance(right_paddle.paddle) < 10:
            self.random_angle = random.randint(-30, 30)
            self.setheading(180+self.random_angle)
        elif self.xcor() < -430 or self.distance(left_paddle.paddle) < 10:
            self.setheading(0+self.random_angle)


        
ball = Ball()
draw_line()

screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)

screen.onkey(key='Up', fun=right_paddle.move_up)
screen.onkey(key='Down', fun=right_paddle.move_down)

is_on = True
while is_on:
    screen.update()
    ball.move()
    time.sleep(0.01)





screen.exitonclick()