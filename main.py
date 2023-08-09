from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# create a snake, generates the 3 segment snake at starting positions
snake = Snake()

# create a food
food = Food()

# create scoreboard
scoreboard = Scoreboard()

# when arrow keys are pressed, snake moves in that direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = 0
# while the game is on, the snake moves forwards until a key is pressed to change its direction
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move_snake()
    screen.update()

    # detect collisions with food, when collision occurs: generate new food, increment score, add segment to snake
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.add_snake_segment()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # detect collision with wall
    if snake.collide_with_wall():
        scoreboard.update_high_score()
        scoreboard.reset_scoreboard()

        snake.reset_snake()

    # detect collision with tail
    if snake.collide_with_tail():
        scoreboard.update_high_score()
        scoreboard.reset_scoreboard()
        snake.reset_snake()


screen.exitonclick()
