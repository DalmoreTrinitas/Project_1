from math import sqrt


class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def count_perimeter(self):
        perimeter = (self.z + self.y + self.x)
        return perimeter

    def count_square(self):
        semiperimeter = self.count_perimeter() / 2
        square = sqrt(semiperimeter * (semiperimeter - self.z) * (semiperimeter - self.y) * (semiperimeter - self.x))
        return square

