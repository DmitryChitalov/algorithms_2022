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
from functools import reduce


# Решение через ООПС
class HexNum:

    def __init__(self, digits):
        """
        Функция инициализации класса, в качестве аргумента требует список цифр.
        """
        self.digits = digits

    def from_str(input_str):
        """
        Метод возвращает список символов для представления 16-ричного числа.
        Все буквенные символы переводятся в заглавные.
        В качестве аргумента берет строку.
        """
        return HexNum(list(input_str.upper()))

    def __add__(self, other):
        """
        Метод возвращает экземпляр класса, который является суммой двух таковых.
        """
        result = hex(int(''.join(self.digits), 16) +
                     int(''.join(other.digits), 16))
        return HexNum.from_str(str(result)[2:])

    def __mul__(self, other):
        """
        Метод возвращает экземпляр класса, который является произведением двух таковых.
        """
        result = hex(int(''.join(self.digits), 16) *
                     int(''.join(other.digits), 16))
        return HexNum.from_str(str(result)[2:])

    def __str__(self):
        """
        Перегруженный магический метод для удобного вывода через print.
        """
        return f'{self.digits}'


# Решение через defaultdict
def hex_lst_from_str(input_str):
    """
    Функция возвращает список символов для представления 16-ричного числа.
    Все буквенные символы переводятся в заглавные.
    В качестве аргумента берет строку.
    """
    return list(input_str.upper())


def hex_pair_sum(hex_nums):
    """
    Функция сумму всех числе из заданного словаря в виде списка.
    """
    summ = sum([int(''.join(lst), 16) for lst in hex_nums.values()])
    return hex_lst_from_str(str(hex(summ))[2:])


def hex_pair_mul(hex_nums):
    """
    Функция произведение всех числе из заданного словаря в виде списка.
    """
    summ = reduce(
        lambda a, b: a * b,
        [int(''.join(lst), 16) for lst in hex_nums.values()]
    )
    return hex_lst_from_str(str(hex(summ))[2:])


# Проверка решения через ООП
a = HexNum.from_str('16C')
b = HexNum.from_str('F')
print(a + b)
print(a * b)

# Проверка решения через defaultdict
hex_nums = defaultdict(list)
hex_nums['A'] = ['16C']
hex_nums['B'] = ['F']
print(hex_pair_sum(hex_nums))
print(hex_pair_mul(hex_nums))
