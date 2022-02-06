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
Попытайтесь решить это задание в двух вариантах.
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
from functools import reduce


# вариант 1
class HexOperation:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return list(hex(int(self.x, base=16) + int(other.x, base=16)))[2:]

    def __mul__(self, other):
        return list(hex(int(self.x, base=16) * int(other.x, base=16)))[2:]


if __name__ == '__main__':
    s1 = HexOperation(input('Введите первое число: '))
    s2 = HexOperation(input('Введите второе число: '))
    print(s1 + s2)
    print(s1 * s2)


# вариант 2
def run_hex_operation():
    dct = defaultdict(list)
    for i in range(2):
        num = input('Введите число: ')
        dct[i] = list(num)
    sum_result = list(hex(sum([int(''.join(i), base=16) for i in dct.values()])))[2:]
    mul_result = list(hex(reduce(lambda a, b: a * b, [int(''.join(i), base=16) for i in dct.values()])))[2:]
    return f'Сумма: {sum_result}\nПроизведение: {mul_result}'


if __name__ == '__main__':
    print(run_hex_operation())
