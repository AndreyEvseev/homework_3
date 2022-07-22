# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def descimal_to_binary(k: int) -> str:
    bin_k = f'{k % 2}'
    while k // 2 != 0:
        k = k // 2
        bin_k = f'{k % 2}' + bin_k
    bin_k = int(bin_k)
    return bin_k

k = int(input('Введите натуральное число: '))
b = descimal_to_binary(k)
print(f'{k} -> {b}')