#this code was written with a partner

import turtle
import random

# Create a list of player names
players = ['player1', 'player2']

# Create a flag variable to keep track of who wins the race
winner = False

# Create the turtle objects for each player
player1 = turtle.Turtle()
player2 = turtle.Turtle()

# Move player1 to the starting position of the second lane
player1.penup()
player1.goto(100, 400)
player1.pendown()

# Move player2 to the starting position of the second lane
player2.penup()
player2.goto(100, 300)
player2.pendown()

# Set the turtle shape and color for each player
player1.shape('turtle')
player1.color('green')
player2.shape('turtle')
player2.color('blue')

# Create a screen to display the race
screen = turtle.Screen()

# Functions and race logic written by both you and your partner

def car_check(player):
    # First barrier
    if 440 <= player.xcor() <= 450 and player.ycor() >= -249:
        player.penup()
        first = player.xcor()
        second = player.ycor()
        player.goto(first - 50, second + 50)
    # Second barrier
    elif -52 <= player.xcor() <= 251 and -46 <= player.ycor() <= 252:
        player.penup()
        first = player.xcor()
        second = player.ycor()
        player.goto(first - 50, second + 50)
    # Third barrier
    elif -250 <= player.xcor() <= -240 and player.ycor() >= -250:
        player.penup()
        first = player.xcor()
        second = player.ycor()
        player.goto(first + 50, second - 50)
    else:
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-252, -250)
        for i in range(1):
            random_x = random.randint(-200, 200)
            random_y = random.randint(-500, -300)
            turtle.hideturtle()
            turtle.penup()
            turtle.write("Go ", font=("Verdana", 12, "normal"))
            turtle.goto(random_x, random_y)

def TandB_check(player):
    if -250 <= player.xcor() <= 450 and player.ycor() >= 453:
        player.penup()
        first = player.xcor()
        second = player.ycor()
        player.goto(first, second - 50)
    elif -252 <= player.xcor() <= 440 and player.ycor() <= -250:
        player.penup()
        first = player.xcor()
        second = player.ycor()
        player.goto(first, second + 50)

def finshline_check(player):
    if -40 <= player.xcor() <= -30 and player.ycor() >= 250:
        player.penup()
        first = player.xcor()
        second = player.ycor()
        player.goto(first + 10, second)

# Winning screen
def winnnig_screen():
    if -55 <= player1.xcor() <= -45 and player1.ycor() >= 250:
        turtle.hideturtle()
        turtle.goto(0, 0)
        turtle.color('green')

# Create a function to move player 1 forward
def move_player1():
    player1.forward(10)
    car_check(player1)
    TandB_check(player1)
    finshline_check(player1, -40, -30, 250)
    if -55 <= player1.xcor() <= -45 and player1.ycor() >= 250:
        print(f'{players[0]} wins the race!')
        turtle.done()
        turtle.exitonclick()

# Create a function to move player 2 forward
def move_player2():
    player2.forward(10)
    car_check(player2)
    TandB_check(player2)
    finshline_check(player2)
    if -55 <= player2.xcor() <= -45 and player2.ycor() >= 250:
        print(f'{players[1]} wins the race!')
        turtle.done()
        turtle.exitonclick()

# Player 1 controls
def player1_go_up():
    player1.setheading(90)
def player1_go_down():
    player1.setheading(270)
def player1_go_left():
    player1.setheading(180)
def player1_go_right():
    player1.setheading(0)

# Player 2 controls
def player2_go_up():
    player2.setheading(90)
def player2_go_down():
    player2.setheading(270)
def player2_go_left():
    player2.setheading(180)
def player2_go_right():
    player2.setheading(0)

# Key bindings for movement
screen.onkeypress(player1_go_up, 'w')
screen.onkeypress(player1_go_down, 's')
screen.onkeypress(player1_go_left, 'a')
screen.onkeypress(player1_go_right, 'd')
screen.onkeypress(move_player1, 'q')

screen.onkeypress(player2_go_up, 'Up')
screen.onkeypress(player2_go_down, 'Down')
screen.onkeypress(player2_go_left, 'Left')
screen.onkeypress(player2_go_right, 'Right')
screen.onkeypress(move_player2, 'p')

screen.listen()

# Track creation
def box(x, y, f):
    track = turtle.Turtle()
    track.penup()
    track.goto(x, y)
    track.pendown()
    track.width(10)
    for i in range(4):
        track.forward(f)
        track.left(90)

def create_track():
    track = turtle.Turtle()
    track.speed(0)
    track.color('black')
    track.pensize(10)
    box(-250, -250, 700)
    box(-50, -50, 300)

# Sign instructions
def sign():
    sign = turtle.Turtle()
    sign.penup()
    sign.goto(200, 250)
    sign.write('Get to the top in order to accelerate use q for player one and p for two', align='center', font=('Arial', 12, 'normal'))
    sign.hideturtle()

# Calling the function to draw the track
create_track()

# Finish line
turtle.color("green")
turtle.penup()
turtle.goto(-50, 250)
turtle.width(10)
turtle.pendown()
turtle.left(90)
turtle.forward(200)

# Creating crowd
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

people = ["square", "circle", "triangle", "turtle"]

def create_random_shape():
    random_shape = random.choice(people)
    turtle.shape(random_shape)
    random_x = random.randint(-200, 200)
    random_y = random.randint(-500, -300)
    turtle.goto(random_x, random_y)
    turtle.color(random.random(), random.random(), random.random())
    turtle.stamp()

for i in range(10):
    turtle.penup()
    create_random_shape()

# Listen for user input
screen.listen()
screen.mainloop()
