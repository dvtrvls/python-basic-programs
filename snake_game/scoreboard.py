from turtle import Turtle
ALIGNMENT = 'center'
FONT = 'Monospace'
FONT_SIZE = 25

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", font=(FONT, FONT_SIZE), align=ALIGNMENT)
    def increase_score(self):
        self.score+=1
        self.update_score()

class GameOver(Turtle):
     
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('red')
        self.penup()
        self.hideturtle()
    def game_over(self, final_score):
        self.write(arg=f"GAME OVER!\n final score: {final_score}", font=(FONT, 10), align=ALIGNMENT)


    

