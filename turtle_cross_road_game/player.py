from turtle import Turtle



FINISH_LINE =  280
WALK_INCREMENT = 15
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.go_to_starting_position()
    
    def go_to_starting_position(self):
        self.clear()
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.goto(self.xcor(), self.ycor()+WALK_INCREMENT)

    def move_backward(self):
        self.goto(self.xcor(), self.ycor()-WALK_INCREMENT)
             
    def move_left(self):
        self.goto(self.xcor()-WALK_INCREMENT, self.ycor())

    def move_right(self):
        self.goto(self.xcor()+WALK_INCREMENT, self.ycor())

    def is_finish(self):
        return self.ycor() > FINISH_LINE

