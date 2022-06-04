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


class HexClass():
    def __init__(self, number):
        self.number = list(number)

    def __add__(self, other):
        return list(hex(int(''.join(self.number), 16) + int(''.join(other.number), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.number), 16) * int(''.join(other.number), 16)))[2:]


if __name__ == '__main__':
    number_1 = HexClass('A2')
    number_2 = HexClass('C4F')

    print(number_1 + number_2)
    print(number_1 * number_2)
