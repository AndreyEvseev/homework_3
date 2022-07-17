# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

import random

def fill_list(n=10, min=0, max=100) -> list: 
    new_list = [random.randint(min, max)]
    for i in range(1, n):
        new_list.append(random.randint(min, max))
        i += 1
    return new_list

def sum_elements_odd_position(user_list):
    sum_odd = 0
    for i in range(1, len(user_list)):
        if i % 2 != 0:
            sum_odd = sum_odd + user_list[i]
    return sum_odd

n = int(input('Количество элементов списка: '))
min = int(input('Граница 1 диапазона значений элементов списка: '))
max = int(input('Граница 2 диапазона значений элементов списка: '))
if max < min:
    max, min = min, max
source_list = fill_list(n, min, max)
sum_odd = sum_elements_odd_position(source_list)
print(source_list)
print(f'Сумма элементов списка, стоящих на нечётной позиции = {sum_odd};')
