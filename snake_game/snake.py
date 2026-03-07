from turtle import Turtle
INITIAL_LENGTH = 3


class Snake:
    def __init__(self):
        self.body_parts = []
        self.coordinates = []
        self.initial_speed = 15

        for i in range(INITIAL_LENGTH):
            body = self.add_body()
            body.goto(body.xcor() -20 * i, body.ycor())
            self.body_parts.append(body)
            self.coordinates.append((body.xcor(), body.ycor()))

    def move(self):
        for body_part_num in range(len(self.body_parts)-1, 0, -1):
            second_to_last = self.body_parts[body_part_num-1]
            x, y = second_to_last.position()
            self.body_parts[body_part_num].goto(x, y)
        self.body_parts[0].forward(self.initial_speed)

    def up(self):
        if self.body_parts[0].heading() != 270:
            self.body_parts[0].setheading(90)

    def down(self):
        if self.body_parts[0].heading() != 90:
            self.body_parts[0].setheading(270)

    def left(self):
        if self.body_parts[0].heading() != 360:
            self.body_parts[0].setheading(180)

    def right(self):
        if self.body_parts[0].heading() != 180:
            self.body_parts[0].setheading(360)

    def add_body(self):

        body = Turtle(shape='square')
        body.penup()
        body.color('white')
        return body
    def extend(self):
        new_body = self.add_body()
        new_body.goto(self.body_parts[-1].position())
        self.body_parts.append(new_body)
    def update_speed(self):
        self.initial_speed+=1
        

    