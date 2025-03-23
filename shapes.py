

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

    def perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        print(perimeter)


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        self.width = length


