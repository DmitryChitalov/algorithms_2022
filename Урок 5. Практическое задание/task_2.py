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

class HexOperation:
    def __init__(self, numb_1, numb_2):
        self.numb_1 = numb_1
        self.numb_2 = numb_2
    
    def __add__(self, other):
        return list(hex(int(''.join(self.numb_1), 16) + int(''.join(other.numb_2), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.numb_1), 16) * int(''.join(other.numb_2), 16)))[2:]

hex_num_1 = list(input("Введите первое шестнадцатеричное число: "))
hex_num_2 = list(input("Введите второе шестнадцатеричное число: "))

sum_hex_num = HexOperation(hex_num_1, hex_num_2) + HexOperation(hex_num_1, hex_num_2)

mult_hex_num = HexOperation(hex_num_1, hex_num_2) * HexOperation(hex_num_1, hex_num_2)

print(f'Сумма числел равно: {sum_hex_num}')

print(f'Произведение числел равно: {mult_hex_num}')


