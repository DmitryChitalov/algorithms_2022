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

# через ООП


class HexDigit:
    def __init__(self, list_in: list):
        self.digit = list_in

    def __add__(self, other):
        digit_1 = int(''.join(self.digit), 16)
        digit_2 = int(''.join(other.digit), 16)
        return list(f'{digit_1 + digit_2:X}')

    def __mul__(self, other):
        digit_1 = int(''.join(self.digit), 16)
        digit_2 = int(''.join(other.digit), 16)
        return list(f'{digit_1 * digit_2:X}')


if __name__ == '__main__':
    list_1 = ['A', '2']
    list_2 = ['C', '4', 'F']

    digit_1 = HexDigit(list_1)
    digit_2 = HexDigit(list_2)

    print('через ООП', '\n')
    print('Сумма:', digit_1 + digit_2)
    print('Произведение:', digit_1 * digit_2)
