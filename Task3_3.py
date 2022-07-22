# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

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
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
import Func_fill_list_float as f
source_list = f.fill_list(n, b1, b2)
diff = difference_fractional_parts(source_list)
print(f'{source_list} => {diff};')
