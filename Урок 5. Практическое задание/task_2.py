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
import collections
import operator
from functools import reduce

""" Collections solution """
def create_dict(num1: str, num2: str) -> collections.defaultdict:
    my_dict = collections.defaultdict(list)
    my_dict.setdefault("num1", list(num1))
    my_dict.setdefault("num2", list(num2))
    return my_dict

def dict_sum(instance):
    return list(hex(sum(map(lambda x: int("".join(x), 16), instance.values()))).replace("0x", "").upper())


def dict_multiplication(instance):
    return list(hex(reduce(operator.mul, map(lambda x: int("".join(x), 16), instance.values()), 1)).upper()[2:])


""" OOP solution """
class hexNum:
    def __init__(self, num: str):
        self.num = num

    def __mul__(self, other) -> list:
        return list(hex(int(self.num, 16) * int(other.num, 16)).upper()[2:])

    def __add__(self, other) -> list:
        return list(hex(int("".join(self.num), 16) + int("".join(other.num), 16)).upper()[2:])


if __name__ == "__main__":
    """ This is Collections """
    print("collections solution")
    hex_num1 = "A2" # input("Hex number1")
    hex_num2 = "C4F" # input("Hex number2")
    dict_instance = create_dict(hex_num1, hex_num2)
    print("sum: ", dict_sum(dict_instance))
    print("multiplication: ", dict_multiplication(dict_instance))

    """ This is OOP """
    print("*"*50)
    print("sum by OOP", hexNum(hex_num1) + hexNum(hex_num2))
    print("multiplication by OOP", hexNum(hex_num1) * hexNum(hex_num2))