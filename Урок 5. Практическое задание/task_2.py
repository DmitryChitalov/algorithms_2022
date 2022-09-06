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


class HexNumOper:
    def __init__(self, num):
        self.num = num
        self.num_hex = hex(int(num, 16))
        self.num_hex_arr = [char.upper() for char in str(self.num_hex)[2:]]
        self.sum_arr = []

    def __add__(self, other):
        sum_hex = hex(int(self.num, 16) + int(other.num, 16))
        sum_arr = [char.upper() for char in str(sum_hex)[2:]]
        return sum_arr

    def __mul__(self, other):
        mul_hex = hex(int(self.num, 16) * int(other.num, 16))
        mul_arr = [char.upper() for char in str(mul_hex)[2:]]
        return mul_arr


def fill_dict(num):
    num_str = str(hex(int(num, 16)))[2:]
    num_arr = [char.upper() for char in num_str]
    dict_1[num].append(num_arr)


dict_1 = defaultdict(list)
f_num = input("Введите первое шестнадцатиричное число (в латинской раскладке): ")
s_num = input("Введите второе шестнадцатиричное число (в латинской раскладке): ")

# Вариант 1. Через коллекции.

fill_dict(f_num)
fill_dict(s_num)

sum1 = str(hex(int(f_num, 16) + int(s_num, 16)))[2:]
mul1 = str(hex(int(f_num, 16) * int(s_num, 16)))[2:]

fill_dict(sum1)
fill_dict(mul1)

print(f"Первое число: {dict_1[f_num][0]} \nВторое число: {dict_1[s_num][0]} \n"
      f"Сумма чисел: {dict_1[sum1][0]} \nПроизведение чисел:  {dict_1[mul1][0]}")

# Вариант 2. Через ООП

f_num2 = HexNumOper(f_num)
s_num2 = HexNumOper(s_num)

print(f"Первое число: {f_num2.num_hex_arr} \nВторое число: {s_num2.num_hex_arr} \n"
      f"Сумма чисел: {f_num2 + s_num2} \nПроизведение чисел:  {f_num2 * s_num2}")
