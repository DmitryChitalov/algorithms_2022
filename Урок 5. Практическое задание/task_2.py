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


class Hex():

    def __init__(self, digits):
        self.digits = digits

    @staticmethod
    def hex_to_dec(digits_string):
        return int(''.join(digits_string), 16)

    def __add__(self, other):
        sum_dec = self.hex_to_dec(self.digits) + self.hex_to_dec(other.digits)
        return hex(sum_dec).replace('0x', '').upper()

    def __mul__(self, other):
        sum_dec = self.hex_to_dec(self.digits) * self.hex_to_dec(other.digits)
        return hex(sum_dec).replace('0x', '').upper()


if __name__ == '__main__':
    hex_1 = Hex(input('Первое число: ').split())
    hex_2 = Hex(input('Второе число: ').split())
    print(f'Сумма: {(hex_1 + hex_2)}')
    print(f'Произведение: {(hex_1 * hex_2)}')
