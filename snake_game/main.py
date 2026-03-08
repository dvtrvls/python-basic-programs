from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, GameOver
import time
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import threading

def play_game_over_sound(): 
    playsound("snake_game/anongpoint.mp3")   


def game_over_2():
    global game_is_on
    game_is_on = False

    # close the Turtle window completely
    screen.bye()

    # play sound
    threading.Thread(target=play_game_over_sound).start()
    time.sleep(1)
    # open meme window
    root = tk.Tk()
    root.title("Game Over Meme")

    # center the window on screen
    window_width, window_height = 600, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    img = Image.open("snake_game/sadwolf.jpg")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.pack()

    # keep reference alive
    label.image = tk_img

    root.mainloop()

screen = Screen()
food = Food()
snake = Snake()
score = ScoreBoard()
screen.tracer(0)

def config_screen():
   
    screen.setup(height=500, width=500)
    screen.bgcolor('black')
    screen.title('snake game')
    screen.listen()

#bind keys
screen.onkey(key='Up', fun= snake.up)
screen.onkey(key='Down', fun= snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun= snake.left)

config_screen()
game_is_on = True

def game_over():
    screen.clear()
    config_screen()
    GameOver().game_over(score.score)
    
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #Check collision with food
    if snake.body_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score() 
        snake.update_speed()

    #Check collision with walls
    x, y = snake.body_parts[0].position()
   
   
       
    if y > 230 or y < -230 or  x > 230 or x < -230:
        score.update_high_score()
        snake.snake_reset()
        game_over_2()
        game_is_on = False
        
      
       
   #check tail collision
    for body_part in snake.body_parts[1:]:
        if snake.body_parts[0].distance(body_part) < 10:
            score.update_high_score()
            snake.snake_reset()
            game_over_2()
            game_is_on = False
      
       

screen.exitonclick()

