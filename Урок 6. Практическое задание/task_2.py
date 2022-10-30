"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


@profile
def func_for_profile(number):

    def calculate_series(number):
        """
        подсчёт суммы n элементов следующего ряда чисел:
        1 -0.5 0.25 -0.125 ...
        """

        if number == 1:
            return 1

        return calculate_series(number - 1) / -2

    return calculate_series(number)


if __name__ == '__main__':
    nmb = 555
    print(f'Количество элементов: {nmb}, их сумма: {func_for_profile(nmb)}')

# Так как функция рекурсивная, то количество таблиц с замерами соответствует количеству вызовов
# Что бы получить одну таблицу с общим замером, оборачиваем функцию другой функцией и её уже замеряем.

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     15     19.3 MiB     19.3 MiB           1   @profile
#     16                                         def func_for_profile(number):
#     17
#     18     20.2 MiB      0.9 MiB         556       def calculate_series(number):
#     19                                                 """
#     20                                                 подсчёт суммы n элементов следующего ряда чисел:
#     21                                                 1 -0.5 0.25 -0.125 ...
#     22                                                 """
#     23
#     24     20.2 MiB      0.0 MiB         555           if number == 1:
#     25     20.2 MiB      0.0 MiB           1               return 1
#     26
#     27     20.3 MiB      0.0 MiB         554           return calculate_series(number - 1) / -2
#     28
#     29     20.3 MiB      0.0 MiB           1       return calculate_series(number)
#
#
# Количество элементов: 555, их сумма: 1.695830344760954e-167
