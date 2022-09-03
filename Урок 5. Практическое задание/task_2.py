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
from functools import reduce


def input_two_hex_numbers():
    numbers = defaultdict(list)
    # defaultdict(<class 'list'>, {'A2': ['A', '2'], 'C4F': ['C', '4', 'F']})
    for i in range(1, 3):
        str_hex_number = input(f"Введите {i}-е шестнадцатеричное число: ")
        numbers[str_hex_number] = list(str_hex_number)

    return numbers


print("* * * Решение через collections * * *")
d = input_two_hex_numbers()
print("Числа сохранены как: ", end=' ')
print(*d.values())

# Without the 0x prefix, you need to specify the base explicitly,
# otherwise there's no way to tell:
addition = sum([int(''.join(i), 16) for i in d.values()])
print("Сумма: ", list(format(addition, 'X')))

multiplication = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in d.values()])
print("Произведение: ", list(format(multiplication, 'X')))
print('-' * 80)


class Hex:
    def __init__(self, number):
        self.lst_hexnumber = list(number)

    def get_number(self):
        return self.lst_hexnumber

    def __add__(self, other):
        return list(format(int(''.join(self.lst_hexnumber), 16) +
                           int(''.join(other.lst_hexnumber), 16),
                           'X'
                           )
                    )

    def __mul__(self, other):
        return list(format(int(''.join(self.lst_hexnumber), 16) *
                           int(''.join(other.lst_hexnumber), 16),
                           'X'
                           )
                    )


print("* * * Решение через ООП * * *")
str_hexnumber_1 = input("Введите 1-е шестнадцатеричное число: ")
str_hexnumber_2 = input("Введите 2-е шестнадцатеричное число: ")
hex_1 = Hex(str_hexnumber_1)
hex_2 = Hex(str_hexnumber_2)
print(f"Числа сохранены как: {hex_1.get_number()} {hex_2.get_number()}", end=' ')
print("Сумма: ", hex_1 + hex_2)
print("Произведение: ", hex_1 * hex_2)
print('-' * 80)
