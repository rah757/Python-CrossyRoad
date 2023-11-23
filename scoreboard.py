FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto((-275,250))
        self.write(f"Level: {self.level}", font= FONT)
        
    
