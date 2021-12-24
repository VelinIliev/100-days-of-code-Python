import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(30)
def move_backwards():
    tim.backward(30)
def rotate_clockwise():
    heading = tim.heading()
    tim.setheading(heading + 10)
def rotate_counter_clockwise():
    heading = tim.heading()
    tim.setheading(heading - 10)
def clear_drwaing():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "W", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "S", fun = move_backwards)
screen.onkey(key = "d", fun = rotate_clockwise)
screen.onkey(key = "D", fun = rotate_clockwise)
screen.onkey(key = "a", fun = rotate_counter_clockwise)
screen.onkey(key = "A", fun = rotate_counter_clockwise)
screen.onkey(key = "c", fun = clear_drwaing)
screen.onkey(key = "C", fun = clear_drwaing)



screen.exitonclick()