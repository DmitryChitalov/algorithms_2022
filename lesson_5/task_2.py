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

from collections import deque, defaultdict


# Первый вариант
def hex_nums():
    numbers = defaultdict(list)
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    sum_of_nums = hex(int(num1, 16) + int(num2, 16))[2:]
    product_of_nums = hex(int(num1, 16) * int(num2, 16))[2:]
    lst1 = list(deque(num1))
    lst2 = list(deque(num2))
    lst3 = list(deque(sum_of_nums))
    lst4 = list(deque(product_of_nums))
    numbers['Первое число'] = lst1
    numbers['Второе число'] = lst2
    numbers['Сумма чисел'] = lst3
    numbers['Произведение чисел'] = lst4
    return numbers


example = hex_nums()
print(example)


# Второй вариант
class HexNums:
    numbers = defaultdict(list)
    title = 'Первое число'
    selector = 0

    def __init__(self, numb):
        self.numb = numb
        self.digits_of_numb()

    def __add__(self, other):
        HexNums.selector = 1
        return HexNums(hex(int(self.numb, 16) + int(other.numb, 16))[2:])

    def __mul__(self, other):
        HexNums.selector = 2
        return HexNums(hex(int(self.numb, 16) * int(other.numb, 16))[2:])

    def __str__(self):
        return self.numb

    def digits_of_numb(self):
        lst = list(deque(self.numb))
        if HexNums.selector == 0:
            HexNums.numbers[HexNums.title] = lst
            HexNums.title = 'Второе число'
        if HexNums.selector == 1:
            HexNums.numbers['Сумма чисел'] = lst
            HexNums.selector = 0
        if HexNums.selector == 2:
            HexNums.numbers['Произведение чисел'] = lst
            HexNums.selector = 0


numb1 = input('Введите первое число: ')
numb2 = input('Введите второе число: ')
a = HexNums(numb1)
b = HexNums(numb2)
print(a)
a + b
a * b
print(HexNums.numbers)
