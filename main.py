import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carl = Player()

screen.listen()
screen.onkeypress(carl.move, "Up")

cars = []

movementSpeed = 5
speedIncrement = 2

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Spawn car and move
    createCar = random.choice([True, False, False, False])      # Random spawnrate for cars - more false means lesser cars spawned
    if createCar:
        car = CarManager(movementSpeed)
        cars.append(car)
    for car in cars:
        car.moveCarToLeft(movementSpeed)
        
    # Check if car reached finishline
    if carl.ycor() > carl.FINISH_LINE_Y:
        carl.winRound()
        movementSpeed += speedIncrement
        
        
    
        
    
        
        
        