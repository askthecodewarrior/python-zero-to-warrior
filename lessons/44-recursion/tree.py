# A tree made of smaller trees
import turtle

pen = turtle.Turtle()
turtle.bgcolor("black")
pen.color("gold")
pen.speed(0)
pen.left(90)
pen.teleport(0, -220)


def branch(length):
    if length < 15:
        return
    pen.forward(length)
    pen.left(30)
    branch(length * 0.7)
    pen.right(60)
    branch(length * 0.7)
    pen.left(30)
    pen.backward(length)


branch(150)
turtle.done()
