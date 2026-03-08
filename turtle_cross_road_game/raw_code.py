from turtle import *
import time
import random

screen = Screen()
screen.setup(height=600, width=600)
screen.listen()
screen.tracer(0)
colors = (
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "cyan"
)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.goto(300, random.randint(-260, 260))

    def move_forward(self):
        self.goto(self.xcor()-10, self.ycor())


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-240, 260)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Impact", 20, 'bold'), align='center')
        
    def update_level(self):
        self.level+=1
        self.write_level()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.color('black')
        self.reset()
        
    def move_forward(self):
        self.goto(self.xcor(), self.ycor()+10)
    def move_backward(self):
        self.goto(self.xcor(), self.ycor()-10)
             
    def move_left(self):
        self.goto(self.xcor()-10, self.ycor())
    def move_right(self):
        self.goto(self.xcor()+10, self.ycor())

    def reset(self):
        self.starting_pos = (0, -280)
        self.goto(self.starting_pos)

cars = []
player = Player()
level = Level()
is_on = True

screen.onkey(key='Up', fun=player.move_forward)
screen.onkey(key='Down', fun=player.move_backward)
screen.onkey(key='Left', fun=player.move_left)
screen.onkey(key='Right', fun=player.move_right)
game_speed = 0.1

while  is_on:
    time.sleep(game_speed)
    screen.update()
    if random.randint(1,6) == 1:
        cars.append(Car())

    for car in cars:   # shallow copy
        car.move_forward()
        if car.distance(player) < 20:
            is_on = False
            screen.clear()
            pen = Turtle()
            pen.color('red')
            pen.hideturtle()
            pen.write("GAME OVER", font=("Impact", 20, 'bold'), align='center')

    if player.ycor() > 280:
        player.reset()
        game_speed *= 0.80
        level.update_level()




screen.exitonclick()


