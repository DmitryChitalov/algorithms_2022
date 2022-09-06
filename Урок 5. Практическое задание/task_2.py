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


class HexadecimalNumber:
    def __init__(self, val):
        self.hex_val = val
        self.equal_decimal = int(val, 16)

    def __str__(self):
        return f'{list(self.hex_val)}'

    def __add__(self, other):
        if isinstance(other, HexadecimalNumber):
            return HexadecimalNumber(hex(self.equal_decimal + other.equal_decimal)[2:].upper())

    def __mul__(self, other):
        if isinstance(other, HexadecimalNumber):
            return HexadecimalNumber(hex(self.equal_decimal * other.equal_decimal)[2:].upper())


def hex_sum(f_num, s_num):
    return list(hex(int(f_num, 16) + int(s_num, 16))[2:].upper())


def hex_mul(f_num, s_num):
    return list(hex(int(f_num, 16) * int(s_num, 16))[2:].upper())


def main_function():
    first_number = input('Введите первое шестнадцатеричное число: ')
    second_number = input('Введите второе шестнадцатеричное число: ')
    print(f'Их сумма: {hex_sum(first_number, second_number)}\nИх произведение: {hex_mul(first_number, second_number)}')


def main_oop():
    first = HexadecimalNumber(input('Введите первое шестнадцатеричное число: '))
    second = HexadecimalNumber(input('Введите второе шестнадцатеричное число: '))
    print(f'Их сумма: {first + second}\nИх произведение: {first * second}')


if __name__ == '__main__':
    main_function()
    main_oop()
