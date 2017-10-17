import random

class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, p2X, p2Y):
        xDif = p2X - self.x
        yDif = p2Y - self.y
        print(xDif, yDif)
        midX = xDif + self.x
        midY = yDif + self.y
        return midX, midY

    def __str__(self):
        return str(self.x) + "," + str(self.y)

p1 = Point(0, 10)
print(p1.distance(-10, -10))
p3 = Point(-10, 10)
