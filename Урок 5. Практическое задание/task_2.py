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
from collections import defaultdict

hexadecimal_d = defaultdict(list)


# 1
def hexadecimal_calc():
    try:
        operations_number = int(input('Enter the number of operations: '))
    except ValueError:
        print('You must enter a number, not a string')
        return
    for i in range(operations_number):
        first_hexa = input('Enter the first hexadecimal number: ').upper()
        second_hexa = input('Enter the second hexadecimal number: ').upper()
        hexadecimal_d[first_hexa] = list(first_hexa)
        hexadecimal_d[second_hexa] = list(second_hexa)
        operator = input('Enter + or *: ')
        if operator == '+':
            operation = str(hex(int(''.join(hexadecimal_d[first_hexa]), 16) +
                            int(''.join(hexadecimal_d[second_hexa]), 16)))
            result = operation[2:].upper()
            hexadecimal_d[result] = list(result)
            print(hexadecimal_d[result])
        elif operator == '*':
            operation = str(hex(int(''.join(hexadecimal_d[first_hexa]), 16) *
                                int(''.join(hexadecimal_d[second_hexa]), 16)))
            result = operation[2:].upper()
            hexadecimal_d[result] = list(result)
            print(hexadecimal_d[result])
        else:
            print('You must enter + or *, not something else')
            return
    return


hexadecimal_calc()


# 2
class HexadecimalCalc:
    def __init__(self, h):
        self.hexadecimal = h

    def __add__(self, other):
        add = str(hex(int(self.hexadecimal, 16) + int(other.hexadecimal, 16)))
        return add[2:].upper()

    def __mul__(self, other):
        mul = str(hex(int(self.hexadecimal, 16) * int(other.hexadecimal, 16)))
        return mul[2:].upper()


first_hexadec = HexadecimalCalc('a2')
second_hexadec = HexadecimalCalc('c4f')
print(first_hexadec + second_hexadec)
print(first_hexadec * second_hexadec)
