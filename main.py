from Triangle import Triangle
from Rectangle import Rectangle


def print_hello_world(phrase):
    print(phrase)


if __name__ == "__main__":
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(9, 7)

    print_hello_world(phrase="triangle:")
    perimetr = triangle.count_perimeter()
    print(perimetr)

    square = triangle.count_square()
    print(square)

    print("rectangle:")

    perimeter = rectangle.count_perimeter()
    print(perimeter)

    square = rectangle.count_square()
    print(square)

    compare = rectangle.compare_means()
    print(compare)