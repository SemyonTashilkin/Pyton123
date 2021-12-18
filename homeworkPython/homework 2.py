import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_radius(self):
        return self.radius

    def get_volume(self):
        return (4 / 3 * (math.pi * (self.radius ** 3)))

    def get_square(self):
        return (4 * math.pi * self.radius ** 2)

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def int_point_inside(self, x, y, z):
        if (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 <= self.radius ** 2:
            return True
        else:
            return False


s = Sphere()
s.radius = 0.6
print('get_radius:', s.get_radius())
print('get_volume:', s.get_volume())
print('get_square:', s.get_square())
print('get_center:', s.get_center())
print('int_point_inside:', s.int_point_inside(0, -1.5, 0))
s.set_radius(1.6)
print('get_radius:', s.get_radius())
print('int_point_inside:', s.int_point_inside(0, -1.5, 0))
