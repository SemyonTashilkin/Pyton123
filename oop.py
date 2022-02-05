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


# import math

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

####################### Занятие 16.12.2021

# class Point:
#     __slots__ = ["__x", "__y"]
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_coords_x(self):
#         return self.__x
#
#     def __del_coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 100
# print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property
#     def coords_x(self):
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# p1.coord_x = 7
# print(p1.coord_x)
# print(p1.__dict__)

# Задача 1

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.to_pounds())
# w.kg = 41
# print(w.to_pounds())
# w.kg = "10"
# print(w.to_pounds())

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())

# Задача 2

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x -1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.inc(5), q.dec(5))

# Задача 3

# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         elif b > a and b > c and b > d:
#             return b
#         elif c > a and c > b and c > d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         elif b < a and b < c and b < d:
#             return b
#         elif c < a and c < b and c < d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def sred(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(a):
#         fac = 1
#         for i in range(1, a + 1):
#             fac *= i
#         return
#
#
# print(Numbers.max(3, 5, 7, 9))
# print(Numbers.min(3, 5, 7, 9))
# print(Numbers.sred(3, 5, 7, 9))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls (day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count (".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <=12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year} - {self.month} - {self.day}'


# d = "16.12.2021"
# day, month, year = map(int, d.split("."))
# print(day, month, year)
# d = Date()
# date = d.from_string("16.12.2021")
# print(date.string_to_db())
#
# d1 = Date()
# date1 = d1.from_string("09.09.2021")
# print(date1.string_to_db())
#
# date2 = Date.from_string("15.10.2021")
# print(date2.string_to_db())

# dates = [
#     '30.12.2021',
#     '30-12-2021',
#     '01.01.2021',
#     '12.31.2020'
# ]
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print('Неправильная дата или формат строки с датой')


# Задача

# import math
#
#
# class SquareFigure:
#     count = 0
#
#     @staticmethod
#     def formula_Gerona(a, b, c):
#         SquareFigure.count += 1
#         p = (a + b + c) / 2
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def OsnVys(a, h):
#         SquareFigure.count += 1
#         return 0.5 * h * a
#
#     @staticmethod
#     def SquareKv(a):
#         SquareFigure.count += 1
#         return a ** 2
#
#     @staticmethod
#     def SquarePr(a, b):
#         SquareFigure.count += 1
#         return a * b
#
#
# print(SquareFigure.formula_Gerona(3, 4, 5))
# print(SquareFigure.OsnVys(6, 7))
# print(SquareFigure.SquareKv(7))
# print(SquareFigure.SquarePr(2, 6))
# try_t = SquareFigure()
# print(try_t.formula_Gerona(1, 2, 3))
# print(SquareFigure.count)

# ***************************** Date 21.12.2021

# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_euro = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         # редактирование курса рубля по отношению к долару
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         # редактирование курса рубля по отношению к евро
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):  # смена владельца счета
#         self.surname = surname
#
#     def convert_to_usd(self):
#         # перевод в долары
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         # перевод в евро
#         eur_val = Account.convert(self.value, Account.rate_euro)
#         print(f'Состояние счета: {eur_val} {Account.suffix_euro}')
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#
#     def add_percent(self):  # начисление процентов
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):  # сняти заданной суммы
#         if val > self.value:
#             print(f'К сожалению, у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено')
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print('Инициализатор базового класса Prop')
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         Prop.__init__(self, *args)
#
#     def draw_line(self):
#         print(f'Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}')
#
#
# # print(isinstance(Point, object))
# # line.draw_line()
# # line.width = 10
# # print(line.width)
# line = Line(Point(1, 2), Point(10, 20))
# print(line.__dict__)

##### Date 23.12.2021

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Значение ширины должно быть больше 0')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Значение высоты должно быть больше 0')
#
#     def border_new(self, b):
#         self.border = b
#
#     def area(self):
#         return self.__width * self.__height
#         #return self.border_new()
#
#
# react = Rectangle(10, 20, 'green', '1px solid gray')
# print(react.area())
# print(react.width)
# print(react.height)
# print(react.color)
# print(react.border)
# react.width = 50
# print(react.area())

