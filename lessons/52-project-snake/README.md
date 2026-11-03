# Lesson 52: Build a Snake Game in Python (Beginner Project)

Part of **Python: Zero to Warrior**, a free Python course for beginners. A project lesson: a snake game you play with the
arrow keys, built with the turtle module, which comes with Python, so there's nothing to install.
Video: https://youtu.be/bRyRw_Idg6k · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

Run it: `python3 snake.py` on a Mac (`python snake.py` on Windows). Steer with the arrow keys; close the window to quit.

## What's in this lesson
- **Everything on the screen is a turtle.** The snake is a list of square turtles (the first one, `snake[0]`, is the
  head), the food is a circle turtle, and one more hidden turtle, the pen, writes the score and GAME OVER.
- **The window.** `screen = turtle.Screen()` opens it, `title`, `setup(420, 420)` and `bgcolor("black")` set it up, and
  `screen.mainloop()` keeps it open, waiting for key presses and timers, until you close it (lesson 15's `turtle.done()`
  is the same thing). Turtle knows hundreds of color names, like `"gold"` and `"deepskyblue"`.
- **The board.** In turtle, `(0, 0)` is the middle of the window, x goes across and y goes up. A square turtle is 20
  pixels on each side (`CELL = 20`), so the snake moves one square at a time, and the squares on the board go from -200 to
  200 in both directions.
- **The game loop.** `screen.tracer(0)` turns off turtle's own drawing after every change (it would flicker and slow
  down as the snake grows), so `game_loop()` moves the snake, checks what it ran into, redraws the window once with
  `screen.update()`, and then books its own next run with `screen.ontimer(game_loop, DELAY)`: the function itself, with
  no parentheses, `DELAY` milliseconds (120) from now. That's about eight moves a second.
- **The arrow keys.** `screen.listen()` gives the window the keyboard, and `screen.onkey(go_up, "Up")` calls `go_up`
  when you press the up arrow and let go. Each `go_` function changes `direction` (`global direction`, lesson 26), but
  only if the snake isn't going the opposite way, so it can't turn straight back into itself.
- **The food.** `random.randint(-10, 10) * CELL` picks a spot on the board (both ends count), and
  `head.distance(food) < 10` means the head landed on it.
- **Growing.** `grow()` makes a new square on top of the last part (`snake[-1].pos()`) and appends it to the list. In
  `move()`, each part goes to where the part in front of it is, counting DOWN from the tail:
  `for i in range(len(snake) - 1, 0, -1)`, and then the head moves one square.
- **Game over.** `abs(x) > 200 or abs(y) > 200` is a wall; `head.distance(part) < 10` for any `part` in `snake[1:]` is
  the snake's own body. `game_over()` writes GAME OVER and calls `screen.update()` (game_loop stops before its own
  update), and `return` leaves `game_loop` before `ontimer`, so no next move is booked.
- **The score.** `pen.write(...)` writes from the pen's spot to the right; `pen.clear()` erases what the pen wrote, then
  it writes the new score with an f-string.

## The common mistake
Counting UP in the body loop, `for i in range(1, len(snake)):`, moves part 1 onto the head's spot first, then part 2
onto part 1's new spot, which is the head's spot again, and so on. Every part piles onto one square, so the snake stays
two squares long however much it eats. Count down from the tail instead.

## Files
- `snake.py`: the finished game from the video.
- `starter.py`: the game with a TODO in `place_food()` for the YOUR TURN.
- `solution.py`: one way to do the YOUR TURN.
- `speedup.py`, `restart.py`, `wrap.py`: one way to do each practice problem.

## Your turn (from the video)
Right now, `place_food()` can drop the food right on top of the snake's body. Change it so it keeps picking a new spot
while the spot it picked is on any part of the snake. (`solution.py` adds a small `on_snake(x, y)` function and a
`while` loop, lesson 14.)

## Practice problems
1. **Speed it up.** Make the game a little faster every time the snake eats: keep the current delay in a variable that
   starts at `DELAY`, take 5 off it each time the snake eats (but never go under 60), and use it in `ontimer`.
   (`speedup.py`)
2. **Play again.** After GAME OVER, make the space bar start a new game: hide the body parts and remove them from the list
   (`del snake[1:]`), put the head back in the middle going right, reset the score, place the food and start
   `game_loop()` again. Only do it when the game is over, or every space bar press would start a second loop.
   (`restart.py`)
3. **No walls.** Instead of game over at the edge, make the snake come out on the other side: when the head goes past
   200, put it at -200, and the other way around, for x and for y. (`wrap.py`)
