import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed(0)
timmy.screensize(100,100)
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return r, g, b
def draw_spirograph(gap):
    gap = 5
    range_c = int(360 / gap)
    for x in range(range_c):
        timmy.color(random_color())
        current_heading = timmy.heading()
        timmy.setheading(current_heading + gap)
        timmy.circle(100)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()