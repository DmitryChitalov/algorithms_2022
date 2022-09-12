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
# __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#

from memory_profiler import memory_usage
from memory_profiler import profile
from numpy import array
from pympler import asizeof


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


@decor  # При отключенном @profile Выполнение заняло 0.0 Mib. Результат: 761995
@profile
def gen_sum_to_num(input_num):  # для оптимизации памяти вместа рекурсии воспользовалась
    gen_sum = sum(i for i in range(input_num + 1))  # ленивыми вычислениями: генератором и функцией sum
    return gen_sum  # в результате оптимизации
    # снизилось на одну треть количество различных вызовов (Occurrences),
    # Increment во всех строках стал равен 0. Нет роста потребляемой памяти при вызове функции.
    # Значение Mem usage не меняетя. После окончания скрипта используемая память (Mem usage) не изменилась.
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявило.
    # Выполнение функции заняло практически втрое меньше мебибайт (с учетом работы @profile).


@profile
def arr_print_num(pr_num):
    my_arr_list = array(list(range(1, pr_num + 1)))
    print(f'array занимает {asizeof.asizeof(my_arr_list)} байт.')
    # при использовании функцию array() из библиотеки NumPy массив стал занимать почти в 10 раз меньше памяти.
    my_str = str(my_arr_list[0])
    for i in range(1, len(my_arr_list)):
        my_str = f'{my_str} + {str(my_arr_list[i])}'  # При использовании f строки, вместо сложения строк.
        # @profile указывает на рост Increment на 0,5 MiB. Это меньше, чем при сложении строк примерно на 20%.
        # Mem usage тоже возросла на 0,5 MiB. Это тоже меньше, чем при сложении строк примерно на 20%.
    return my_str


if __name__ == '__main__':
    inp_nam = 1234
    # sum_to_num_gen = gen_sum_to_num(inp_nam)
    mem_diff_gen, sum_to_num_gen = gen_sum_to_num(inp_nam)
    print(f"Выполнение заняло {mem_diff_gen} MiB. Результат: {sum_to_num_gen}")

    str_left_side_arr = arr_print_num(inp_nam)
    str_right_side = f'{inp_nam}({inp_nam}+1)/2'
    right_side = inp_nam * (inp_nam + 1) / 2

    left_side = sum_to_num_gen
    print(f'{str_left_side_arr} = {str_right_side}')
    print(f'left side: {str_left_side_arr} = {left_side}')
    print(f'right_side: {str_right_side} = {right_side}')
    print(f'left side = right_side : {left_side == right_side}')
