from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.title("ping pong game")
screen.setup(height=600, width=900)
screen.listen()
scoreboard = ScoreBoard()
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


draw_line()  
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
ball.setheading(45)
screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)

screen.onkey(key='Up', fun=right_paddle.move_up)
screen.onkey(key='Down', fun=right_paddle.move_down)

is_on = True
while is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    
    #detect collision with left and right paddles
    if ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(left_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #check if the paddle miss
    if ball.xcor() > 430:
        scoreboard.update_left_score()
        ball.right_miss()

    elif ball.xcor() < -430:
        scoreboard.update_right_score()
        ball.left_miss()





screen.exitonclick()