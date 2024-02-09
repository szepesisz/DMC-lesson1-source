import math


class Length(float):
    # def __new__(cls, v):
    #     return float.__new__(cls, v)

    def __init__(self, v):
        float.__init__(v)
        assert self > 0, 'Length should be positive'
        self.visible = True


class Shape:
    # De mi van ha pl hosszakkal és szögekkel akarom megadni?
    # def __init__(self, *a, **kw):
    #     for v in list(a)+list(kw.values()):
    #         assert v > 0, 'Length should be positive'

    def area(self):  # absztrakt osztály
        raise NotImplementedError

    def __str__(self):
        _params = [f'{k}={v}' for k, v in self.__dict__.items() if isinstance(v, Length) and v.visible]
        return f'{self.__class__.__name__}({", ".join(_params)})'


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = Length(a)
        self.b = Length(b)

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.a = Length(a)
        self.b.visible = False


class Ellipse(Shape):
    def __init__(self, a, b):
        self.a = Length(a)
        self.b = Length(b)

    def area(self):
        return self.a * self.b * math.pi


class Circle(Ellipse):
    def __init__(self, r):
        super().__init__(r, r)
        self.r = Length(r)
        self.a.visible = False
        self.b.visible = False


shapes = [
    Rectangle(5, 6),
    Square(7),
    Circle(2),
    Ellipse(4, 5),
    Rectangle(4, 7)
]

for s in shapes:
    print(s, s.area())

print(sum([s.area() for s in shapes]))

s1 = Square(4)
print(isinstance(s1, Rectangle))

# r1 = Rectangle(3, -5)
# print(r1, r1.area())