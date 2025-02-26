import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_cars()

    # Detecting collision with cars
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting if player crossed the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.next_level()
        scoreboard.change_level()

screen.exitonclick()
