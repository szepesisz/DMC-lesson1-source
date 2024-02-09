import math


class Shape:
    def area(self):  # absztrakt osztály
        raise NotImplementedError

    def __str__(self):
        _params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(_params)})'


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.a = a

    def __str__(self):
        return f'{self.__class__.__name__}(a={self.a})'


class Ellipse(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b * math.pi


class Circle(Ellipse):
    def __init__(self, r):
        super().__init__(r, r)
        self.r = r

    def __str__(self):
        return f'{self.__class__.__name__}(r={self.r})'


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


# az area fgv polimorf
# újrafelhasználható
# funkcionális: feladat megoldása
# oop: előkészítem, hogy sokat tudjak csinlálni: nem a probléma, hanem a világ modellezése felől közelítek
# nem must-have, csak ha segít
