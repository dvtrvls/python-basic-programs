from turtle import Turtle

FONT = ("Impact", 20, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.starting_level = 1
        self.goto(-240, 260)
        self.color('black')
        self.write_level()

   
    def write_level(self):
        self.clear()
        self.write(f"Level: {self.starting_level}", font=FONT, align='center')
        
    def update_level(self):
        self.starting_level+=1
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')  
        self.write("GAME OVER", font=FONT, align='center')
      