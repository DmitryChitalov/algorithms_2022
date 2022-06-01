"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


from memory_profiler import profile
# Обернем функцию с рекурсией для получения замера

@profile
def number_reverse(num):
    if num < 10:
        return num
    else:
        return str(num % 10) + str(number_reverse(num // 10))

if __name__ == '__main__':
    number_reverse(2348972389751892735)


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     17     28.1 MiB     28.1 MiB          19   @profile
#     18                                         def number_reverse(num):
#     19     28.1 MiB      0.0 MiB          19       if num < 10:
#     20     28.1 MiB      0.0 MiB           1           return num
#     21                                             else:
#     22     28.1 MiB      0.0 MiB          18           return str(num % 10) + str(number_reverse(num // 10))