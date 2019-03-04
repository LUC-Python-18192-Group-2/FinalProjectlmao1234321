import csv
import turtle

file = open("AVIATION.csv")
data = file.readlines()

data = data[1:]

t=turtle.Turtle()
t.speed = (100000000000000000000000)




image = "ezz.gif"

screen = turtle.Screen()

screen.bgpic("ezz.gif")


for row in data:
    data_of_row = row.split(",")

    if data_of_row[0] == '':
      continue
    else:
      latitude = float(data_of_row[0])

    if data_of_row[1] == '':
        continue
    else:
     longitude = float(data_of_row[1])



    total_fatal_injuries = float(data_of_row[2])

    if total_fatal_injuries > 50:
        if total_fatal_injuries >= 150:
            t.color("black", "Black")
        elif total_fatal_injuries >= 100:
            t.color("black", "Dark Red")
        else:
            t.color("black", "Red")
    elif total_fatal_injuries >= 10 or total_fatal_injuries <= 50:
        if total_fatal_injuries >= 35:
            t.color("black", "Dark Blue")
        elif total_fatal_injuries >= 20:
            t.color("black", "Light Blue")
        else:
            t.color("black", "Dark Orange")
    else:
        if total_fatal_injuries >= 5:
            t.color("black", "yellow")
        else:
            t.color("black", "pink")

    x = float(data_of_row[1])*4.9 + 5
    y = float(data_of_row[0])*5 - 85

    t.penup()
    t.setpos(0,0)

    t.setx(x)
    t.sety(y)

    t.pendown()

    angle=90

    t.begin_fill()

    for j in range(4):
        t.forward(total_fatal_injuries/2)
        t.left(angle)


    t.end_fill()

turtle.done()