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

Это файл для первого скрипта
"""

# Урок 2. Курс Алгоритмы.
# Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#

from memory_profiler import memory_usage
from memory_profiler import profile
from numpy import array
from pympler import asizeof
from sys import setrecursionlimit

setrecursionlimit(10000)


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff, res

    return wrapper


def enter_a_number():
    my_flag = True
    while my_flag:
        try:
            my_number = int(input('Введите число: '))
            my_flag = False
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
    return my_number


@decor  # При отключенном @profile Выполнение заняло 1.26953125 MiB. Результат: 761995
@profile
def inside_sum_to_num(my_num):
    def sum_to_num(input_num):  # @profile указывает на рост потребляемой памяти (Increment) на 1,7 - 1,8 MiB
        if input_num == 1:
            return 1
        return input_num + sum_to_num(input_num - 1)

    return sum_to_num(my_num)  # используемая память (Mem usage) после выполнения функцмм возросла.


@profile
def print_num(pr_num):
    my_list = list(range(1, pr_num + 1))
    print(f'list занимает {asizeof.asizeof(my_list)} байт.')
    # массив занимает почти в 10 раз больше памяти, чем при использовании функцию array() из библиотеки NumPy.
    my_str = str(my_list[0])
    for i in range(1, len(my_list)):
        my_str = my_str + ' + ' + str(my_list[i])
        # При сложении строк @profile указывает на рост Increment на 0,6 - 0,7 MiB.
        # Mem usage тоже возростает на 0,6 - 0,7 MiB.
        # Это больше, чем при использовании f-строк примерно на 20%.
    return my_str


if __name__ == '__main__':
    inp_nam = 1234
    # sum_to_num = inside_sum_to_num(inp_nam)
    mem_diff, sum_to_num = inside_sum_to_num(inp_nam)
    print(f"Выполнение заняло {mem_diff} MiB. Результат: {sum_to_num}")

    str_left_side = print_num(inp_nam)
    str_right_side = f'{inp_nam}({inp_nam}+1)/2'
    right_side = inp_nam * (inp_nam + 1) / 2
    left_side = sum_to_num
    print(f'{str_left_side} = {str_right_side}')

    print(f'left side: {str_left_side} = {left_side}')
    print(f'right_side: {str_right_side} = {right_side}')
    print(f'left side = right_side : {left_side == right_side}')
