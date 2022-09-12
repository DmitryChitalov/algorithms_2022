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

class Hexadec: # Не умеет работать с отрицательными числами и числами с запятой.

    dct = { # нужен для перевода в десятичную систему и обратно
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    def __init__(self, str):
        self.lst = list(str.upper()) #сразу превратим в список. По хорошему надо было бы убрать нули в начале строки, если они были.

        for i in range(len(self.lst)): #Если в строке есть буквы кроме ABDCEF поднимем ошибку.
            if self.lst[i] not in self.dct:
                raise ValueError

        dec = 0 # для удобства будем хранить десятичное представление в self.dec.
        # Через него будем умножать и складывать. Можно (нужно) было написать функцию.
        hex_reverse = []
        for i in range(len(self.lst)):
            hex_reverse.insert(0, self.lst[i])
        for i in range(len(hex_reverse)):
            dec = dec + self.dct[hex_reverse[i]] * 16**i
        self.dec = dec


    def dec_to_hex(self, num): # для перевода десятичного представление в шестнадцатиричное
        hex_lst = []
        while num != 0:
            for key, val in self.dct.items():
                if divmod(num, 16)[1] == val:
                    hex_lst.insert(0, key)
            num = divmod(num, 16)[0]
        return hex_lst

    def __add__(self, other):
        return Hexadec.dec_to_hex(self, self.dec + other.dec)


    def __mul__(self, other):
        return Hexadec.dec_to_hex(self, self.dec * other.dec)

    def __str__(self):
        hex_str = "[" #Превращаем в строку, которая выглядит как список, чтоб можно было вызвать функцией print()
        for i in range(len(self.lst)):
            hex_str = hex_str + f"'{self.lst[i]}', "
        return hex_str[:-2]+']'









try:
    number0 = Hexadec('fgh')
except ValueError:
    print(f'Неверное шестнадцатиричное число')

number = Hexadec('c4f')
number2 = Hexadec('a2')
print(number)
print(number2)
print(number + number2)
print(number * number2)



# print(divmod(3151, 16))
# print(divmod(196, 16))
# print(divmod(12, 16))

#print(hec(3151))