# Задача

# class Liquid:  # жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density  # плотность жидкости
#
#     def edit_density(self, val):  # изменение плотности
#         self._density = val
#
#     def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
#         res = m / self._density
#         print(f"Объем {m} кг {self._name} равен {res} m^3/")
#         return res
#
#     def calc_m(self, v):  # вычисление массы жидкости соотвертствующее заданному объему
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} составляет {res} кг.')
#         return res
#
#     def print_info(self):
#         print(f"Жидкость {self._name} плотность = {self._density} kg/m^3.")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         else:
#             return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть числами')
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник: \nШирина: {self.width}\nВысота: {self.height}")
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super.__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#        print("Рамка:", {self.fon})
#
#
# shape1 = RectFon(400, 200, "blue")
# shape1.show_rect()


# class Liquid:  # жидкость
#     def __init__(self, name, density):
#         self.__name = name
#         self.__density = density  # плотность жидкости
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, change_name):
#         self.__name = change_name
#
#     @property
#     def density(self):
#         return self.__density
#
#     @density.setter
#     def density(self, value):
#         self.__density = value
#
#     def edit_density(self, val):  # изменение плотности
#         self.__density = val
#
#     def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
#         res = m / self.__density
#         print(f"Объем {m} кг {self.__name} равен {res} m^3/")
#         return res
#
#     def calc_m(self, v):  # вычисление массы жидкости соотвертствующее заданному объему
#         res = v * self.__density
#         print(f'Вес {v} m^3 {self.__name} составляет {res} кг.')
#         return res
#
#     def print_info(self):
#         print(f"Жидкость {self.__name} плотность = {self.__density} kg/m^3.")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m):  # переопределение вычисление объема жидкости, соответствующего заданной массе
#         v = super().calc_v(m)
#         v_alc = m * self.strength
#         print(f'Объем алкоголя в {m} кг {self.name} составляет {v_alc} m^3')
#         return v, v_alc
#
#     def calc_m(self, v):
#         m = super().calc_m(v)
#         m_alc = v * self.strength
#         print(f'Вес алкоголя в {m} m^3 {self.name} составляет {m_alc} кг.')
#         return m, m_alc
#
#     def print_info(self):
#         super().print_info()
#         print(f'крепость = {self.strength}')
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)
#
# a.print_info()
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         #self.verify_old(old)
#         #self.verify_weight(weight)
#         #.verify_ps(ps)
#
#         self.__fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# p1.weight = 60
# p1.password = "4567 123456"
# p1.old = 35
# print(p1.fio)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()

# ========================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):  # абстрактный метод
#         raise NotImplementedError("В дочернем должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольник: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# from abc import ABC, abstractmethod
#
#
# # абстрактный класс
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # абстрактный метод
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещён на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
# class Table():
#
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
#
# t = Sq_table(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = Round_table(radius=10)
# print(t1.__dict__)
# print(t1.calc_area())


# ===========================

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_ru(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_ru(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_ru(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_ru():.2f} RUB')
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_ru():.2f} RUB')


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):


#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#         print("Display 1 Abstract Method")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#         print("Display 2 Abstract Method")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Я - метод внешнего класс")
#
#     def outer_obj_method(self):
#         print("Я являюсь связующим методом объекта внешнего класса")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я - метод внутреннего класса")
#             MyOuter.outer_class_method()
#             # print(MyOuter.age)
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний", out)
# # print(inner.inner_name)
# inner.inner_method()


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee List")
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = '657'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Degree", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Albina"
#             self.id = '007'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Degree", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()

# class Geekforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is an inner class of inner class")
#
#
# outer = Geekforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()


# class OS:
#     def system(self):
#         return "Windows 10"
#
#
# class CPU:
#     def make(self):
#         return "Intel"
#
#     def model(self):
#         return "Core-i7"

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is braking")
#
#
# b = Dog("Buddy")
# b.bark()
# b.play()
# b.sleep()

