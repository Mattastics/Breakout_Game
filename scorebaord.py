from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 300)
        self.write(self.score, align='center', font =('Courier', 40, 'normal'))

    def point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'   GAME OVER\nYou scored {self.score} points', align='center', font=('Courier', 40, 'normal'))

    def win(self):
        self.go(0, 0)
        self.write('YOU WIN!', align='center', font=('Courier', 40, 'normal'))


