"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

# Урок 2. Курс Алгоритмы.
# Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#

from memory_profiler import memory_usage
from memory_profiler import profile


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor  # Выполнение заняло 0.00390625 Mib. Результат: (1013, 976) при отключенном @profile.
# Это на три порядка меньше.
@profile
def even_odd_tup(my_num):
    my_number = tuple(my_num)
    num_tup = ('1', '3', '5', '7', '9')
    even = sum(1 for num in my_number if num in num_tup)
    odd = sum(1 for num in my_number if num not in num_tup)
    return odd, even
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявило.
    # Increment везде 0. Значение Mem usage не меняетя.


if __name__ == '__main__':
    my_num = str(sum(i ** i for i in range(700)))
    res_1, mem_diff_1 = even_odd_tup(my_num)
    print(f"Выполнение заняло {mem_diff_1} MiB. Результат: {res_1}")
