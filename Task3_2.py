# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

import random
import math

def fill_list(n: int, min: int, max: int) -> list: 
    new_list = [random.randint(min, max)]
    for i in range(1, n):
        new_list.append(random.randint(min, max))
        i += 1
    return new_list

def product_pairs(user_list) -> list:
    new_list = []
    for i in range(0, math.ceil(len(user_list)/2)):
        new_list.append(user_list[i]*user_list[len(user_list)-1-i])
    return new_list

n = int(input('Количество элементов списка: '))
min = int(input('Граница 1 диапазона значений элементов списка: '))
max = int(input('Граница 2 диапазона значений элементов списка: '))
if max < min:
    max, min = min, max
source_list = fill_list(n, min, max)
result_list = product_pairs(source_list)
print(f'{source_list} => {result_list};')
