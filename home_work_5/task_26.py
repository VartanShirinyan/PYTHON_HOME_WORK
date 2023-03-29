"""Задача 26:  Напишите программу, которая на вход принимает два числа a и b, 
и возводит число А в целую степень b с помощью рекурсии.

*Пример:*

a = 3; b = 5 -> 243 (3⁵)
    a = 2; b = 3 -> 8 """


def degree(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        return a * degree(a, b - 1)


a = int(input("Введите число А: "))
b = int(input("Введите число b: "))
result = degree(a, b)
print(f"{a} в степени {b} -> {result}")
