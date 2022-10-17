"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile

"""less_2_task_3"""


@profile()
def wrapped(number):
    def reverse_numbers(data):
        last_num = data % 10
        first_num = data // 10
        if data == 0:
            return ""

        return str(last_num) + reverse_numbers(first_num)

    return reverse_numbers(number)


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     18     18.7 MiB     18.7 MiB           1   @profile()
#     19                                         def wrapped(number):
#     20     18.7 MiB      0.0 MiB           8       def reverse_numbers(data):
#     21     18.7 MiB      0.0 MiB           7           last_num = data % 10
#     22     18.7 MiB      0.0 MiB           7           first_num = data // 10
#     23     18.7 MiB      0.0 MiB           7           if data == 0:
#     24     18.7 MiB      0.0 MiB           1               return ""
#     25
#     26     18.7 MiB      0.0 MiB           6           return str(last_num) + reverse_numbers(first_num)
#     27
#     28     18.7 MiB      0.0 MiB           1       return reverse_numbers(number)
#
#
# 005001

user_choice = int(input("Введите число для реверса: "))
print(wrapped(user_choice))

"""Проблема замера расходования памяти при работе скрипта с рекурсией состоит в том, что скрипт постоянно
самовызывается, провоцируя очередной замер профайлера. Чтобы этого избежать, как и обсуждалось на уроке,
обернём скрипт с рекурсией в отдельную функцию-обёртку для единого замера расхода RAM"""
