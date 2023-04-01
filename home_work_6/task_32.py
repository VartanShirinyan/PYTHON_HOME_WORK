'''Задача 32: 
Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

def find_indexes(lst, min, max):
    indexes = []
    for i in range(len(lst)):
        if min <= lst[i] <= max:
            indexes.append(i)
    return indexes
