from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def update_left_score(self):
        self.left_score += 1
        self.clear()
        self.write_score()
    def update_right_score(self):
        self.right_score += 1   
        self.clear()
        self.write_score()
    def write_score(self):
        self.goto(-50, 200)
        self.write(self.left_score, align='center', font=("Courier", 50, "bold"))
        self.goto(50, 200)
        self.write(self.right_score, align='center', font=("Courier", 50, "bold"))