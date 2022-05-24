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


class HexNumber:

    def __init__(self, h):
        self.hex = [*h.upper()]
        self.hex_d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        self.dec_h = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5:'5', 6:'6', 7: '7', 8: '8',
                      9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def to_10(self, hex):
        self.hex = hex
        self.dec = 0
        n = 0
        for i in self.hex[::-1]:
            self.dec = self.dec + self.hex_d[i] * (16 ** n)
            n += 1
        return self.dec

    def to_16(self, dec):
        self.dec = dec
        self.hex = []
        while self.dec != 0:
            if self.dec < 16:
                self.hex.insert(0, (self.dec_h[self.dec]))
                break
            n1 = self.dec // 16
            self.hex.insert(0, (self.dec_h[(self.dec - (n1 * 16))]))
            self.dec = n1
        return self.hex

    def __add__(self, other):
        self.rez = self.to_10(self.hex) + self.to_10(other.hex)
        return self.to_16(self.rez)

    def __mul__(self, other):
        self.rez = self.to_10(self.hex) * self.to_10(other.hex)
        return self.to_16(self.rez)


if __name__ == '__main__':
    hex1 = HexNumber ('a2')
    hex2 = HexNumber ('c4f')
    print(hex1 + hex2)
    print(hex1 * hex2)


## К сожалению не понятно как решать через defaultdict(((




