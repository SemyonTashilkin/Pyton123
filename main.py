# day = int(input("Введите день недели (цифрами)"))
# if 1 <= day <=5:
#    print("Рабочий день - ", end="")
#    if day == 1:
#        print("понедельник")
#    if day == 2:
#        print("вторник")
#    if day == 3:
#        print("среда")
#    if day == 4:
#        print("четверг")
#    if day == 5:
#        print("пятница")
# elif day ==6 or day==7:
#    print("Выходной день - ", end="")
#    if day == 6:
#        print("суббота")
#    if day == 7:
#        print("воскресенье")
# else:
#    print("Такого дня нет")

# month = int(input("Введите номер месяца: "))
# if 3 <= month <= 5:
#     print("Весна", end="")
# elif 6 <= month <= 8:
#     print("Лето", end="")
# elif 9 <= month <= 11:
#     print("Осень", end="")
# elif month == 1 and month == 2 or month == 12:
#     print("Зима", end="")
# else:
#     print("Ошибка ввода данных")
#
# a, b = 20, 20
# print("a == b" if a == b else "a > b" if a > b else "a < b")
#
# a, b = 15, 0
# print("На ноль делить нельзя" if b == 0 else a/b)
#
# try:
#    n = int(input("Введите делимое: "))
#   m = int(input("Введите делитель: "))
#    print(n/m)
# except (ValueError, ZeroDivisionError):
#    print("Нельзя вводить строки")
#    print("Делить на ноль нельзя")
# else:
#    print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#    print("Конец программы")
#
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
# n = int(n)
# m = int(m)
# print(n + m)
# except ValueError:
# print(str(n + m))
# finally:
#    print("Конец программы")
#
# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1
#
# i = int(input("Укажите количество симвалов: "))
# while i > 0:
#     print("i=", i)
#     i -= 1
#
# n = input("Введите целое число: ")
# while type(n) != int:
# try:
# n = int(n)
# except ValueError:
# print("Число не целое!")
# n = input("Введите целое число: ")
# if n % 2 == 0:
# print("Число четное")
# else:
# print("Число не четное")
#
#
# n = int(input("Введите начало диапозона: "))
# m = int(input("Введите конец диапозона: "))
# sum = 0
# while n < m:
#     if n % 2 != 0:
#         sum += n
#         n += 1
#     print(sum)
#
# i = 0
# while True:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")
#
# while True:
#     n = int(input("Введите положительное число: "))
#     if not n < 0:
#         break
#
# a = 1
# while True:
#     n = int(input("Введите число: "))
#     if not n != 0:
#         break
#     a += n
# print(a)
#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
#
# i = 1
# while i < 5:
#    print("Внешний цикл: i=", i)
#    j = 1
#    while j < 4:
#        print("\nВнутренний цикл: j=", j)
#        j += 1
#    i += 1
#
# kol = int(input("Введите количество последовательности: "))
# ch = float(input("Введите число: "))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# i = 1
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
# print("Минимальное число: ", min_ch)
# print("Максимальное число: ", max_ch)
# print("Сумма: ", sum_ch)
#
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < 1:
#         if i % 2 == 0:
#             print("*", end="")
#         else:
#             print("-", end=" ")
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     print(" " * i + "*")
#     i += 1
#
# for i in 'Hello':
#     print(i)
#
# j = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue':
#     print(j, 'color:', color)
#     j += 1
#
# for i in 'one', 'two', 1, 20, 0.3:
#     print(i)
#
# for i in range(9, 2, -1):
#     print(i, end=" ")
#
# a = int(input("Введите целое число: "))
# for i in range(1, a):
#    if a % i == 0:
#        print(i, end=" ")
#
# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# for i in range(a, b):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nDone!")
#
# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end="")
#     print()
#
# print([i * 2 for i in "Hello"])
# print([i ** 3 for i in range(30) if i % 2 == 0])
#
# num = [8, 3, 9, 4, 1]
# print(id(num))
# print(num)
# # print(type(num))
# # print(type(["one", "two", 2, 3.5, [1, 2, 3]]))
# print(num[0])
# print(num[-3])
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))
# print("Длина списка: ", len(num))
#
# s = [5] * 6
# # s = [5, 6]
# print(s)
# b = list("Hello")
# print(b)
#
# n = list(range(10, 2, -2))
# print(n)
#
# n = 5
# a = [i ** 2 for i in range(1, n)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# d = b * 3
# print(c)
# print(d)
#
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#    a[i] = int(input("-> "))
# print(a)
#
# a = [input("-> ") for i in range(int(input("Коли-во: ")))]
# print(a)
#
# a = list(range(10, 2, -2))
#
# for i in range(len(a)):
#   print(a[i], end=" ")
# print()
# for j in a:
#    print(j, end=" "
#                "")
#
#
# n = list(range(21, 41))
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Список: ", n, "\nКоличество четных элементов: ", k, "\nСумма нечетных элементов: ", s)
#
# summa = k = 0
# n = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(len(n)):
#     if n[i] != 0:
#         summa += n[i]
#         k += 1
# print(summa/k)
#
# s = [5, 9, 3, 8, 1, 8]
# print(s[1:4:-1])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[-3:1:-1])
#
# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[19:20] = [18]
# print(s)
#
# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[19:20] = [18]
# print(s)
# s.append(99)
# s.append('add')
# print(s)
# s1 = []
# s1.extend([1,2,3])
# print(s1)
# s1.extend('add')
# print(s1)
#
# s = []
# for i in range(1,11):
#     s.extend([i ** 2])
# print(s)
#
# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[19:20] = [18]
# print(s)
# s.append(99)
# s.append('add')
# print(s)
# s.insert(1,100)
# print(s)
#
# s1 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# print(s1)
#
# s = []
# n = int(input("n = "))
# for i in range (n):
#     x = int(input("-> "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("не")
# print(s)
#
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 8]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
#
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s[8:] = []
# print(s)
# # s.remove(0)
# # print(s)
#
# s[3:5] = []
# print(s)
#
# last = s.pop()
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)
#
# # s.clear()
# # print(s)
#
# del s[:]
# print(s)
#
# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
# k = int(input("Введите индекс: "))
# x.pop(k)
# print(x)
#
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s.extend([3, 1, 3, 20, 3, 4, 3, 50, 3])
# print(s)
# num = s.count(3)
# print(num)
#
# ind = s.index(10)
# print(ind)
#
# s_copy = s.copy()
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# a.append(20)
# print("a =", a)
# print("b =", b)
#
# s.append(120)
# print(s)
# print(s_copy)
#
# s.reverse()
# print(s)
#
# s.sort(reverse=True)
# print(s)
#
#
# sorted_s = sorted(s)
# print(sorted_s)
# print(s)
#
# print("---------------")
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len)
# print(s2)
#
# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
# k = int(input("Введите индекс: "))
# x.pop(k)
# print(x)

