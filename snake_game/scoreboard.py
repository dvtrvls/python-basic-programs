from turtle import Turtle
ALIGNMENT = 'center'
FONT = 'Monospace'
FONT_SIZE = 18

with open("snake_game/high_score.txt", 'r') as file:
    highest_score = int(file.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = highest_score
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", font=(FONT, FONT_SIZE), align=ALIGNMENT)
    def increase_score(self):
        self.score+=1
        self.update_score()
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open("snake_game/high_score.txt", 'w') as file:
                file.write(str(self.high_score))     
        self.score = 0
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


    

