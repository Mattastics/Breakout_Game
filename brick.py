from turtle import *


class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1.3, stretch_len=9)
        self.penup()
        self.color(color)
        self.goto(position)
        self.speed(0)
