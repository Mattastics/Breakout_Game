from turtle import *
from paddle import Paddle
from brick import Brick
from ball import Ball
from scorebaord import Scoreboard
import time

VERTICAL_LIMIT = 300
HORIZONTAL_LIMIT = 710
PADDLE_POSITION = (0, -300)
tracer(0, 0)

win = Screen()
win.setup(width=1550, height=750)
win.bgcolor('black')
win.title('Breakout!')

paddle = Paddle(PADDLE_POSITION)
scoreboard = Scoreboard()

# Build Bricks
brick_x_axis = -HORIZONTAL_LIMIT
brick_y_axis = 120

# First Row of Bricks
blue_bricks = []
for j in range(8):
    blue_brick = Brick((brick_x_axis, brick_y_axis), 'blue')
    blue_bricks.append(blue_brick)
    brick_x_axis += 188
brick_x_axis = -HORIZONTAL_LIMIT
brick_y_axis += 40
# Second Row of Bricks
green_bricks = []
for j in range(8):
    green_brick = Brick((brick_x_axis, brick_y_axis), 'green')
    green_bricks.append(green_brick)
    brick_x_axis += 188
brick_x_axis = -HORIZONTAL_LIMIT
brick_y_axis += 40
# Third Row of Bricks
yellow_bricks = []
for j in range(8):
    yellow_brick = Brick((brick_x_axis, brick_y_axis), 'yellow')
    yellow_bricks.append(yellow_brick)
    brick_x_axis += 188
brick_x_axis = - HORIZONTAL_LIMIT
brick_y_axis += 40
# Fourth Row of Bricks
orange_bricks = []
for j in range(8):
    orange_brick = Brick((brick_x_axis, brick_y_axis), 'orange')
    orange_bricks.append(orange_brick)
    brick_x_axis += 188
brick_x_axis = - HORIZONTAL_LIMIT
brick_y_axis += 40
# FifthRow of Bricks
red_bricks = []
for j in range(8):
    red_brick = Brick((brick_x_axis, brick_y_axis), 'red')
    red_bricks.append(red_brick)
    brick_x_axis += 188
brick_x_axis = - HORIZONTAL_LIMIT
brick_y_axis += 40

ball = Ball()

win.listen()

win.onkeypress(paddle.go_right, 'Right')
win.onkeypress(paddle.go_left, 'Left')


def playing():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        win.update()
        ball.move()
        # Ceiling
        if ball.ycor() > VERTICAL_LIMIT:
            ball.bounce_y()
        # Wall
        if ball.xcor() > HORIZONTAL_LIMIT + 30 or ball.xcor() < -HORIZONTAL_LIMIT - 30:
            ball.bounce_x()

        # Paddle
        if ball.distance(paddle) < 110 and ball.ycor() < -270 and paddle.xcor() > ball.xcor() and \
                paddle.xcor() - ball.xcor() > 0:
            ball.paddle_left()
            ball.increase_speed()
            print(paddle.xcor(), ball.xcor(), paddle.xcor()-ball.xcor())

        elif ball.distance(paddle) < 110 and ball.ycor() < -270 and paddle.xcor() > ball.xcor() and \
                paddle.xcor() - ball.xcor() <= 0:
            ball.paddle_right()
            ball.increase_speed()
            print(paddle.xcor(), ball.xcor(), paddle.xcor()-ball.xcor())

        elif ball.distance(paddle) < 110 and ball.ycor() < -270 and paddle.xcor() < ball.xcor():
            ball.paddle_right()
            ball.increase_speed()
            print(paddle.xcor(), ball.xcor(), paddle.xcor()-ball.xcor())

        # Bricks
        for b in blue_bricks:
            if b.ycor() - ball.ycor() <= 30 and ball.distance(b) < 90 or \
                    b.ycor() - ball.ycor() >= 10 and ball.distance(b) < 20:
                b.hideturtle()
                ball.bounce_y()
                blue_bricks.remove(b)
                scoreboard.point()
        for g in green_bricks:
            if g.ycor() - ball.ycor() <= 30 and ball.distance(g) < 100 or \
                    g.ycor() - ball.ycor() >= 10 and ball.distance(g) < 20:
                g.hideturtle()
                ball.bounce_y()
                green_bricks.remove(g)
                scoreboard.point()
        for y in yellow_bricks:
            if y.ycor() - ball.ycor() <= 30 and ball.distance(y) < 100 or \
                    y.ycor() - ball.ycor() >= 10 and ball.distance(y) < 20:
                y.hideturtle()
                ball.bounce_y()
                yellow_bricks.remove(y)
                scoreboard.point()
        for o in orange_bricks:
            if o.ycor() - ball.ycor() <= 30 and ball.distance(o) < 100 or \
                    o.ycor() - ball.ycor() >= 10 and ball.distance(o) < 20:
                o.hideturtle()
                ball.bounce_y()
                orange_bricks.remove(o)
                scoreboard.point()
        for r in red_bricks:
            if r.ycor() - ball.ycor() <= 30 and ball.distance(r) < 100 or \
                    r.ycor() - ball.ycor() >= 10 and ball.distance(r) < 20:
                r.hideturtle()
                ball.bounce_y()
                scoreboard.point()
                red_bricks.remove(r)
                scoreboard.score += 1

        if ball.ycor() < -HORIZONTAL_LIMIT:
            game_is_on = False
        #
        if blue_bricks == [] and green_bricks == [] and yellow_bricks == [] and orange_bricks == [] and red_bricks == []:
            game_is_on = False
        #
        if game_is_on == False and scoreboard.score < 40:
            scoreboard.game_over()
        elif game_is_on == False and scoreboard.score ==40:
            scoreboard.win()

playing()
update()
win.exitonclick()
