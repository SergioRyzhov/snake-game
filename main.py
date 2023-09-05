import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

SPEED_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED_TIME)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall x
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.reverse_x()

    # Detect collision with wall y
    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reverse_y()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
