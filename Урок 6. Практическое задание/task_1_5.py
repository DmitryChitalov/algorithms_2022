"""
Задание 1.5.
"""
# Алгоритмы Python. DZ_5.2
# Написать программу сложения и умножения двух шестнадцатеричных чисел,
# через ООП

from pympler import asizeof


class HexCalcClass:
    def __init__(self, n):
        self.val = n

    def __add__(self, other):
        add = str(hex(int(self.val, 16) + int(other.val, 16)))
        return add[2:].upper()

    def __mul__(self, other):
        mul = str(hex(int(self.val, 16) * int(other.val, 16)))
        return mul[2:].upper()


class HexCalcOptClass:
    __slots__ = ['x']

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        add = str(hex(int(self.x, 16) + int(other.x, 16)))
        return add[2:].upper()

    def __mul__(self, other):
        mul = str(hex(int(self.x, 16) * int(other.x, 16)))
        return mul[2:].upper()

if __name__ == '__main__':
    hex1 = HexCalcClass ('A2')
    hex2 = HexCalcClass ('C4F')
    print('Размер числа hex1: ',asizeof.asizeof((hex1)))
    print('Размер числа hex2: ',asizeof.asizeof((hex2)))
    print('Размер результата сложения', asizeof.asizeof((hex1 + hex2)))
    print('Размер результата произведения:', asizeof.asizeof((hex1 * hex2)))
    print()
    print('    После применения __slots__ ')
    hex3 = HexCalcOptClass ('A2')
    hex4 = HexCalcOptClass ('C4F')
    print('Размер числа hex1: ',asizeof.asizeof((hex3)))
    print('Размер числа hex2: ',asizeof.asizeof((hex4)))
    print('Размер результата сложения', asizeof.asizeof((hex3 + hex4)))
    print('Размер результата произведения:', asizeof.asizeof((hex3 * hex4)))


"""
Размер числа hex1:  264
Размер числа hex2:  264
Размер результата сложения 56
Размер результата произведения: 56

    После применения __slots__ 
Размер числа hex1:  96
Размер числа hex2:  96
Размер результата сложения 56
Размер результата произведения: 56

Теперь атрибуты класса хранятся в слотах (__slots__)а не в словаре (__dict__),
что позволяет экономить память.
Однако могут возникнуть проблемы с наследованием и 
множественным наследованием класса. 
"""
