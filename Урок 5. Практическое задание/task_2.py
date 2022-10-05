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


class HexNum:
    def __init__(self, num):
        self.hex = hex(int(num, 16))
        self.hex_arr = [i.upper() for i in num]

    def __mul__(self, other):
        res_num = int(self.hex, 16) * int(other.hex, 16)
        self.hex_arr = [i.upper() for i in str(res_num)[2:]]
        self.hex = hex(res_num)
        return self

    def __add__(self, other):
        res_num = self.hex + other.hex
        self.hex_arr = [i.upper() for i in str(res_num)[2:]]
        self.hex = hex(res_num)
        return self


num = input('first num')
num_2 = input('second num')

num = HexNum(num)
num_2 = HexNum(num_2)

res = num * num_2
print(res)