# import random
# from random import random, randint, randrange
#
# print(random())
# print(randint(0, 9))
# print(randrange(0, 10, 2))

# import random as r

# print(r.randint(0, 9))
# print(r.randint(0, 9))

# cities = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеренбург"]
# print(r.choice(cities))

# s = [55, 66, 77, 88, 99, 66, 45, 78, 90]
# print(r.sample(s, 3))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)

# print(round(r.uniform(10.5, 25.5),2))

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print("Длина списка:", len(lst))
# print("Минимальное значение из списка:", min(lst))
# print("Максимальное значение из списка:", max(lst))
# print("Сумма элементов:", sum(lst))


# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# max_1 = max(mas1)
# print("Max: ", max_1)
# mas1.remove(max_1)
# mas1.insert(0, max_1)
# print(mas1)

# mas1 = [r.randint(-20, 20) for i in range(10)]
# print(mas1)
# mas1.sort(reverse=True)
# print(mas1)

# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# min_l = min(mas1)
# print("Min: ", min_l)
# ind_min_l = mas1.index(min_l)
# print("Index_min: ", ind_min_l)
# # del mas1[0:ind_min_l]
# print(mas1[ind_min_l:])

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)

# lst = []
# if lst:
#     print("True. Список пустой")
# else:
#     print("False")

# lst1 = [r.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# lst2 = [r.randint(0, 10) for j in range(int(input("Введите размер второго списка: ")))]
# print("List1: ", lst1)
# print("List2: ", lst2)
# lst3 = lst1 + lst2
# print("List3: ", lst3)
# lst3 = []
# # for i in range(len(lst1)):
# #     if lst1[i] not in lst3:
# #         lst3.append(lst1[i])
# # for i in range(len(lst2)):
# #     if lst2[i] not in lst3:
# #         lst3.append(lst2[i])
#
# for i in lst1:
#     repeat = False
#     for j in lst2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst3.append(i)
# for i in lst2:
#     repeat = False
#     for j in lst1:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst3.append(i)
# print("Элементы обоих списков без повторений:\n", "List3: ", lst3)
# lst3 = []
# for i in range(len(lst1)):
#     if lst1[i] in lst2 and lst1[i] not in lst3:
#         lst3.append(lst1[i])
# print(lst3)
# lst3=[]
# lst3=[min(lst1), min(lst2), max(lst1), max(lst2)]
# print(lst3)

# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = users1
# users2.append("Виктория")
# print(users1 is users2)

# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = copy.deepcopy(users1)
# users2.append("Виктория")
# print(users1)
# print(users2)
# print(users1 is users2)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка2
# ]
#
# print(m[1][2])
# print(m)
#
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# square = [[x**2 for x in row] for row in m]
#
# for row in square:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# m = [[x for x in range(y, y+10)] for y in range(10)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x+y)

# m = [
#     [2, 5, 8],
#     [8, 5, 6],
#     [9, 4, 1],
#     [7, 5, 6]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# for i in range(len(m)):
#     if i % 2 == 0:
#         m[i].sort()
#     else:
#         m[i].sort(reverse=True)
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()


# w, h = 3, 4
# m = [[r.randint(-20, 10)for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#
#         print(x, end="\t")
#     print()
# print()

# import copy
# import random as r


# 05.10.2021
from math import *

# radius = 2
# print(pi * (radius ** 2))

# num = sqrt(2)
# print(num)
# num1 = ceil(3.8)
# print(num1)
# num2 = floor(3.8)
# print(num2)

# radius = int(input("Введите радиус окружности: "))
# n = round(2 * pi * radius, 2)
# print("Длина окружности: ", n)

# num = -5.24
# print("Модуль числа: ", fabs(num))
#
# a = -14
# b = -8
# print("Наибольший общий делитель: ", gcd(a, b))

# mun_list = [1, 5, 3, 3.8]
# print("Сумма", fsum(mun_list))
#
# print(degrees(3.12159))
# print(sin(radians(90)))
# print(tan(radians(0)))

# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print(sqrt((a**2)+(b**2)))

# Вычисление площади фигуры
# print("Выбор фигуры" "\n1 - треугольник" "\n2 - прямоугольник" "\n3 - круг")
# num = int(input(": "))
# if num == 1:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     c = float(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print(round(s, 2))
# if num == 2:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     s =

import time
import locale

locale.setlocale(locale.LC_ALL, "ru")

# sec = time.time()
# print(sec)
# local_time = time.ctime(sec)
# print(local_time)
#
# res = time.localtime(sec)
# print(res)
# print("Год:", res.tm_year)
# print("Месяц:", res.tm_mon)
# print("День месяца:", res.tm_mday)
# print("Часов:", res.tm_hour)
# print("Минуты:", res.tm_min)
# print("Секунды:", res.tm_sec)
# print("День недели:", res.tm_wday)
#
# print(time.strftime("Today is %d %B, %Y", time.localtime(456178945)))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 0.5
# print("Programm started...")
# time.sleep(pause)
# print(str(pause) + " second. ")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут напомнить: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(3)
# finish = time.monotonic()
# res = finish - start
# print("Program time: ", str(res) + " seconds.")

# print(time.strftime("Сегодня: %d %B, %Y"))
# sec = time.time()
# local_time = time.ctime(sec)
# print("Местное время: ", local_time)

# def hello(name, word):
#     print("Hello, ", name, ". Say " + word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#    print (a + b)

# x = 5
# y = 3
# res = get_sum(x, y)
# print(res)
# print(get_sum(2.6, 4.3))
# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
# symbol(9, "+", "-")
# symbol(7, "X", "0")

######################################## 07.10.2021
# def hi(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(hi(10, 5))
# print(hi(5, 10))

# def maxmin(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# print(maxmin(10, 5))
# print(maxmin(5, 15))


# a = float(input("a = "))
# b = float(input("b = "))
# def fun(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(a, b)

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#         print()
#
# fib(35)


# def change(lst):
#     # 1-й вариант lst[0], lst[-1] = lst[-1], lst[0]
#     # 2-й вариант
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def get_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, d=3))

# def digit_sum(n, even=True):
# #     s = 0
# #     while n > 0:
# #         a = n % 10
# #         if even and a % 2 == 0:
# #             s += a
# #         elif not even and a % 2 != 0:
# #             s += a
# #         n //= 10
# #     return s
# #
# #
# # print("Сумма четных элементов: ")
# # print(digit_sum(9874023))
# # print(digit_sum(38271))
# # print(digit_sum(123456789))
# #
# # print("Сумма нечетных элементов: ")
# # print(digit_sum(9874023, even=False))
# # print(digit_sum(38271, even=False))
# # print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))

# 12.10.2021
# tpl = (10, 20, 30)
# print(tpl)
#
# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# a1 = (5,)
# print(type(a1))
# c = 1, 2, 3
# print(type(c))
# print(c)

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])
# a[1] = 3

# s1 = [int(input("-> ")) for i in range(5)]
# s2 = tuple([int(input("-> ")) for i in range(5)])
# print(s2)

# s = input("Введите по порядку, без пробелов элементы кортежа: ")
# a = tuple(s)
# print(a)

# import random as r
#
# mas = tuple([2 ** i for i i)n range(1, 13)]
# print(mas)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))
# # print(t3.index("a"))
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print("Такого символа нет")

# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             f = tpl.index(el)
#             s = tpl.index(el, f + 1) + 1
#             return tpl[f:s]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# import random as r


# def ran(a, b):
#     return tuple(r.randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
#
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [5, 6, 7], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# def func(lst):
#     a = []
#     [a.append(i) for i in reversed(lst) if i not in a]
#     return tuple(a)
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = (1, 2, 3)
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
#
# ls = list(a)
# print(ls)

# contries = (
#    ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#    ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )

# print(contries)
# for country in contries:
#    countryName, countryPopulation, cities = country
#    print("\nСтрана:", countryName, "\nНаселение =", countryPopulation)
#    for city in cities:
#        cityName, cityPopulation = city
#        print("\tГород:", cityName, "\tНаселение =", cityPopulation)

# 14.10.2021
# s = {"banana", "apple", "orange", "apple", "orange"}
# print(type(s))
# print(s)
# print(len(s))
# a = set('1231')
# print(a)
# c = ["red", "green", "green", "blue", "purple"]
# col = set(c)
# print(col)

# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# num = list({i for i in numbers if i % 2 == 0})
# print(num)

# def to_set(a):
#     b = set(a)
#     return b, len(b)
#
#
# print(to_set('я обычная строчка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# c = {"red", "green", "blue", "purple"}
# print("green" not in c)

# pr = {1, 2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")

# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r1 if i[1] == 'c'}
# print(a)

# a = {0, 1, 1, 2, 3}
# a.add(4)
# print(a)
# a.remove(4)
# print(a)
# b = 2
# if b in a:
#     a.remove(b)
# print(a)
#
# a.discard(1)
# print(a)
# a.pop()
# print(a)
#
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# a.update(b)
# b |= a
# c = a.intersection(b)
# c = a & b
# a &= b
# c = a - b
# c = a ^ b
# a ^= b
# c = a != b
# c = a.copy()
# print(c)
# print(a)


