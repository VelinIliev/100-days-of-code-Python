from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color("coral")

angles = 3
color = ["red", "black", "orange", "yellow", "pink", "green", "brown", "grey"]

while angles < 10:
    random_color = random.choice(color)
    for _ in range(angles):
        
        timmy.color(random_color)
        timmy.forward(100)
        timmy.left(360/angles)
    angles +=1

screen = Screen()
screen.exitonclick()