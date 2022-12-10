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
2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""


class HexNumber:
    def __init__(self, number):
        self.number = number.upper()

    def __add__(self, other):
        return HexNumber(hex(int(self.number, 16) + int(other.number, 16))[2:].upper())

    def __mul__(self, other):
        return HexNumber(hex(int(self.number, 16) * int(other.number, 16))[2:].upper())

    def __str__(self):
        return self.number


if __name__ == '__main__':
    hexnumber_1 = HexNumber('A2')
    hexnumber_2 = HexNumber('C4F')
    print(hexnumber_1)
    print(hexnumber_2)
    print(hexnumber_1 + hexnumber_2)
    print(hexnumber_1 * hexnumber_2)
