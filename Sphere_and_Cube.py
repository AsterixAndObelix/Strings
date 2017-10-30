class Cube:
    def __init__(self, length):
        self.side = length
    def surface(self):
        return (self.side ** 2) * 6
    def area(self):
        return self.side ** 3

box = Cube(5)

print(box.surface())
print(box.area())

class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def surface(self):
        return (self.radius ** 2 * 3.14) * 4
    def volume(self):
        return (self.radius ** 3) * 3.14 * (4/3)

ball = Sphere(10)

print(ball.surface())
print(ball.volume())
