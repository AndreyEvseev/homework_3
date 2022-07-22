# Функция для формирования списка случайных целых чисел

import random

def fill_list(n: int, border1: int, border2: int) -> list: 
    if border1 < border2:
        min, max = border1, border2
    else:
        min, max = border2, border1
    new_list = [random.randint(min, max)]
    for i in range(1, n):
        new_list.append(random.randint(min, max))
        i += 1
    return new_list