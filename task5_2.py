"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
from collections import defaultdict


def lst_to_ddict(num):
    hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    return defaultdict(int, {index: hex_to_dec[value] for index, value in enumerate(reversed(num))})
# reversed - реверс числа
# enumerate() позволяет получить индекс элемента и его значение (0,последнее значение; 1, предпоследнее значение)


def ddict_to_lst(num):
    hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_to_hex = {val: key for key, val in hex_to_dec.items()}

    return [dec_to_hex[num[i]] for i in reversed(num)]
# {'five': 5, 'two': 2, 'three': 3, 'one': 1, 'four': 4, 'six': 6} при reversed будет ->
# {'six': 6, 'four': 4, 'one': 1, 'three': 3, 'two': 2, 'five': 5}
# i -> 5,4,3,2,1,0


def operation_add(a, b):
    a = lst_to_ddict(a)
    b = lst_to_ddict(b)
    c = defaultdict(int)
    next_num = 0
    n = max(len(a), len(b))
    for i in range(n):
        c[i] = (a[i] + b[i] + next_num) % 16
        next_num = (a[i] + b[i] + next_num) // 16
    if next_num > 0:
        c[n] = next_num
    return ddict_to_lst(c)


def operation_mul(a, b):
    a = lst_to_ddict(a)
    b = lst_to_ddict(b)
    c = defaultdict(int)
    for j in range(len(b)):
        temp = defaultdict(int)
        next_num = 0
        for i in range(len(a)):
            temp[i] = (a[i] * b[j] + next_num) % 16
            next_num = (a[i] * b[j] + next_num) // 16
        if next_num > 0:
            temp[len(a)] = next_num
        temp = ddict_to_lst(temp)
        temp.extend(['0' for k in range(j)])
        c = operation_add(c, temp)

    return c

a = list(input('Введите 1-ое 16-ое число: '))
b = list(input('Введите 2-ое 16-ое число: '))
print(f'Сумма чисел: {operation_add(a, b)}')
print(f'Умножение чисел: {operation_mul(a, b)}')
