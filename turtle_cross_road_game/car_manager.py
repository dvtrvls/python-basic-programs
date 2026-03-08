from turtle import Turtle
import random
SPEED = 10
colors = [
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
]


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
        self.goto(self.xcor()-SPEED, self.ycor())

class CarManager:
    def __init__(self):
        self.all_cars = []
    def create_car(self):
        self.all_cars.append(Car())
    def move_cars(self):
        for car in self.all_cars:
            car.move_forward()
    def make_car_faster(self):
        global SPEED
        SPEED += 3