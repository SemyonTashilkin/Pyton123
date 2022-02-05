class IntegerNumber:
    def __set_name__(self, owner, name):
        self.__name = name

    def __set__(self, instance, value):
        if not float(value).is_integer():
            raise ValueError("Значение должно быть целочисленным")
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point3D:
    x = IntegerNumber()
    y = IntegerNumber()
    z = IntegerNumber()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def prt(self):
        print({self.x}, {self.x}, {self.x})


p = Point3D(1, 2, 3)
print(str(p.__dict__))
