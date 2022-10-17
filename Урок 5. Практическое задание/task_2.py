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

# Hexadecimal_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

num_1 = 'A2'
num_2 = 'C4F'
addition = hex(int(num_1, 16) + int(num_2, 16))
multiplication = hex(int(num_1, 16) * int(num_2, 16))
print(addition)
print(multiplication)


def hexadecimal_calc():
    final_dict = defaultdict(list)
    num_dict = defaultdict(list)
    num_1 = input("Введите первое шестнадцатеричное число: ")
    num_2 = input("Введите второе шестнадцатеричное число: ")
    # num_1 = 'A2'
    # num_2 = 'C4F'
    num_dict[1] = num_1
    num_dict[2] = num_2
    el_addition = list(hex(int(num_dict[1], 16) + int(num_dict[2], 16))[2:])
    el_multiplication = list(hex(int(num_dict[1], 16) * int(num_dict[2], 16))[2:])
    final_dict[1] = el_addition
    final_dict[2] = el_multiplication
    print(f'Результат сложения {final_dict[1]}')
    print(f'Результат умножения {final_dict[2]}')


hexadecimal_calc()


class Hexadecimal_calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self):
        return list(hex(int(self.num_1, 16) + int(self.num_2, 16))[2:])

    def __mul__(self):
        return list(hex(int(self.num_1, 16) * int(self.num_2, 16))[2:])


def hexadecimal_calc_2():
    final_dict = defaultdict(list)
    num_dict = defaultdict(list)
    num_1 = str(input("Введите первое шестнадцатеричное число: "))
    num_2 = str(input("Введите второе шестнадцатеричное число: "))
    # num_1 = 'A2'
    # num_2 = 'C4F'
    num_dict[1] = num_1
    num_dict[2] = num_2
    result = Hexadecimal_calculator(num_dict[1], num_dict[2])
    final_dict['Результат сложения'] = Hexadecimal_calculator.__add__(result)
    final_dict['Результат умножения'] = Hexadecimal_calculator.__mul__(result)
    print(final_dict)


if __name__ == '__main__':
    hexadecimal_calc_2()

# Готово