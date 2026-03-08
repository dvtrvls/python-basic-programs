import time
from turtle import Screen
from player import Player
import random
from car_manager import Car, CarManager
from scoreboard import ScoreBoard
game_speed = 0.1

def update_game_speed():
    global game_speed
    if game_speed > 0.02:   # don’t go below 0.02s
        game_speed *= 0.90
       
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(key='Up', fun=player.move_forward)
screen.onkey(key='Down', fun=player.move_backward)
screen.onkey(key='Left', fun=player.move_left)


is_on = True
car_manager = CarManager()
score_board  = ScoreBoard()

while is_on:
    time.sleep(game_speed)
    screen.update()
    if player.is_finish():
        score_board.update_level()
        player.go_to_starting_position()
        update_game_speed()
        car_manager.make_car_faster()
        
    if random.randint(1, 6) == 1:
        car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_on = False
            screen.clear()
            score_board.game_over()

screen.exitonclick()

