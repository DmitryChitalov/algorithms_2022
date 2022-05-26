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


class MyHex:
    def __init__(self, hex_number_str):
        self.hex_number_str = hex_number_str.upper()
        self.hex_number = int(self.hex_number_str, 16)
        self.hex_number_list = [el for el in self.hex_number_str]

    @property
    def show_number(self):
        print(self.hex_number_str, self.hex_number_list, self.hex_number)

    def __add__(self, other):
        self.hex_number = self.hex_number + other.hex_number
        self.hex_number_str = hex(self.hex_number)[2:].upper()
        self.hex_number_list = [el for el in self.hex_number_str]

    def __mul__(self, other):
        self.hex_number = self.hex_number * other.hex_number
        self.hex_number_str = hex(self.hex_number)[2:].upper()
        self.hex_number_list = [el for el in self.hex_number_str]


def hex_calc_start():
    print('Вас приветствует калькулятор!\n'
          'Сложить 2 шестнадцатиричных чиса c ООП - введите 1\n'
          'Умножить 2 шестнадцатиричных чиса с ООП - введите 2\n'
          'Сложить 2 шестнадцатиричных чиса c collections - введите 3\n'
          'Умножить 2 шестнадцатиричных чиса с collections - введите 4\n'
          'Выход - введите любой символ!')
    try:
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        user_input = input('Введите выбор операции: ')
        if user_input == '1':
            hex_calc_class(first, second)
        elif user_input == '2':
            hex_calc_class(first, second, True)
        elif user_input == '3':
            hex_calc_collection(first, second)
        elif user_input == '4':
            hex_calc_collection(first, second, True)
        else:
            exit(0)
    except Exception as e:
        print(f'Что то пошло нетак! Ошибка {e}!')
    hex_calc_start()


def hex_calc_class(first, second, mult=False):
    first_num = MyHex(first)
    second_num = MyHex(second)
    print(f'Введенное первое число: {first_num.hex_number_list}')
    print(f'Введенное второе число: {second_num.hex_number_list}')
    if mult:
        first_num * second_num
    else:
        first_num + second_num
    print(f'Результат {"умножения" if mult else "сложения"} двух чисел: {first_num.hex_number_list}')


def hex_calc_collection(first, second, mult=False):
    number_dict = defaultdict(str)
    number_dict[first] = [el for el in first]
    number_dict[second] = [el for el in second]
    print(f'Введенное первое число: {number_dict[first]}')
    print(f'Введенное второе число: {number_dict[second]}')
    if mult:
        third_temp = int(first, 16) * int(second, 16)
    else:
        third_temp = int(first, 16) + int(second, 16)
    third = hex(third_temp).upper()[2:]
    number_dict[third] = [el for el in third]
    print(f'Результат {"умножения" if mult else "сложения"} двух чисел: {number_dict[third]}')


if __name__ == '__main__':
    hex_calc_start()

"""
Как по мне, особые коментарии излишни, больше понравилось решение через ООП
"""