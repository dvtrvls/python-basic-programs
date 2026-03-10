from turtle import *
import pandas as pd
import time


states_data = pd.read_csv("50_states.csv")

#this way of accessing their coordinates is a risky one because it assumes that the data we have
#is complete and in the right order

data = states_data.state.tolist()
x = states_data.x.tolist()
y = states_data.y.tolist()

state_dict = {}

for i in range(len(data)):
    state_dict[data[i]] = (x[i], y[i])

image = "blank_states_img.gif"
screen = Screen()
screen.title("U.S State Game")
screen.addshape(image)
shape(image)

pen = Turtle()
pen.penup()
pen.hideturtle()

all_state = set(data)
correct_guess = set()

def write_state(name, coordinates):
    pen.goto(coordinates)
    pen.write(name, align="center")

while True:
    #ask for user input
    usr_guess = screen.textinput(f"{len(correct_guess)}/{len(all_state)} ","guess a state: ")
    if usr_guess:
        usr_guess = usr_guess.title()

    #check if it is on the list of statename
    if usr_guess in state_dict.keys():

        coordinates = state_dict[usr_guess]
        #go to location, write the statename
        write_state(usr_guess, coordinates)

        #update how many things got right
        correct_guess.add(usr_guess)

    if usr_guess == "Exit":
        break
    if len(all_state) == len(correct_guess):
        print("LETS GO BABYCAKES !!")
        break

missing_states = all_state - correct_guess
missing_states_df = pd.DataFrame(list(missing_states), columns=['state'])
missing_states_df.to_csv("missing_states.csv", index=False)




screen.exitonclick()



