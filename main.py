"""
Object State and Instanece:
what is Instance ?
when we create a multiple object from a class this is called an Instance.
for Eg:
timmy = Trutle()
tommy= Trutle()
They but are independent from each other .Both can have different attributes and methods
What is State?
Each of them have different attributes and methods and in programming this is known as State.
For eg:
timmy.color() = "green"
tommy.color() ="purple"
so In this case they have different State
"""

import random
from turtle import Turtle, Screen

colors = ["red", "yellow", "green", "orange", "pink", "purple", ]
y_position = [165, 120, 80, 40, 0, -40]
is_race_is_on = False
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)  # this will set a height and width of our screen.
# Now we want to show a dialog to make a bet
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win a race ?Enter your color: ")

'''we have to set position of our turtle'''
for turtle_range in range(0, 6):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.color(colors[turtle_range])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_position[turtle_range])  # this will set a position of our turtle
    all_turtles.append(new_turtle)

if user_bet:
    is_race_is_on = True

while is_race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win a  bet and the winner is {winning_color}")
            else:
                print(f"you loose! winner is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()  # hold a screen