# a1 = {1, 2}
# a2 = {3}
# a3 = {4, 5}
# a4 = {3, 2, 6}
# a5 = {7, 8}
# a6 = {9, 8}
#
# c = a1 | a2 | a3 | a4 | a5 | a5 | a6
# print(c)
# print("Unic elems count:", len(c))
# print("Min elem:", min(c))
# print("Max elem:", max(c))

# s1 = input("Введите первую строку: ")
# s2 = input("Введите вторую строку: ")
# s3 = set(s1) & set(s2)
# for i in s3:
#     print(i, end=" ")

# ris = {"Марина", "Женя", "Света"}
# mus = {"Костя", "Женя", "Илья"}
# only = ris ^ mus
# both = ris & mus
# drawing = ris - both
# print("Only one hobby:", only)
# print("Both hobbies:", both)
# print("Drawing:", drawing)

# s = frozenset({i ** 2 % 4 for i in range(10)})
# print(s)

# r1 = set('ABCD')
# b = {frozenset({i+j for j in r1.difference({i})}) for i in r1}
# print(b)

# def superset(s1, s2):
#     if s1 > s2:
#         print("Объект", s1, "является чистым супермножеством")
#     elif s1 == s2:
#         print("Множества равны")
#    elif s1 < s2:
#         print("Объект", s2, "является чистым супермножеством")
#     else:
#        print("Супермножество не обнаружено")


# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}

# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)

# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)
#
# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {str(a): a ** 2 for a in range(2, 7)}
# print(d4)
# print(d4["2"])
# d4["2"] = 15
# print(d4)
# d4["5"] = 4 ** 2
# print(d4)

# d5 = {0: "text1", "one": 40, (1, 2.3): 'кортеж', 1: [2, 3, 5, 6, 7]}
# print(d5)
# print(d5[1, 2.3])
# del d5[(1, 2.3)]
# print(d5)
#
# print("one" in d5)
# print("a" in d5)
#
# print(d5.keys())
#
# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# # print(d6["four"])
# key = "four"
# # if key in d6:
# #     del d6[key]
# try:
#     del d6[key]
# except KeyError:
#     print('Элемента с ключом "' + key + '" нет в словаре')
# print(d6)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, "=", d6[key])

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d2 = int(input("Какой элемент исключить: "))
# del d[d2]
# print(d)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# print(len(d6))

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals["Испания"] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франиця', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны " + country + ": " + capitals[country])
#     else:
#         print("В базе нет страны с названием: " + country)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по", goods[i][2], "руб", sep="")


# d = {"A": 1, "B": 2, "C": 3}
# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
# d.clear()
# print(d)
# d2 = d.copy()
# d2["B"] = 5
# d["E"] = 7
# print("d =", d)
# print("d2 =", d2)

# value = d.get("B")
# print(value)
# print(d)
#
# new = d.items()
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys()
# print(a)
#
# item = d.pop("B")
# print(item)
# print(d)

# item = d.popitem()
# print(item)
# print(d)

# item = d.setdefault("R", 5)
# print(item)
# print(d)

# d.update([('R', 7), ('Q', 9)])
# print(d)
# d.update([('A', 20), ('B', 40)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {"A": 1, "B": 2, "C": 3}
# # v = d.values()
# # print(v)
# # lst = list(v)
# # print(lst)
# print(list(d.values()))

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y, ':', a[x][y])

# d1 = {
#     "John": {
#         "N": 3056,
#         "S": 8463,
#         "E": 8441,
#         "W": 2694
#     },
#     "Tom": {
#         "N": 4832,
#         "S": 6786,
#         "E": 4737,
#         "W": 3612
#     },
#     "Anne": {
#         "N": 5239,
#         "S": 4802,
#         "E": 5820,
#         "W": 1859
#     },
#     "Fiona": {
#         "N": 3904,
#         "S": 3645,
#         "E": 8821,
#         "W": 2451
#     }
# }
# for x in d1:
#     print(x)
#     for y in d1[x]:
#         print(y, ':', a[x][y])
# name = input("Имя: ")
# reg = input("Регион: ")
# print(d1[name][reg])
# s = int(input("Новое значение: "))
# d1[name][reg] = s
# print(d1[name])

# a = {'один': 1, 'два': 2, 'три': 3}
# d = {value: key for key, value in a.items()}
# print(d)

# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {key: value for key, value in a.items() if value <= 2}
# print(d)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)


# value = input("-> ")
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)

# # # # # # # #
# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
#
# print(m.get((2, 1), 0))
# print(m.get((0, 1), 0))

# try:
#     print(m[(2, 1)])
# except KeyError:
#     print(0)

# if (0, 1) in m:
#     print(m[(0, 1)])
# else:
#     print(0)
# # # # # # # # # # # # # # #

# a = {1: "Rectangle", 2: "Triangle", 3: "Circle"}
# value = list(a.values())
# print(value)
#
# k = list(a.keys())
# print(k)
#
# par = list(a.items())
# print(par)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# b = {}
# s = None
# for i in a:
#     if type(i) == str:
#         b[i] = []
#         s = i
#     else:
#         b[s].append(i)
# print(b)

# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# c = [4.6, 4.0, 9.3]
# # d = {k: v for (k, v) in zip(b, a)}
# d = zip(a, b, c)

# print(list(zip(range(5), range(100))))

