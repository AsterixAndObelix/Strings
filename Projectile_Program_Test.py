import math
import turtle

class Projectile:

    def __init__(self, angle, velocity, height):
        ttie = turtle.Turtle()
        ttie.down()
        self.xpos = 0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)
        ttie.xcor(Projectile.getX(self))
        ttie.ycor(Projectile.getY(self))

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

def getInputs():
    angle = eval(input("What is the launch angle?"))
    velocity = eval(input("What is the velocity?"))
    height = eval(input("What is the initial height?"))
    time = eval(input("What is the time interval between calculations?"))
    return angle, velocity, height, time

def main():
    window = turtle.Screen()
    angle, velocity, height, time = getInputs()
    ptie = Projectile(angle, velocity, height)
    while ptie.getY() >= 0:
        ptie.update(time)
    print("Distance travelled: {0:0.1f} meters.".format(p.getX()))

main()
