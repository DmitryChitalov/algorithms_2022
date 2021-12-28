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


class HexDigit:
    def __init__(self, digit):
        self._data = self._to_array(digit)

    def _to_array(self, digit):
        return list(str(digit))

    def _digit10(self):
        return int(''.join(self._data), 16)

    def __str__(self):
        return ''.join(self._data)

    def __add__(self, other):
        if not isinstance(other, HexDigit):
            raise TypeError('Оба операнда должны быть одного типа')

        return HexDigit(hex(self._digit10() + other._digit10())[2:])

    def __mul__(self, other):
        if not isinstance(other, HexDigit):
            raise TypeError('Оба операнда должны быть одного типа')

        return HexDigit(hex(self._digit10() * other._digit10())[2:])


if __name__ == '__main__':
    try:
        a = hex(int(input('Введите первое число (х16): '), 16))[2:]
        b = hex(int(input('Введите второе число (х16): '), 16))[2:]
    except ValueError as e:
        print('Вы ошиблись при вводе, попробуйте еще раз.')
        exit(e)

    print(f'Сумма чисел: {HexDigit(a) + HexDigit(b)}')
    print(f'Произведение чисел: {HexDigit(a) * HexDigit(b)}')