# a = {12: "Dec", 1: "Jan", 2: "Feb"}
# b = {3: "Math", 4: "April", 5: "May"}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# ls = [2, 4, 1, 3]
# n = ['b', 'd', 'a', 'c']
#
# # a = list(zip(ls, n))
# # print(a)
# # a.sort()
# # print(a)
# # a = list(zip(n, ls))
# # print(a)
# # a.sort()
# # print(dict(a))
#
# a = sorted(zip(ls, n))
# print(a)

# month = ["January", "February", "March"],
# total = [52000.00, 51000.00, 48000.00],
# prod = [46800.00, 45900.00, 43200.00]
#
# for t, p, m in zip(total, prod, month):
#     profit = t - p
#     print("Общая прибыль в", m, "= ", profit)

# one = {'apple': 0.04, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "->", v)

# data = [5, 6, 7, 8, 9, 4, 1]
# for i, val in enumerate(data):
#     print(i, ":", val)

# d = {1: {'a': 1, 'b': 2, 'c': 3},
#      2: {'a': 10, 'b': 20, 'c': 30}}
# for i,k in enumerate(d):
#     print(i, ") key = ", k, ", value = ", d[k], sep="")

# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))

# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst, 1)
# c = next(b)
# print(c)

# a = [1, 2, 3]
# b = [4, 5, 6, *a]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))
# print(func())

# def summa(*params):
#     # res = 0
#     # for n in params:
#     #     res += n
#     # return res
#     return sum(params)
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 6, 1))

# def a(*z):
#     return {i: i for i in z}
#
#
# print(a(1, 2, 3, 4))
# print(a('grey', (2, 17), 3.11, -4))

# def arf(*params):
#     res = (sum(params)) / len(params)
#     print(res)
#     return [i for i in params if i < res]
#
#
# print(arf(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(arf(3, 6, 1, 9, 5))

# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(1, 3))
# print(func(1, 2, 3, "abc"))

# def print_scores(student, *scores):
#     print("Имя студента:" + student)
#     for s in scores:
#         print(s, end=" ")
#     print()
#
#
# print_scores("Валентин", 100, 90, 88, 92, 99)
# print_scores("Роман", 96, 20, 33, 56)

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*params, only_odd=False):
#     res = []
#     for i in params:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def func(*args, **kwargs):
#     return args, kwargs
#
#
# print(func(4, 6, a=1, b=3, c=5))
# # print(func(1, 2, 3, "abc"))
# print(func(a="Python"))

# def info(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# info(firstname="Irina", lastname="Sharma", age=22, phone="1234567898")
# info(firstname="Igor", lastname="Wood", age=25, phone="4564871778", email="igor@mgmail.com", country="Russia")

# my_dict = {'one' : 'first'}
#
# def db(**data):
#     my_dict.update(**data)
#     return my_dict
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# print('my_dict = ', db(name='Bob', age=31, weight=61, eyes_color='grey'))

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)

# name = "Tom"
#
# def hi():
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye:", name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# def add_two(a):
#     x = 2
#     return a + 2
#
#
# print(add_two(3))
# print(x)

# def add_five(a):
#     x = 2
#
#     def wrap():
#         print("x =", x)
#         return a + x
#
#     return wrap()
#
#
# print(add_five(5))

# x = 4
#
#
# def func():
#     print(x + 3)
#
#
# func()

# import builtins
#
# names = dir(builtins)
# for i in names:
#     print(i)

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренний функции", a + b)
#
#     print("Значение внешней переменной a:", a)
#     fun2(4)
#
#
# fun1()


# x = 25

# def fn():
#     global t
#     a = 30
#     t = a
#     print("global:", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)
#         return
#
#     inner()
#     return
#
#
# fn()
#
# z = x + t
# print(z)

# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#
#         fn3()
#         print("fn2.x1 =", x1)
#
#     fn2()
#     print("fn1.x1 =", x1)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print("result = ", result)

# s = 0
#
#
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))
# # print("s =", s)

# def increment(n):
#     def inner_increment(x):
#         return n + x
#
#     return inner_increment
#
#
# a = increment(10)
# print(a(5))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'Ella': 54,
#     'David': 75,
#     'Fiona': 35,
#     'Grace': 69
# }

# def make_classfilter(lower, upper):
#     def class_student(exem):
#         return {k: v for (k, v) in exem.items() if lower <= v <= upper}
#
#     return class_student
#
#
# a = make_classfilter(80, 100)
# b = make_classfilter(70, 80)
# c = make_classfilter(50, 70)
# d = make_classfilter(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 3)
# print(obj1.add())
#
# obj2 = func(5, 3)
# print(obj1.sub())
#
# obj3 = func(5, 3)
# print(obj1.mul())

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func("a", "b"))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# sumn = lambda a=1, b=2, c=3: a + b + c
# print(sumn())
# print(sumn(10))
# print(sumn(10, 20))
# print(sumn(10, 20, 30))

# func1 = lambda *args: args
# print(func1(1, 2, 3, 4))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4,)
#
# for t in c:
#     print(t('abc'))

# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: (lambda x: x + n))
#
# f = inc(42)
# print(f(0))
#
# print((lambda n: (lambda x: x + n))(42)(3))
#
# print((lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))

# 02.11.2021 *************************************************************

# d = {'c': 4, 'b': 15, 'a': 10}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# print(list_d)
# print(dict(list_d))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
# ]
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# print()
# res1 = sorted(players, key=lambda item: item['raiting'])
# print(res1)
# print()
# res1 = sorted(players, key=lambda item: item['raiting'])
# res2 = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res2)

