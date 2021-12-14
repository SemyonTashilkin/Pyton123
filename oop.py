# class Point:
#     """Класс для предоставлении координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)


# print(Point.__doc__)
# print(Point.__name__)

# p1 = Point()
# p1.set_coords(5, 10)
#
# p2 = Point()
# p2.set_coords(40, 80)

# print(type(p1))
# print(isinstance(p1, Point_3D))

# p1.x = 5
# p1.y = 10
# # p1.z = 20
# print(p1.x, Point.x)
# print(getattr(p1, "x"))
#
# setattr(p1, "z", 7)
# print(hasattr(p1, "x"))
# print(hasattr(p1, "z"))
# print(p1.__dict__)
#
# delattr(p1, 'z')
# print(p1.__dict__)

# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)

# print(p1.__dict__)
# Point.x = 100  # новое значение x
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))


# Задача1

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "Street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}"
#               f"\nНомер телефона: {self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("*" * 40)
#
#     def input_info(self, name, birthday, phone, country, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # метод устанавливает имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, birthday):  # метод устанавливает имя
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def get_phone(self):
#         return self.phone
#
#     def get_country(self):
#         return self.country
#
# human1 = Human()
# human1.print_info()
# human1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# human1.print_info()
# human1.set_name("Ирина")
# print(human1.get_name())
# print(human1.get_birthday())

# ************** Задача 2

# class Car:
#     model = "model"
#     year = "year"
#     maker = "maker"
#     power = "power"
#     color = "color"
#     price = "price"
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year}"
#               f"\nПроизводитель: {self.maker}\nМощность двигателя: {self.power}"
#               f"\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print("*" * 40)
#
#     def input_info(self, model, year, maker, power, color, price):
#         self.model = model
#         self.year = year
#         self.maker = maker
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#
# car1 = Car()
# car1.print_info()
# car1.input_info("X7 M50i", "2021", "BMW", "530 л.с", "white", "10790000")
# car1.print_info()
# car1.set_model("Lada")
# car1.print_info()
# print(car1.get_model())

# ***** Задача 3

# class Person:
#     skill = 10  # квалификация сотрудника
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Данные сотрудника: {self.name} {self.surname}")
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника {self.name}: {self.skill}")
#
#
# p1 = Person()
# p1.print_info("Viktor", "Reznik")
# p1.add_skill(3)
# print()
# p2 = Person()
# p2.print_info("Anna", "Dolgih")
# p2.add_skill(2)

# date 14.12

# class Point:
# def __new__(cls, *args, **kwargs):
#     print("Конструктор")
#     return super().__new__(cls)

# def __init__(self, x=0, y=0):
#     # print("Инициализатор")
#     self.x = x
#     self.y = y

# def set_coords(self, x, y):
#     self.x = x
#     self.y = y


# p1 = Point(5, 10)
# print(p1.__dict__)
# Point.__init__(p1, 20)
# print(p1.__dict__)
# p2 = Point()
# print(p2.__dict__)
# p3 = Point(y=2)
# print(p3.__dict__)


# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1

# def __del__(self):
#     print("Удаление экземпляра: " + self.__class__.__name__)

# def chek_value(z):
#     if isinstance(z, int) or isinstance(z, float):
#         return True
#     return False
#
# def set_coords(self, x, y):
#     if Point.chek_value(x) and Point.chek_value(y):
#         self.x = x
#         self.y = y
#     else:
#         print("Координаты должны быть числами")
#
# def get_coords(self):
#     return self.x, self.y

# p1 = Point(5, 10)


# print(p1.__dict__)
# p2 = Point(2, 3)
# print(p2.__dict__)
# p3 = Point(2, 3)
# p4 = Point(2, 3)
# # print(p1.x)
# print(Point.count)
# print(p3.count)

# p1 = Point(5, 10)
# p1.set_coords(2.3, 5.6)
# print(p1.get_coords())
# print(p1.__dict__)

# Задача Robot

# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.count += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.count -= 1
#
#         if Robot.count == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.count)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут", self.name)
#
#
# r1 = Robot("R2-D2")
# r1.say_hi()
# print("Численность робота:", Robot.count)
# r2 = Robot("C-3PO")
# r2.say_hi()
# r3 = Robot("C1-3PO")
# r3.say_hi()
# r4 = Robot("C2-3PO")
# r4.say_hi()
# print("Численность робота:", Robot.count)
# print("\nЗдесь роботы могут проделать какую-нибудь работу\n")
# print("Роботы закончили свою работу. Давйте их выключим.")
# del r1
# del r2
# del r3
# del r4
# print("Численность роботов:", Robot.count)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def chek_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#
#         if Point.chek_value(x) and Point.chek_value(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.chek_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.chek_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
#
# p1.set_coords_x(100)
# p1.set_coords_y(10)
# print(p1.get_coords())


import math


# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def get_figure(self):
#         # for i in range(self.__length):
#         #     print(self.__width * "*")
#         print((self.__width * "*" + "\n") * self.__length)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print('Длина прямоугольника', rec1.get_length())
# print('Ширина прямоугольника', rec1.get_width())
# print('Площадь', rec1.square())
# print('Периметр', rec1.perimetr())
# print('Гипотенуза', round(rec1.hypo(), 2))
# rec1.get_figure()

