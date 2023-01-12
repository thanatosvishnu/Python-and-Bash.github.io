import time
import turtle
import random


screen = turtle.Screen()
user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle are you going to bet?")

COLORS = ["red", "orange", "yellow", "green", "blue"]
DIRECTION = [-110, 40, -75, 0, -40]
players = []
for turtles in range(0, 5):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(COLORS[turtles])
    new_turtle.penup()
    turtle.setup(width=500, height=400)
    new_turtle.goto(x=-230, y=DIRECTION[turtles])
    players.append(new_turtle)

is_game_on = False

if user_bet:
    is_game_on = True

while is_game_on:


    for player in players:
        player.speed("normal")
        if player.xcor() > 230:
            is_game_on = False
            winner = player.pencolor()
            if user_bet == winner:
                turtle.hideturtle()
                turtle.write(f"You won!. The {winner} is the winner", align="center", font=("Arial", 8, "normal"))
            else:
                turtle.hideturtle()
                turtle.write(f"You lost!. The {winner} is the winner", align="center", font=("Arial", 8, "normal"))

        moves = random.randint(0, 10)
        player.forward(moves)

screen.exitonclick()