# a = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y)
# ]
# b = a[4](5, 12)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i), end=" ")
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday'),
# }
# d[2]()
# from math import *
#
# d = {
#     'circle': lambda r: pi * r ** 2,
#     'p': lambda x, y: x * y,
#     't': lambda a, b, h: 0.5 * h * (a + b)
# }
# print("Площадь окружности:", d['circle'](2))
# print("Площадь прямоугольника:", d['p'](10, 13))
# print("Площадь окружности:", d['t'](7,5,3))

# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 14))
# print(maximum(5, 14))

# minimum = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(minimum(9, 8, 5))

# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
# # lst2 = list(map(mul, lst))
# # print(lst2)
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# lst = ['1', '2', '3', '4', '5']
# lst2 = list(map(int, lst))
# print(lst2)

# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
# res = list(map(round, areas, range(1, 5)))
# print(res)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: (x + y), l1, l2))
# print(res)

# st = "hello"
# res = list(map(lambda x: x * 3, st))
# print(res)

# t = ('asfsak', 'asp', 'asfqwqasd', 'asq')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# import random as r
#
# lst1 = [r.randint(0, 100) for i in range(10)]
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst1))
# print(lst1)
# print(lst2)

# lst1 = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, lst1)))

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)

# a = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], a))
# print(m)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основе заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилинда
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(3, 6))
# print(cylinder.__doc__)
# print(max.__doc__)

# 04.11.2021 **************************************************************

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

#### Присваивание ######################

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# # test = my_decorator(func_test)
# # test()
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def func_decorator(fn):
#     i = 0
#
#     def wrap():
#         nonlocal i
#         fn()
#         i += 1
#         print("Вызов функции", i)
#
#     return wrap
#
#
# @func_decorator
# def fn():
#     print("Hello")
#
#
# fn()
# fn()
# fn()


# def args_decorator(fn):
#     def wrap(*arg1, **arg2):
#         print("args", arg1)
#         print("kwargs:", arg2)
#         fn(*arg1, **arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c="Виктор", study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         # print(args)
#         # print(kwargs)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# @args_decorator
# def one(a, b):
#     print(a + b)
#
#
# @args_decorator
# def two(a, b, c=3):
#     print(a * b * c)
#
#
# one(2, 3)
# two(2, 3, 4)
# two(2, 3, c=5)


# def args_decorator(arg1, arg2):
#     print("Я создаю декоратор. Аргументы:", arg1, arg2)
#
#     def my_decorator(func):
#         print("Я - декоратор. Аргументы", arg1, arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print("Я - обертка вокруг декорируемой функции")
#             func(arg1, arg2)
#             return func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return my_decorator
#
#
# @args_decorator("Игорь", "Нефедов")
# def print_full_name(first, last):
#     print("Меня зовут:", first, last)
#
#
# print_full_name("Ирина", "Лаврова")

# def args_decorator(decorator_text):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     return my_decorator
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("world!")

# def multiply(num):
#     def my_decor(func):
#         def wrap(args):
#             return "Результат: " + str(func(args) * num)
#
#         return wrap
#
#     return my_decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Типы данных не соответствуют")
#
#             for i in kwargs:
#                 if type(f_kwargs[i]) != kwargs[i]:
#                     raise TypeError("Типы данных не соответствуют")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello, ", "world", "!"))
# print(typed_fn3("Hello, ", "world! ", z=5))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world("Hi")
# hello_world2("world!")

# 09.11.2021 ************************************************************

# q = "Pyt"
# w= 'hon'
# e = q + w
# print(e)
# print(e * -3)
# print(e in "I am learn Python")
#
# s = "Hello"
# print(s[2:len(s)-1])
# print(s[:])
# print(s[4:2])
# print(s[-5:-2])
# print(s[0:5:2])

# s = 'abcdefgh'
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, -1)])

# s = 'python'
# print(id(s))
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# def change_char(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#     return s2
#
#
# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
# str2 = change_char(str1, "N", "P")
# print(str1)
# print(str2)

# print(u"Hello")
# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print(f'Меня зовут {name}, мне {age} лет')

# import math
#
# print(f"Значение числа pi: {math.pi:.2f}")
#
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")

# planets = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f'Мы живем на планете {planets[2]}')
#
# planet = {"name": "Земля", "radius": 6378000}
# print(f"Планета {planet['name']}. Радиус {planet['radius']/1000} км")
#
# print(f"15 / 4 = {round(15/4)}")

# name = "друг"
# prof = "программист"
# lang = "Python"
#
# message = (
#     f"Привет {name}. "
#     f"Ты {prof}. "
#     f"На языке {lang}."
# )
#
# print(message)

# a = 74
# print(f"{{{a}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')

# print(ord('a'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# str1 = 'Test string for me'
# arr = [ord(x) for x in str1]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in [ord(x) for x in (input("-> "))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))

# a = 122
# b = 97
# print(*(chr(x)for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))


# 11.11 **************************************************************************************************************

# s = "hello, WORLD! I am learning Python. 123@!"
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.lower().count("i"))
# print(len(s))
# print(s.count("l", 0, 15))
#
# print(s.find("l"))

# str1 = input("Введите два слова через пробел: ")
# a = str1[str1.find(" ") + 1:]
# b = str1[:str1.find(" ")]
# print(a)
# print(b)
# print(a + " " + b)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)


