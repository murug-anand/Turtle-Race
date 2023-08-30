from turtle import Turtle, Screen
import random

s = Screen()
line = Turtle()
m = Turtle()
line.color("white")
line.pencolor("black")
colors = ["blue", "red", "green", "orange", "brown", "black"]
s.setup(width=500, height=400)
bet = s.textinput(title="enter you bet", prompt="on which turtle u gonna bet \nblue, red, green, orange, brown, black")

y = [-70, -40, -10, 20, 50, 80]
race_is_on = False
turtles = []
for f in range(0, 6):
    t = Turtle("turtle")
    t.color(colors[f])
    t.penup()
    t.goto(-240, y[f])
    turtles.append(t)

line.pencolor("silver")
line.penup()
line.goto(-220, 200)
line.right(90)
line.pendown()
line.width(3)
line.forward(410)
m.pencolor("gold")
m.penup()
m.goto(220, -200)
m.right(-90)
m.pendown()
m.width(3)
m.forward(410)
if bet:
    race_is_on = True

while race_is_on:
    for k in turtles:
        if k.xcor() > 202:
            race_is_on = False
            won = k.pencolor()
            if won == bet:
                print(f"You selected : {bet} \nyou won since {won} wins!")
            else:
                print(f"You selected : {bet} \nyou lost since {won} wins!")

        dist = random.randint(0, 10)
        k.forward(dist)

s.exitonclick()
