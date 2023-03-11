# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

ticket = input("Введите шестизначный номер билета: ")

# Находим сумму первых трех цифр
first_three = int(ticket[0]) + int(ticket[1]) + int(ticket[2])

# Находим сумму последних трех цифр
last_three = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# Проверяем, является ли билет счастливым (сумма первых трех цифр равна сумме последних трех)
if first_three == last_three:
    print("Yes")
else:
    print("No")