# s = "Дана ст(рока символов ,среди которых есть одна открыв)ающаяся"
# print(s[s.find('(') + 1:s.find(')')])


# s = 'aaaaaaaaaafaaaaaaaaaafaaaaaaaaaaa'
# for i in s:
#     if i.count('f') == 1:
#         print(s.index("f"))
#     elif i.count('f') >= 2:
#         print(s.index("f"))
#     else:
#         pass

# s = "hello, WORLD! I am learning Python. 123@!"
# print(s.endswith("hello", 0, 5))

# print('abc123'.isalnum())
# print('AAACjhl'.isalnum())
# print('45648975641'.isdigit())
# print("asd".isidentifier())
# print('asqwp'.islower())

# print('https://www.python.org'.lstrip('/:pths'))

# s = "Замените в этой строке все появления буквы \"о\" на букву \"О\", кроме первого и последнего вхождения"
# print(s)
# s = s.replace('о', 'О')
# s = s[s.index("о"):13].lower("О")
# print(s)


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
# print('...'.join(['1', '99']))
#
# print(':'.join("Hello"))

# stroka = input("Введите ФИО - ").split()


# def ren(inp):
#     return inp[0] + " " + inp[1][0] + ". " + inp[2][0] + "."
#
#
# print(ren(stroka))

# 16.11 ***********************************************************************

import re

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# reg = 'я'
# print(s.find(reg))
# print(reg in s)
#
# print(re.findall(reg, s))
# print(re.search(reg, s))
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# # reg = 'Я'
# print(re.match(reg, s))
# reg = r"\."
# print(re.split(reg, s, 1))
# print(re.sub(reg, '!', s))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 2565"
# reg = '[2021]'
# print(re.findall(reg, s))
# s = "Ели[-ели]."
# reg = r'[А-Яа-яё\[\].-]'
# print(re.findall(reg, s))

# reg = r'[^0-9]'
# print(re.findall(reg, s))

# s = 'Час в 24-часовом формате от 00 до 23. 2121-06-15Т21:45. Минуты, в диапозоне от 00 до 59. 21021-06-1501:09.'
# reg = r'[02][0-9][\:][0-9][0-9]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 2565"
# reg = r'\Bпаден'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта. 2565"
# reg = r'20*'
# print(re.findall(reg, s))

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+', d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.*", "", s))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("-", ".", re.sub("#.*", "", s)))


# s = "12 сентября 2021 года"
# reg = r'\d{3,}'
# print(re.findall(reg, s))

# s = "МИД - Министерство иностранных дел, ГЭС - гидроэлектростанция, ФСБ - Федеральная служба безопасноти"
# reg = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]'
# print(re.findall(reg, s))

# tel = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7[0-9]{10}'
# print(re.findall(reg, tel))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# # reg = r'\w+\s\w+\.$'
# reg = r'\w+\.$'
# print(re.findall(reg, s))

# s = "+7 900"
# reg = r'^\+\d+\s+\d+$'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# reg = r'я'
# print(re.findall(reg, s, flags=re.IGNORECASE))
# print(re.findall(r'\d+', "12 + ۳"))
# print(re.findall(r'\d+', "12 + ۳", flags=re.ASCII))

# text = r'''
# Торт
# с вишней1
# вишней2
# '''
# print(re.findall(r'Торт.c', text))
# print(re.findall(r'Торт.с', text, flags=re.DOTALL))
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))

# print(re.findall('''
# [\w.-]+
# @ # разбиваем по @
# [\w.-]+
# ''', "test@mail.ru", re.VERBOSE))


# 18.11 ************************************************************************************

# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))
#
# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; год= 1831'
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))

# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*?>', text))

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.search('<.*?>', text).group())

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img[^>]*>'
# print(re.findall(reg, s))

# text = 'Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровневый язык программирования ' \
#        'общего назначения с динамической строгой типизацией и автоматическим управлением паматью[18][19]'
# reg = r'\[.*?]'
# print(re.findall(reg, text))

# s = "Борис, Юрий, Ирина отлично учаться!"
# reg = r'Борис|Юрий|Ирина'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.I))
# print(re.search(reg, s, re.I).group())

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# date_user = input('Введите дату в формате dd-mm-YYYY: ')
# date_user = '28-08-2021'
# reg = r'([0-2][0-9]|[3][01])-([0][1-9]|[1][0-2])-([1][9][0-9][0-9]|[2][0][0-9][0-9])'
# print(re.findall(reg, date_user))

# s = '127.0.0.1'
# reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "Базовый JS прост. Продвинутый Python сложен. Базовый Python просто."
# 1 reg = r'[а-яё]+(?= Python)'
# 2 reg = r'Базовый(?! Python)'
# 3 reg = r'(?<=Базовый )\w{2,6}'
# reg = r'(?<!Продвинутый )Python'
# print(re.findall(reg, s, re.I))


# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"
# reg = r'\w+(?<!Людовик)VI'
# print(re.findall(reg, s, re.I))

# s1 = '1X, Text ABC 123 A1B2C3'
# reg = r'(?<!\d)\d(?!\d)'
# print(re.findall(reg, s1, re.I))
#
# s2 = 'text from #START# till #END#'
# reg = r'(?<=#START#).*(?=#END#)'
# print(re.findall(reg, s2, re.I))
#
# s3 = '12_34__56'
# reg = r'\d+(?=_(?!_))'
# print(re.findall(reg, s3, re.I))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 2565"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print("Строка: ", m[0])
# print("Цифра: ", m[1])
# print("Буквы: ", m[2])

