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

a = 'A2'
b = 'C4F'
print(hex(int(a, 16) + int(b, 16)))
"""


class Calc(str):
    def __init__(self, pasr_str):
        self.a = pasr_str
        self.mas = []
        for i in self.a:
            self.mas.append(i)
        print(self.mas)

    def __add__(self, other):
        return hex(int(self.a, 16) + int(other.a, 16))

    def __mul__(self, other):
        return hex(int(self.a, 16) * int(other.a, 16))


c1 = Calc("A2")
c2 = Calc("C4F")

print(c1 + c2)
print(c1 * c2)

"""
Решение через collections
"""
import collections


def pars_string(string):
    x = collections.defaultdict(list)
    y = collections.defaultdict(list)
    x, y = string.split()
    x = list(x)
    y = list(y)
    print(x, ' \n', y)
    print(int("".join(x), 16) + int("".join(y), 16))


diction = collections.defaultdict(list)

pars_string("11 111")
