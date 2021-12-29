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

class Hex:
    def __init__(self, number):
        self.num = str(number)
        print(self.num)


    def __mul__(self, other):
        return hex(int(self.num, 16) * int(other.num, 16))[2:].upper()


    def __add__(self, other):
        return hex(int(self.num, 16) + int(other.num, 16))[2:].upper()


a = Hex(input('Введите шестнадцатиричное число'))
b = Hex(input('Введите шестнадцатиричное число'))

print('sum', a + b)
print('product', a * b)