# s = "Самолёт прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'google.com and google.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.search(reg, s).group())
# print(re.sub(reg, r'http://\1', s))

# def is_roman_number(num):
#     pattern = r'^M{0,3}(CD|CM|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
#     if re.search(pattern, num):
#         return True
#     return False
#
#
# print(is_roman_number('MMDCCLXXIII'))
# print(is_roman_number('CCCMMVIIVV'))


# 23.11 *************************************************************************

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
#

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(type(names[1]) == list)
# print(isinstance(names, list))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def count_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
#
#
# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(count_items(names))

# def union(s):
#     if not s: # s == [] проверка списка на пустоту
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("        Hello \tWorld "))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 17))

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# # print(binary_search(lst, 3))
# print(binary_search(lst, 1))

import random as r

# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - 1 - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print

# s1 = [5, 9, 6, 7]
# s2 = [3, 11, 8]
# s3 = [2, 4]
# s4 = [10, 1, 12]
# s5 = s1 + s2 + s3 + s4
# sor_1 = "1 - сортировка по убыванию"
# sor_2 = "2 - сортировка по возрастанию"
# print(s5)
# n = int(input("-> "))
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         if n == 1:
#             for j in range(len(array) - i - 1):
#                 if array[j] < array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#         elif n == 2:
#             for j in range(len(array) - 1 - 1):
#                 if array[j] > array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#         else:
#             print("Нет такой сортировки")
#
#
# bubble(s5)
# print(s5)
#
# number_search = int(input("Ввдеите значение для поиска: "))
#
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             return True
#         else:
#             pos = pos + 1
#     return found
#
#
#
# print(seq_search(s5, number_search))


# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [9, 5, 3, 8, 6]
# print(array)
# array = merge_sort(array)
# print(array)

# def shell_sort(s):
#     gap = len(s)
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, "Список: ", s)
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)

# f = open(r"D:\pythonProject6\text.txt", "r")
# print(*f)
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# **************************************
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()

# f = open("test.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# for line in f:
#     print(line)
#
# f.close()

# f = open("test_file1.txt", "r")
# count = 0
# for line in f:
#     count += 1
# print('count =', count)
# f.close()

# f = open('xyz.txt', 'a')
# print(f.write('New text.'))
# lst = [str(i) + str(i - 1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# lines = ['This is line a', 'This is line b']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'r')
# text = f.readlines()
# print(text)
# f = open('xyz.txt', 'a')
# text[1] = 'Замена'
# print(text)
# f.close()

# 30.11 **********************************************************

# f = open('text.txt', 'r+')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())

# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
#
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file_name, 'r') as f:
#     file_lst = f.read().split(' ')
#
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))

# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r", encoding="utf-8") as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("text.txt"))

# with open ('text.txt', 'r', encoding="utf-8") as f:
#     lst = list(f.read().split())
#     m = max(len(i) for i in lst)
#     print([i for i in lst if len(i) == m])

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open('one.txt', 'w') as f:
#     f.write(text)
# read_file = "one.txt"
# write_file = "two.txt"
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)
# with open(write_file, 'r') as fw:
#     for line in fw:
#         print(line, end="")


# import os

# print('Текущая директория', os.getcwd())
# print(os.listdir())
# os.mkdir("folder")
# os.makedirs("folder1/folder2/folder3")
# os.remove('xyz.txt')
# os.rename('folder', 'test')
# os.rename('text.txt', 'folder1/folder2/ts1.txt')
# os.renames('text.txt', "text/new_text/tx.txt")
# os.rmdir('test')
# for root, dirs, files in os.walk('folder1', topdown=True):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# for root, dirs, files in os.walk("Work", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

import os
import os.path
import time

# print(os.path.split(r"D:\pythonProject6\folder1\folder2\folder3\file.txt"))
# print(os.path.dirname(r"D:\pythonProject6\folder1\folder2\folder3\file.txt"))
# print(os.path.basename(r"D:\pythonProject6\folder1\folder2\folder3\file.txt"))
# print(os.path.join('files', r"D:\pythonProject6", "folder1", "folder2", "file.txt"))

# dirs = ['Work/F1', 'Work/F2/F21']
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()


# file_with_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)

# print(os.path.exists(r'D:\pythonProject6\text\last.txt'))
# print(os.path.getctime(r'D:\pythonProject6\Work\w.txt'))
# print(os.path.getatime(r'D:\pythonProject6\Work\w.txt'))
# print(os.path.getmtime(r'D:\pythonProject6\Work\w.txt'))
# print(os.path.getsize(r'D:\pythonProject6\Work\w.txt'))

# path = r'test.txt'
# size = os.path.getsize(path)
# kb = size / 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
#
#
# print("Размер:", kb, ' KB')
# print("Дата последнего использования:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print("Дата последнего редактирования:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# print(os.path.normcase('C:User/admin/Documents'))
# print(os.path.relpath(r'D:\pythonProject6\test.txt'))
# print(os.path.isfile(r'D:\pythonProject6\test.txt'))
# print(os.path.isdir(r'D:\pythonProject6'))

# dir_name = 'Work'
# objs = os.listdir(dir_name)
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{obj} - dir')

# print('Hello')

print("Вносим изменения")
print("Вносим изменения в склонированный проект")

