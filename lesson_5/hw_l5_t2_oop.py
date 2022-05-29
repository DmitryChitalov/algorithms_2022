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


class HexSumMul:
    def __init__(self):
        self.h_num = input('Введите число в 16 С.И.: ')
        self.num = int(self.h_num, 16)

    def __add__(self, other):
        return list(hex(self.num + other.num))[2:]

    def __mul__(self, other):
        return list(hex(self.num * other.num))[2:]


if __name__ == '__main__':
    fst_num = HexSumMul()
    scnd_num = HexSumMul()
    print(f'Сумма чисел: {fst_num + scnd_num}')
    print(f'Произведение чисел: {fst_num * scnd_num}')
