import turtle

def recipe (times, initial):
    initial = ""
    final = ""
    for counter in times:
        final = read(initial)
        initial = final

    return initial

def read(initial):
    final = ""
    for ctie in initial:
        final = final + change(ctie)

    return final

def change(ctie):
    final = ""
    if ctie == "F":
        final = "FF"
    elif ctie == "X":
        final = "--FXF++FXF++FXF--"
    else:
        final = ctie

    return final

def draw(htie, list, atie, dtie):
    for dtie in list:
        if dtie == "F":
            htie.forward(dtie)
        elif dtie == "":
            htie.backward(dtie)
        elif dtie == "+":
            htie.right(atie)
        elif dtie == "-":
            htie.left(atie)

def main():
    list = recipe(5, "FXF--FF--FF")
    print(list)
    htie = turtle.Turtle()
    window = turtle.Screen()
    htie.up()
    htie.back(200)
    htie.right(90)
    htie.forward(100)
    htie.left(90)
    htie.down()
    htie.speed(9)

    draw(htie, list, 60, 5)

    window.exitonclick()

main()
