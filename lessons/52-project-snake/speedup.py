# Practice 1 (lesson 52): the snake speeds up every time it eats
import random
import turtle

CELL = 20
DELAY = 120
FONT = ("Courier", 18, "bold")

screen = turtle.Screen()
screen.title("Snake")
screen.setup(420, 420)
screen.bgcolor("black")
screen.tracer(0)

head = turtle.Turtle("square")
head.color("gold")
head.penup()
snake = [head]
direction = "right"

food = turtle.Turtle("circle")
food.color("deepskyblue")
food.penup()
food.goto(100, 0)

score = 0
delay = DELAY
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(-200, 180)
pen.write("Score: 0", font=FONT)


def go_up():
    global direction
    if direction != "down":
        direction = "up"


def go_down():
    global direction
    if direction != "up":
        direction = "down"


def go_left():
    global direction
    if direction != "right":
        direction = "left"


def go_right():
    global direction
    if direction != "left":
        direction = "right"


def move():
    for i in range(len(snake) - 1, 0, -1):
        snake[i].goto(snake[i - 1].pos())
    if direction == "up":
        head.sety(head.ycor() + CELL)
    elif direction == "down":
        head.sety(head.ycor() - CELL)
    elif direction == "left":
        head.setx(head.xcor() - CELL)
    elif direction == "right":
        head.setx(head.xcor() + CELL)


def place_food():
    x = random.randint(-10, 10) * CELL
    y = random.randint(-10, 10) * CELL
    food.goto(x, y)


def grow():
    part = turtle.Turtle("square")
    part.color("goldenrod")
    part.penup()
    part.goto(snake[-1].pos())
    snake.append(part)


def game_over():
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=FONT)
    screen.update()


def game_loop():
    global score, delay
    move()
    x = head.xcor()
    y = head.ycor()
    if abs(x) > 200 or abs(y) > 200:
        game_over()
        return
    for part in snake[1:]:
        if head.distance(part) < 10:
            game_over()
            return
    if head.distance(food) < 10:
        place_food()
        grow()
        score += 1
        delay = max(60, delay - 5)
        pen.clear()
        pen.write(f"Score: {score}", font=FONT)
    screen.update()
    screen.ontimer(game_loop, delay)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
game_loop()
screen.mainloop()
