from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.goto(-280, 250)
        self.level = 1
        self.write(arg=f"Level {self.level}", font=FONT)

    def change_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center",  font=FONT)

