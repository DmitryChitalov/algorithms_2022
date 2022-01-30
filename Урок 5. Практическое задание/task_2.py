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

# Первый вариант через defaultdict

num_1 = 'A2'
num_2 = 'C4F'
my_dict = defaultdict(list)


def full_dict(x):
    for i in x:
        my_dict[x].append(i)


full_dict(num_1)
full_dict(num_2)


def get_sum(x, y):
    result = hex(int(x, 16) + int(y, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result


# print(get_sum(num_1, num_2))


def get_mul(x, y):
    result = hex(int(x, 16) * int(y, 16))[2:].upper()
    if result not in my_dict:
        for i in result:
            my_dict[result].append(i)
    return result


# print(get_mul(num_1, num_2))


# Второй способ через ООП

class HexNum:

    def __init__(self, num=str):
        self.num = num
        self.__nums_dict = {}
        for i in num:
            self.__nums_dict.setdefault(num, [])
            self.__nums_dict[num].append(i)

    def get_dict(self):
        return self.num, self.__nums_dict

    def __add__(self, other):
        res = hex(int(self.num, 16) + int(other.num, 16))[2:].upper()
        if self.__nums_dict.get(res) is None:
            self.__nums_dict.setdefault(res, [])
            for i in res:
                self.__nums_dict[res].append(i)
        return self

    def __mul__(self, other):
        res = hex(int(self.num, 16) * int(other.num, 16))[2:].upper()
        if self.__nums_dict.get(res) is None:
            self.__nums_dict.setdefault(res, [])
            for i in res:
                self.__nums_dict[res].append(i)
        return self

    def __str__(self):
        return f'{self.num}, {self.__nums_dict}'


a = HexNum('A2')
b = HexNum('C4F')

print(a + b)
print(a * b)