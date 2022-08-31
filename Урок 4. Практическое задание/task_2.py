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

from collections import defaultdict


def get_hex(obj_dict):
    print(hex(int(obj_dict[0], 16) + int(obj_dict[1], 16))[2:])
    print(hex(int(obj_dict[0], 16) * int(obj_dict[1], 16))[2:])


def main():
    obj_dict = defaultdict(list)
    for i in range(2):
        obj_dict[i] = input(
            'Введите шестнадцатиричное число: ').upper()
    return get_hex(obj_dict)


if __name__ == '__main__':
    main()


class GetHex():
    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __str__(self):
        return str(self.hex_number)[2:]

    def __add__(self, other):
        return GetHex(hex(int(self.hex_number, 16) + int(other.hex_number, 16)))

    def __mul__(self, other):
        return GetHex(hex(int(self.hex_number, 16) * int(other.hex_number, 16)))


first_number = GetHex(input('Введите шестнадцатиричное число: ').upper())
second_number = GetHex(input('Введите шестнадцатиричное число: ').upper())

print(first_number + second_number)
print(first_number * second_number)
