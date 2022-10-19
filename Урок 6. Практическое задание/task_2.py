"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


# Функция с урока 2, задание 4, курс Алгоритмы
@profile
def sum_of_numbers(quantity, number=1):
    if quantity == 1:
        return number
    else:
        return number + sum_of_numbers(quantity - 1, number / -2)


# user_input = int(input("Введите количество элементов: "))
# print(sum_of_numbers(user_input))
"""
Из-за того, что функция sum_of_numbers является рекурсивной, 
мы получаем столько таблиц с замерами памяти, сколько раз функция вызывает сама себя.
Обернем рекурсивную функцию в обычную функцию, чтобы получить одну таблицу с замерами памяти.
"""


@profile
def wrapper(var):
    def sum_of_numbers(quantity, number=1):
        if quantity == 1:
            return number
        else:
            return number + sum_of_numbers(quantity - 1, number / -2)

    return sum_of_numbers(var)


user_input = int(input("Введите количество элементов: "))
print(wrapper(user_input))

"""
Введите количество элементов: 3

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     19.9 MiB     19.9 MiB           1   @profile
    33                                         def wrapper(var):
    34     19.9 MiB      0.0 MiB           4       def sum_of_numbers(quantity, number=1):
    35     19.9 MiB      0.0 MiB           3           if quantity == 1:
    36     19.9 MiB      0.0 MiB           1               return number
    37                                                 else:
    38     19.9 MiB      0.0 MiB           2               return number + sum_of_numbers(quantity - 1, number / -2)
    39     19.9 MiB      0.0 MiB           1       return sum_of_numbers(var)
"""
