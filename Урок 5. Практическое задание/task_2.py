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
from collections import deque

num_16 = '0123456789ABCDEF'
num_dict = defaultdict(int)
counter = 0
for key in num_16:
    num_dict[key] += counter
    counter += 1


def num_dex(str):
    dex = 0
    num = deque(str)
    num.reverse()
    for i in range(len(num)):
        dex += num_dict[num[i]] * 16 ** i
    return dex


def num_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in num_dict:
            if num_dict[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


num_1 = num_dex(input('Введите первое шестнадцатиричное число: '))
num_2 = num_dex(input('Введите второе шестнадцатиричное число: '))

print(f'Сумма чисел: {num_hex(num_1 + num_2)}')
print(f'Произведение чисел: {num_hex(num_1 * num_2)}')

# 2. Через ООП

num_1 = input('Введите первое шестнадцатиричное число: ')
num_2 = input('Введите второе шестнадцатиричное число: ')


class HexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(self.num_1, 16) + int(self.num_2, 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(self.num_1, 16) * int(self.num_2, 16)))[2:]


print(f'Сумма чисел: {HexNumber(num_1, num_2) + HexNumber(num_1, num_2)}')
print(f'Произведение чисел: {HexNumber(num_1, num_2) * HexNumber(num_1, num_2)}')
