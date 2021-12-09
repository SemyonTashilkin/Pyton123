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

class Person:
    skill = 10  # квалификация сотрудника

    def print_info(self, name, surname):
        self.name = name
        self.surname = surname
        print(f"Данные сотрудника: {self.name} {self.surname}")

    def add_skill(self, k):
        self.skill += k
        print(f"Квалификация сотрудника {self.name}: {self.skill}")


p1 = Person()
p1.print_info("Viktor", "Reznik")
p1.add_skill(3)
print()
p2 = Person()
p2.print_info("Anna", "Dolgih")
p2.add_skill(2)