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
score = Scoreboard()

screen.listen()
screen.onkeypress(carl.move, "Up")

cars = []

movementSpeed = 5
speedIncrement = 2

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    score.displayScore()
    
    # Spawn car and move
    createCar = random.choice([True, False, False, False])      # Random spawnrate for cars - more false means lesser cars spawned
    if createCar:
        car = CarManager(movementSpeed)
        cars.append(car)
    for car in cars:
        car.moveCarToLeft(movementSpeed)
        if car.distance(carl) < 20:     # Detect car collision
            game_is_on = False
        
    # Check if car reached finishline
    if carl.ycor() > carl.FINISH_LINE_Y:
        carl.winRound()
        score.winRound()
        movementSpeed += speedIncrement
        
    screen.update()
    
# Game ends here, loop is exited. 

screen.clearscreen()    # Screen gets cleared
score.finishGame()    # Update the final score
screen.update()     # Display the final score
time.sleep(3)
    
        
    
        
    
        
        
        