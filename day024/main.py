import turtle as t
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard
from border import Border

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
border = Border()

screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()