from abc import ABC, abstractmethod
import math


class Root(ABC):
    @abstractmethod
    def calc(self):
        pass


class Linear(Root):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        if self.a == 0 and self.b == 0:
            print('Бесконечность')
        elif self.a != 0 and (self.b == 0 or self.a <= self.b):
            print(f"The root of '3x+7=0' is: {round((-self.b / self.a), 2)}")
        else:
            raise TypeError('Корней нет')


class Quadratic(Root):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc(self):
        d = self.b ** 2 + 4 * self.a * self.c
        if d > 0:
            x1 = (self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (self.b - math.sqrt(d)) / (2 * self.a)
            print(f'The roots of 1x^2-2x-3=0 are: {x1}, {x2}')
        elif d == 0:
            x = self.b / (2 * self.a)
            print(f'Корень = {x}')
        else:
            print("Корней нет")


p1 = Linear(3, 7)
p1.calc()
p2 = Quadratic(1, 2, 3)
p2.calc()
