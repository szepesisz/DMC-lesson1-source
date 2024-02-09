
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


r1 = Rectangle(4, 5)
print(r1.area())


class Square:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2


s1 = Square(7)
print(s1.area())


# De!

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


s2 = Square(7)
print(s2.area())


print(s2)  # Csúnya


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangle(a={self.a}, b={self.b})'


r2 = Rectangle(4, 5)
print(r2)
