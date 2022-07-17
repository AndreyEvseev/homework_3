# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

import math

def descimal_to_binary(k: int) -> str:
    bin_k = [k % 2]
    while math.floor(k / 2) != 0:
        k = math.floor(k / 2)
        bin_k.insert(0, k % 2)
    bin_k = "".join(map(str, bin_k))
    return bin_k

k = int(input('Введите натуральное число: '))
b = descimal_to_binary(k)
print(f'{k} -> {b}')