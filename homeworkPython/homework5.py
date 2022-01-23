class Operators:
    def __init__(self, num):
        self.num = num

    def setnum(self, num):
        self.num = num

    def getnum(self):
        return self.num

    def __gt__(self, other):
        return self.num > other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __lt__(self, other):
        return self.num < other.num

    def __le__(self, other):
        return self.num < other.num


c3 = Operators(30)
c1 = Operators(10)

print(f'c3 > c1', c3 > c1)
print(f'c3 >= c1', c3 >= c1)
print(f'c3 < c1', c3 < c1)
print(f'c3 <= c1', c3 <= c1)
