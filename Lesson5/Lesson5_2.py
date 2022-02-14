from collections import defaultdict


class Hex:
    def __init__(self, name):
        self.name = name

    def _def_dic(self):
        d = defaultdict(list)
        for i in self.name:
            d[self.name].append(i)
        return d[self.name]

    def __add__(self, other):
        result = str(Hex(hex(int(self.name, 16) + int(other.name, 16)))).replace("0x", "").upper()
        d = defaultdict(list)
        for i in result:
            d[result].append(i)
        return d[result]

    def __mul__(self, other):
        result = str(Hex(hex(int(self.name, 16) * int(other.name, 16)))).replace("0x", "").upper()
        d = defaultdict(list)
        for i in result:
            d[result].append(i)
        return d[result]

    def __str__(self):
        return f'{self.name}'


a = input("Введите число: ")
b = input("Введите число: ")
a1 = Hex(a)
b1 = Hex(b)
print(f'Сумма чисел равна: {a1 + b1}')
print(f'Произведение чисел равно: {a1 * b1}')
