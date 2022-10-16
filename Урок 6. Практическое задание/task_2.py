"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.

Анализ:
При попытке измерения памяти рекурсивной функции (@memory  line 57 )
выдается занятие памяти на каждой итерации, но не общее потребление памяти при работе всей функции

Чтобы оценить занятие памяти при работе всей функции нужно измерять память не функции рекурсии,
а на более высоком уровне, например (@memory  line 50 ) , или создать функцию - wrapper.

Script listing:
функция recursive_reverse
Number = 123456789
Reverse number = 987654321
Выполнение заняло 0.0078125 Mib

Process finished with exit code 0
"""


from timeit import timeit
from random import randint
from cProfile import run
from memory_profiler import memory_usage
from memory_profiler import profile


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f" Выполнение заняло {mem_diff} Mib")
        return res
    return wrapper


@memory
# @profile
def print_output():
    print(f'Reverse number = {recursive_reverse(num_10000)}')


# @profile
# @memory
def recursive_reverse(number):
    # print(number)
    if number == 0:
        # s1 = str(number % 10)
        # print (f'str(number % 10) = {s1}')
        # print(f'returnback ')
        return ""
    s1 = str(number % 10)
    s2 = recursive_reverse(number // 10)
    # print (f'return {s1}  {s2}')
    return f'{s1}{s2}'



num_10000 = 123456789

print('Function recursive_reverse')
print(f'Number = {num_10000}')
# print(f'Reverse number = {recursive_reverse(num_10000)}')
print_output()





