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

class HexCalcClass:
    def __init__(self, n):
        self.val = n

    def __add__(self, other):
        add = str(hex(int(self.val, 16) + int(other.val, 16)))
        return add[2:].upper()

    def __mul__(self, other):
        mul = str(hex(int(self.val, 16) * int(other.val, 16)))
        return mul[2:].upper()

if __name__ == '__main__':
    hex1 = HexCalcClass ('A2')
    hex2 = HexCalcClass ('C4F')
    print('Cложение чисел:    ', hex1 + hex2)
    print('Произведение чисел:', hex1 * hex2)


"""
Cложение чисел:     CF1
Произведение чисел: 7C9FE
"""
