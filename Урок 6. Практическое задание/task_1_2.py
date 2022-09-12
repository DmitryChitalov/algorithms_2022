"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""

# Урок 5. Курс Алгоритмы.
# Задание 2.
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# 1) через collections
#
# defaultdict(list)
# int(, 16)
# reduce

import numpy as np
from collections import defaultdict
from functools import reduce
from memory_profiler import profile
from numpy import array
from pympler import asizeof

MY_DEF_DIC = defaultdict(list)
MY_DEF_DIC_ARR = defaultdict(array)


@profile
def add_nums():
    """Для ввода шестнадцатеричного числа и помещения его в словарь MY_DEF_DIC"""
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    # inp_num = input('Введите число: ')
    inp_num = "C4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4FC4F"
    MY_DEF_DIC[inp_num] = list(inp_num)
    #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
    #  при использовании функции array() из библиотеки NumPy.
    print(f'Число сохранено : {MY_DEF_DIC[inp_num]}')
    print(f'Число в list заняло {asizeof.asizeof(MY_DEF_DIC[inp_num])} байт памятию')


@profile
def add_nums_arr():
    """Для ввода шестнадцатеричного числа и помещения его в словарь MY_DEF_DIC"""
    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    # inp_num = input('Введите число: ')
    inp_num = str(sum(i ** i for i in range(700)))
    MY_DEF_DIC_ARR[inp_num] = array(list(inp_num))
    #  При использовании функции array() из библиотеки NumPy
    #  массив стал занимать более, чем в 2 раза меньше места в памяти.
    print(f'Число сохранено : {MY_DEF_DIC_ARR[inp_num]}')
    print(f'Число в array заняло {asizeof.asizeof(MY_DEF_DIC_ARR[inp_num])} байт.')


@profile
def sum_nums(my_dic):
    """Для сложения двух шестнадцатеричных чисел, находящихчя в словаре MY_DEF_DIC"""
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    if len(my_dic) == 2:
        sum_two = reduce(
            lambda x, y: hex(int(''.join(my_dic[x]), 16) + int(''.join(my_dic[y]), 16)).upper(), my_dic)
        sum_num = list(sum_two)[2:]
        #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
        #  при использовании функции array() из библиотеки NumPy.
        print(f'Сумма в list заняла {asizeof.asizeof(sum_num)} байт.')
    elif len(my_dic) == 1:
        for key in my_dic.keys():
            sum_num = list(hex(int(key, 16) + int(key, 16)).upper())[2:]
            #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
            #  при использовании функции array() из библиотеки NumPy.
            print(f'Сумма в list заняла {asizeof.asizeof(sum_num)} байт.')
    else:
        sum_num = "Не считаю. Вы ввели больше, чем 2 числа."
    return sum_num


@profile
def sum_nums_arr(my_dic):
    """Для сложения двух шестнадцатеричных чисел, находящихчя в словаре MY_DEF_DIC"""
    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    if len(my_dic) == 2:
        sum_two = reduce(
            lambda x, y: hex(int(''.join(my_dic[x]), 16) + int(''.join(my_dic[y]), 16)).upper(), my_dic)
        sum_num_new = array(list(sum_two)[2:])
        # При использовании функции array() из библиотеки NumPy
        #  массив стал занимать более, чем в 2 раза меньше места в памяти.
        print(f'Сумма в array заняла {asizeof.asizeof(sum_num_new)} байт.')
    elif len(my_dic) == 1:
        for key in my_dic.keys():
            sum_num_new = array(list(hex(int(key, 16) + int(key, 16)).upper())[2:])
            # При использовании функции array() из библиотеки NumPy
            #  массив стал занимать более, чем в 2 раза меньше места в памяти.
            print(f'Сумма в array заняла {asizeof.asizeof(sum_num_new)} байт.')
    else:
        sum_num_new = "Не считаю. Вы ввели больше, чем 2 числа."
    return sum_num_new


@profile
def mul_nums(my_dic):
    """Для умножения двух шестнадцатеричных чисел, находящихчя в словаре MY_DEF_DIC"""
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    if len(my_dic) == 2:
        mul_two = reduce(
            lambda x, y: hex(int(''.join(my_dic[x]), 16) * int(''.join(my_dic[y]), 16)).upper(), my_dic)
        mul_num = list(mul_two)[2:]
        #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
        #  при использовании функции array() из библиотеки NumPy.
        print(f'Произведение в list заняло {asizeof.asizeof(mul_num)} байт.')
    elif len(my_dic) == 1:
        for key in my_dic.keys():
            mul_num = list(hex(int(key, 16) ** 2).upper())[2:]
            #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
            #  при использовании функции array() из библиотеки NumPy.
            print(f'Произведение в list заняло {asizeof.asizeof(mul_num)} байт.')
    else:
        mul_num = "Не считаю. Вы ввели больше, чем 2 числа."
    return mul_num


@profile
def mul_nums_arr(my_dic):
    """Для умножения двух шестнадцатеричных чисел, находящихчя в словаре MY_DEF_DIC"""
    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    if len(my_dic) == 2:
        mul_two = reduce(
            lambda x, y: hex(int(''.join(my_dic[x]), 16) * int(''.join(my_dic[y]), 16)).upper(), my_dic)
        mul_num_new = array(list(mul_two)[2:])
        #  При использовании функции array() из библиотеки NumPy
        #  массив стал занимать более, чем в 2 раза меньше места в памяти.
        print(f'Произведение в array заняло {asizeof.asizeof(mul_num_new)} байт.')
    elif len(my_dic) == 1:
        for key in my_dic.keys():
            mul_num_new = array(list(hex(int(key, 16) ** 2).upper())[2:])
            #  При использовании функции array() из библиотеки NumPy
            #  массив стал занимать более, чем в 2 раза меньше места в памяти.
            print(f'Произведение в array заняло {asizeof.asizeof(mul_num_new)} байт.')
    else:
        mul_num_new = "Не считаю. Вы ввели больше, чем 2 числа."
    return mul_num_new


if __name__ == '__main__':
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    print("Введите два шестнадцатеричных числа.")
    add_nums()
    add_nums()
    print(f'Сумма чисел: {sum_nums(MY_DEF_DIC)}')
    print(f'Произведение - {mul_nums(MY_DEF_DIC)}')
    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    print("Введите два шестнадцатеричных числа.")
    add_nums_arr()
    add_nums_arr()
    print(f'Сумма чисел: {sum_nums_arr(MY_DEF_DIC_ARR)}')
    print(f'Произведение - {mul_nums_arr(MY_DEF_DIC_ARR)}')
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявляет.
    # Increment везде 0. Значение Mem usage не меняетя.
