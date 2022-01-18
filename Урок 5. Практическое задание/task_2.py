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


class Hexadecimal_number:
    def __init__(self, value):
        need_num = set(range(0, 10)).union({'a', 'b', 'c', 'd', 'e', 'f'})
        if set(value) <= need_num:
            self.value = value
        else:
            self.value = None

    def __add__(self, other):



number1 = Hexadecimal_number('aq123')

print(number1.value)
