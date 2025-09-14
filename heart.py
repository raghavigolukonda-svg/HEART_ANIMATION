import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.pensize(2)

def heart_curve(t):
    return 12 * (math.sin(t)**3)

def heart_x(t):
    return 16 * (math.sin(t)**3)

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Draw the heart
pen.penup()
pen.goto(0, 200)
pen.pendown()

pen.begin_fill()
pen.color("red")

t = 0
while t <= 2 * math.pi:
    x = 10 * heart_x(t)
    y = 10 * heart_y(t)
    pen.goto(x, y)
    t += 0.01

pen.end_fill()

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("white")
pen.write("When a programmer falls in love ❤", align="center", font=("Arial", 20, "normal"))
pen.hideturtle()
turtle.done()
