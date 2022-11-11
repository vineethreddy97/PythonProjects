import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
screen.onkey(player.go_up,"Up")
car_manager=CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detect collision with turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()
    # when turtle reaches at finish line
    if player.is_at_finish_line():
        player.starting_point()
        car_manager.level_up()
        scoreboard.increase_level()







screen.exitonclick()