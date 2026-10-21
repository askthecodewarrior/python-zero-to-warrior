# A grid of dots, one row at a time
import turtle
pen = turtle.Turtle()
turtle.bgcolor("black")
pen.color("gold")
pen.penup()
for row in range(5):
    for col in range(5):
        pen.goto(col * 100 - 200, row * 100 - 200)
        pen.dot(10 + row * 10 + col * 10)

turtle.done()
