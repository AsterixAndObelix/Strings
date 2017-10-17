import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

    def reflect_x(self):
        newY = self.y * -1
        return self.x, newY

firstx = int(input("What is the x coordinate of the first point?\n"))
firsty = int(input("What is the y coordinate of the first point?\n"))
secondx = int(input("What is the x coordinate of the second point?\n"))
secondy = int(input("What is the y coordinate of the second point?\n"))

p = Point(firstx, firsty)
q = Point(secondx, secondy)
new = Point(firstx, firsty).reflect_x()
print(p.distanceFromPoint(q))
print(new)
