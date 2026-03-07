from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def speed_up(self):
        if self.move_speed > 0:
            self.move_speed *= 0.90

    def reset_speed(self):
        self.move_speed = 0.1

    def bounce_y(self):
        self.speed_up()
        self.y_move *= -1

    def bounce_x(self):
        self.speed_up()
        self.x_move *= -1

    def left_miss(self):
        self.goto(0, 0)
        self.bounce_x()
        self.reset_speed()
        time.sleep(0.5)

    def right_miss(self):
        self.goto(0, 0)
        self.bounce_x()
        self.reset_speed()
        time.sleep(0.5)