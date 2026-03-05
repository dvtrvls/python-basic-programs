from turtle import *
import random

#create our turtle players
tim = Turtle()
tom = Turtle()
tam = Turtle()

#initialize the state of the turtles

tim.color('red')
tom.color('green')
tam.color('blue')

tim.shape('turtle')
tom.shape('turtle')
tam.shape('turtle')

tim.penup()
tom.penup()
tam.penup()

tim.teleport(-300, 100)
tom.teleport(-300, 0)
tam.teleport(-300, -100)

turtles = {tim.color():tim, tom.color():tom, tam.color():tam}

screen = Screen()
screen.setup(height=400, width=700)
users_bet = screen.textinput(title="make your bet", prompt="what color do you think will win")



def generate_random_walk():
    return random.randint(1, 10)

def draw_finish_line():
    pen = Turtle()
    pen.hideturtle()
    pen.teleport(250, 150)
    pen.setheading(270)
    while True:
        pen.forward(20)
        pen.penup()
        pen.forward(20)
        pen.pendown()
        if pen.position()[1] < -150:
            break

draw_finish_line()

def start_race():

    while True:
        tim.forward(generate_random_walk())
        tom.forward(generate_random_walk())
        tam.forward(generate_random_walk())

        for turtle in turtles.values():
            if turtle.position()[0] >= 250:
                return turtle.color()[0]

winner = start_race()
print(f'{winner} turtle won')
if users_bet == winner:
    print('You win !')
else:
    print('You Lose')



            




screen.mainloop()








