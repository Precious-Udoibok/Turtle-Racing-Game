#TurtlE RACING GAME
import random
from turtle import Turtle,Screen
my_screen = Screen()


#setting the height and width of your screen
my_screen.setup(500,400)
is_race_on = False
#making a small prompt box
my_choice = my_screen.textinput(title='Make a bet',prompt='Which turtle will win the race.')

#make the turtle to return to a particular position using x and y coordinate
#colors of the turtle
colors = ['red','blue','yellow','green','purple','orange']
all_turtle = []
y =150
for turtle_index in range(6):
    y-=50
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    #get the color of each index in the list
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y)
    all_turtle.append(new_turtle)

if my_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == my_choice:
                print(f'You have won. The {wining_color} turtle is the winner')
            else:
                print(f'You have lost. The {wining_color} turtle is the winner')
        turtle.forward(random.randint(0,10))
my_screen.exitonclick()