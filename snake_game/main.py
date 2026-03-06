from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, GameOver


screen = Screen()
food = Food()
snake = Snake()
score = ScoreBoard()

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
    snake.move()

    #Check collision with food
    if snake.body_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score() 

    #Check collision with walls
    x, y = snake.body_parts[0].position()
    if x > 230 or x < -230:
        game_over()
        game_is_on = False
    if y > 230 or y < -230:
        game_over()
        game_is_on = False

   #check tail collision
    for body_part in snake.body_parts[1:]:
        if snake.body_parts[0].distance(body_part) < 10:
            game_over()
            game_is_on = False

screen.exitonclick()



