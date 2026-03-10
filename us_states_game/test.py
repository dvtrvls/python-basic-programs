from turtle import *
import pandas as pd

states_data = pd.read_csv("50_states.csv")
data = states_data.state.tolist()
x = states_data.x.tolist()
y = states_data.y.tolist()

state_dict = {}

for i in range(len(data)):
    state_dict[data[i]] = (x[i], y[i])

def write_state(name, coordinate):
    print(f"go to {name} located in {coordinate}")


all_state = set(data)
correct_guess = set()

while True:
    print(f"{len(correct_guess)}/{len(all_state)} guessed correctly")
    print(f"{len(all_state.union(correct_guess)) - len(all_state.intersection(correct_guess))} states to go")
    usr_guess = input("guess a state: ").title()
    if usr_guess in state_dict.keys():      
        coordinates = state_dict[usr_guess]
        write_state(usr_guess, coordinates)
        correct_guess.add(usr_guess)
    else:
        print("that shi aint a us state bro. what drugs r u taking")

    if len(all_state) == len(correct_guess):
        print("LETS GO BABYCAKES !!")
        break








