class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def count_perimeter(self):
        perimeter = (self.a + self.b) * 2
        return perimeter

    def count_square(self):
        square = (self.a * self.b)
        return square

    def compare_means(self):
        if self.a == self.b:
            return "Квадрат"
        else:
            return "Прямоугольник"

