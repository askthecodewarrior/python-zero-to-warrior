# Practice 3 (boss level, part 2): skip every other dot with continue
import turtle
pen = turtle.Turtle()
turtle.bgcolor("black")
pen.color("gold")
pen.penup()
for row in range(5):
    for col in range(5):
        if (row + col) % 2 == 1:
            continue
        pen.goto(col * 100 - 200, row * 100 - 200)
        pen.dot(10 + row * 10 + col * 10)

turtle.done()
