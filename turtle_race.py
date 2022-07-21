'''
A simple turtle-guessing race game in python
In the beginning of the game, each player must choose the color of the turtle that he/she thinks will win.
Turtles are then being moved forward with random number of steps. The turtle that crosses the line first wins.
The following code is pretty much self-explanatory.
'''


import random
from turtle import Turtle, Screen


is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []
turtle_coordinates = [(-230, -100), (-230, -75), (-230,  -50), (-230, -25), (-230, 0), (-230,  25)]

for i in range(6):
    turtle_list.append(Turtle(shape='turtle'))
    turtle_list[i].penup()
    turtle_list[i].color(colors[i])
    coordinates = turtle_coordinates[i]
    turtle_list[i].goto(x=coordinates[0], y=coordinates[1])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
                break
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner!')
                is_race_on = False
                break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
