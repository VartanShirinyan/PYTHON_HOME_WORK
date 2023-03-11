# Задача 2: 
# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите трехзначное число: '))

# Находим первую цифру, используя операцию целочисленного деления на 100
first_digit = number // 100

# Находим вторую цифру, используя операцию целочисленного деления на 10 и остаток от деления на 10
second_digit = (number // 10) % 10

# Находим третью цифру, используя операцию остаток от деления на 10
third_digit = number % 10

# Находим сумму цифр
sum_of_digits = first_digit + second_digit + third_digit

# Выводим результат
print('Сумма цифр трехзначного числа', number, 'равна', sum_of_digits)
