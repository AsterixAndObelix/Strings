import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'H':
        newstr = 'HFX[+H][-H]'   # Rule 1
    elif ch == 'X':
        newstr = 'X[-FFF][+FFF]FX'
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    history = "O"
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            prow = str(aTurtle.heading())
            run = str(aTurtle.xcor())
            rise = str(aTurtle.ycor())
            history.replace("O", prow + run + rise + "0")
            print()
            #print(savedInfoList)
        elif cmd == ']':
            newInfo = history
            aTurtle.setheading(newInfo.read(0))
            aTurtle.setposition(newInfo, newInfo)


def main():
    inst = createLSystem(4, "H")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 27.5, 5)  # draw the picture

    wn.exitonclick()

main()
