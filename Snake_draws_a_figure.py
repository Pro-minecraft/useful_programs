import turtle
turtle.bgcolor("green")
square = turtle.Turtle()
square.speed(20)
square.pencolor("black")
for i in range(500):
    square.forward(i)
    square.left(91)
    turtle.Terminator()