import turtle

ttie = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)

file = open("T(11.8.5)-Turtles_Drawing_Text_File_Commands", "r")

for line in file:
    values = line.split()
    if values[0] == "UP":
        ttie.up()
    else:
        if values[0] == "DOWN":
            ttie.down()
        else:
            # must be coords
            ttie.goto(int(values[0]), int(values[1]))

file.close()
wn.exitonclick()
