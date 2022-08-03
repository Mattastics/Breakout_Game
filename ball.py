from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, -270)
        self.x_move = 12
        self.y_move = 12
        self.move_speed = .08
        self.turtlesize(1.2)



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.move_speed *= .99

    def ball_speed(self):
        return self.speed

    def paddle_left(self):
        self.y_move *= -1
        self.x_move *= 1

    def paddle_right(self):
        self.y_move *= -1
        self.x_move *= -1

    def paddle_center(self):
        self.y_move *= 1
        self.x_move *= 0