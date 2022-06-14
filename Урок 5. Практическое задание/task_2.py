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


