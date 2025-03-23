


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
    def __init__(self, length, width):
        super().__init__(length, width)
        self.length = length
        self.width = length


# sq = square(12)
# print(sq)

req = Rectangle(40, 10)
print(req.length)
print(req.width)

sq = Square(12, 12)
print(sq.width + sq.length)