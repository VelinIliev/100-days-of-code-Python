import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.create_cars()

    # detect level up
    if player.is_at_finish_line():
        player.start_position()
        scoreboard.level_up()
        car_manager.increase_speed()

    # detect collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20: 
            scoreboard.game_over()
            game_is_on = False
        

screen.exitonclick()

