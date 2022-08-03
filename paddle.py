from turtle import Turtle

HORIZONTAL_LIMIT = 680


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('light blue')
        self.turtlesize(.7, 10)
        self.penup()
        self.goto(position)

    def go_right(self):
        if self.xcor() < HORIZONTAL_LIMIT:
            new_x = self.xcor() + 100
            self.goto((new_x, self.ycor()))

    def go_left(self):
        if self.xcor() > -HORIZONTAL_LIMIT:
            new_x = self.xcor() -100
            self.goto((new_x, self.ycor()))
