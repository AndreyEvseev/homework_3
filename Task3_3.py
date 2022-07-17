# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

import random

def fill_list(n: int, min: int, max: int) -> list: 
    new_list = [round(random.randint(min, max) + random.random(), 5)]
    for i in range(1, n):
        new_list.append(round(random.randint(min, max) + random.random(), 5))
        i += 1
    return new_list

def difference_fractional_parts(user_list) -> float:
    min = max = user_list[0] % 1
    for i in range(1, len(user_list)):
        if user_list[i] % 1 < min:
            min = user_list[i] % 1
        elif user_list[i] % 1 > max:
            max = user_list[i] % 1
        else:
            continue
    diff = round(max - min, 5)
    return diff

n = int(input('Количество элементов списка: '))
min = int(input('Граница 1 диапазона значений элементов списка: '))
max = int(input('Граница 2 диапазона значений элементов списка: '))
if max < min:
    max, min = min, max
source_list = fill_list(n, min, max)
diff = difference_fractional_parts(source_list)
print(f'{source_list} => {diff};')