# class A:
#     # def __init__(self):
#     #     print("Инициализатор класса А")
#     def hi(self):
#         print("A")
#
#
# class B(A):
#     # def __init__(self):
#     #     print("Инициализатор класса B")
#     def hi(self):
#         print("B")
#
#
# class C(A):
#     # def __init__(self):
#     #     print("Инициализатор класса C")
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# d.hi()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# ==================================

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end=" ")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def show(self):
#             print(f" => {self.brand}, {self.cpu}, {self.ram}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#
#
# sub = MySubClass()
# sub.display("Это строка будет отображаться и записываться в файл")

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Good")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# class Clock:
#     __DAY = 86400  # 24*60* - число секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секунды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs + other.__secs)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 + c2
# print(c3.get_format_time())


# class Clock:
#     __DAY = 86400  # 24*60* - число секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секунды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs + other.__secs)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs - other.__secs)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs * other.__secs)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs // other.__secs)
#
#     def __eq__(self, other):
#         # return self.__secs == other.__secs
#         if self.__secs == other.__secs:
#             return True
#         return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# c3 = Clock(300)
# # c1 += c2 + c3
# # print("c1: " + c1.get_format_time())
# # cV = c1 - c2
# # print("c1 - c2: " + cV.get_format_time())
# # cU = c1 * c2
# # print("c1 * c2: " + cU.get_format_time())
# # cD = c1 // c2
# # print("c1 // c2: " + cD.get_format_time())
# # c1 -= c2
# # print("c1 -= c2: " + c1.get_format_time())
# # c1 *= c2
# # print("c1 *= c2: " + c1.get_format_time())
# # c1 //= c2
# # print("c1 //= c2: " + c1.get_format_time())

#
# if c1 == c2:
#     print("Время одинаковое")
# if c1 != c3:
#     print("Время разное")


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[1])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# class Linear(Root):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def calc(self):
#         if self.a == 0 and self.b == 0:
#             print('Бесконечность')
#         elif self.a != 0 and (self.b == 0 or self.a <= self.b):
#             print(f"The root of '3x+7=0' is: {round((-self.b / self.a), 2)}")
#         else:
#             raise TypeError('Корней нет')
#
#         p1 = Linear(3, 7)
#         p1.calc()
#         p2 = Quadratic(1, 2, 3)
#         p2.calc()


# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Правый операнд должен быть типом Point3D"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
#
#     @staticmethod
#     def __check0(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             pass
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("Неверное значение ключа")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print("Координыты должны быть числами")


# pt = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f"Координаты 1-й точки: {pt}")
# print(f"Координаты 2-й точки: {pt2}")

# class Point3D:
# def __init__(self, x, y, z):
# self.xyz = list()
# self.xyz.append(x)
# self.xyz.append(y)
# self.xyz.append(z)
#
# def set_x(self, x):
# self.xyz[0] = x
#
# def set_y(self, y):
# self.xyz[1] = y
#
# def set_z(self, z):
# self.xyz[2] = z
#
# def get(self):
# return self.xyz
#
# pt3 = pt + pt2
# print(f'Сложение координат: ({pt3})')
#
# pt4 = pt - pt2
# print(f'Вычитание координат: ({pt4})')
#
# pt5 = pt * pt2
# print(f'Умножение координат: ({pt5})')
#
# pt6 = pt / pt2
# print(f'Деление координат: ({pt6})')
#
# print(f'Равенство координат: {pt == pt2}')
#
# print("x =", pt['x'], "x1 =", pt2['x'])
# print("y =", pt['y'], "y1 =", pt2['y'])
# print("z =", pt['z'], "z1 =", pt2['z'])
#
# pt['x'] = 20
# print("Запись значения в координату x:", pt['x'])
# print(f"Координаты 1-й точки: {pt}")


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Squere:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Squere(10)
# s2 = Squere(20)
#
# shape = [r1, r2, s1, s2]
#
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}.')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает')
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}.')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает')
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print

# 25.01.2022 =============================================

# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'{self.last_name} {self.first_name} {self.age}', end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, spec, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.group} {self.rating}')
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, spec, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.experience}', end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, spec, group, rating, topic):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f'{self.topic}', end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     # Graduate("Шугани", "Сергей", 15, "PD_011", 5, "Защита персональных данных"),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(6, 9, 8)
# print(len(p))
# print(abs(p))

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
# print(p.length)
# # p.z = 6


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#
# pt3 = Point3D(10, 20)
# pt3.z = 30
# print(pt3.z)


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()
# c1()
#
# c2 = Counter()
# c2()
# c2()
# c2()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1("  ?Hello World! "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("перед вызовом функции")
#         self.func()
#         print("после вызова функции")
#
#
# @MyDecorator
# def function():
#     print("func")
#
#
# function()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         print("перед вызовом функции")
#         res = self.func(a, b)
#         print("после вызова функции")
#         return res
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(85, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print("перед вызовом функции")
#             print(self.name)
#             func(a, b)
#             print("после вызова функции")
#
#         return wrap
#
#
# @MyDecorator("test2")
# def function(a, b):
#     print(a, b)
#
#
# print(function(85, 5))


# 27.01.2022 ==========================

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             res = func(a, b)
#             return res ** self.arg
#
#         return wrapper
#
#
# @Power(3)
# def multuple(a, b):
#     return a * b
#
#
# print("Результат:", multuple(2, 2))


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def dec(fn):
#         def wrap(*args, **kwargs):
#             print("*" * 20)
#             fn(*args, **kwargs)
#             print("*" * 20)
#
#         return wrap
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTERY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенджера нет.")
#         print(text, end=" ")
#         return klass(text)
#
#
# @Message.register('Telegram')
# class TelegramMessage(Message):
#     def send(self):
#         print("(Telegram)")
#
#
# @Message.register('WhatsApp')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(WhatsApp)")
#
#
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create('WhatsApp', "new text")
# m2.send()
# m3 = Message.create("Telegram", "text text")
# m3.send()


# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
#
# p = Person("Иван", "Николаев")

# class String:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#
# p = Person("Иван", "Николаев")
# print(p.name.get())
# p.name.set('Игорь')
# print(p.name.get())


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#
# p = Person("Иван", "Николаев")
# print(p.name)
# print(p.surname)


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())


# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# ==================================================

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# from car import electrocar
#
# e = electrocar.Electrocar("Tesla", "T", 2018, 99000)
# e.show_car()
# e.description_battery()


# circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
# rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
# cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
# circle_max_s = max(circles, key=lambda c: c.get_circle_square())
# rect_min_p = min(rects, key=lambda r: r.get_rect_perimeter())
# cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
# cylinders_v_avg = sum(cylinders_v) / len(cylinders_v)
# print('*' * 50)
# print('Окружность с наибольшей площадью:', end=' ')
# circle_max_s.print_circle()
# print('Прямоугольник с наименьшим периметром:', end=' ')
# rect_min_p.print_rect()
# print(f'Средний объем всех цилиндров: {cylinders_v_avg:.2f}')

# import pickle

# filename = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['фрукты', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 1000
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, 'rb') as fh:
#     print(pickle.load(fh))

# class Test:
#     a_number = 35
#     a_string = 'привет'
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {"first": "a", "secont": 2, "third": [1, 2, 3]}
#
#     def __str__(self):
#         return f'Число: {Test.a_number}\nСтрока: {Test.a_string}\nСписок: {Test.a_list}\nКортеж: {Test.a_tuple}\nСловарь: {Test.a_list}'
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку:\n{my_obj}\n')
#
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку:\n{l_obj}\n')

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding="utf-8")
#         self.count = 0
#
#     def red_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f'{self.count}: {line}'
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding="utf-8")
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader('hello.txt')
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())

import json

data = {
    'firstname': 'Jane',
    'lastName': 'Dho',
    'hobbies': ['running', 'sky diving'],
    'age': 5,
    20 : 'one'
}

# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw)

with open('data_file.json', 'r') as fw:
    print(json.load(fw))




