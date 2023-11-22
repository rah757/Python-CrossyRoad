from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1,2.5)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250,250))
        self.moveCarToLeft()
    
    def moveCarToLeft(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())
    
    