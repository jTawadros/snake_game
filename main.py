from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBd
import time


screen = Screen()
screen.title("Snake")
screen.tracer(0)
screen.bgcolor("black")
screen.setup(600, 600)

snake = Snake()
food = Food(snake.t)
score = ScoreBd()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.head) < 14:
        food.move_food(snake.t)
        snake.update_snakes(1)
        score.update_score()
        time.sleep(0.2)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    for i in snake.t[1:]:
        if snake.head.distance(i) < 10:
            score.game_over()
            game_is_on = False


screen.exitonclick()
