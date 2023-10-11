import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(t.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()
    if t.win():
        scoreboard.score()
        car_manager.increase()
        t.start()


    for car in car_manager.all_cars:
        if car.distance(t) < 20 :
            game_is_on = False


screen.exitonclick()