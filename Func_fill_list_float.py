# Функция для формирования списка случайных вещественных чисел

import random

def fill_list(n: int, border1: int, border2: int) -> list: 
    if border1 < border2:
        min, max = border1, border2
    else:
        min, max = border2, border1
    new_list = [round(random.randint(min, max) + random.random(), 5)]
    for i in range(1, n):
        new_list.append(round(random.randint(min, max) + random.random(), 5))
        i += 1
    return new_list
