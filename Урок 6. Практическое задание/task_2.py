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
def func(number):
    def rec_calc(num, odd=0, even=0):
        """ Подсчет нечетных цифр"""
        if num < 1:
            return even, odd
        if num % 2:
            odd += 1
        else:
            even += 1
        return rec_calc(num // 10, odd, even)
    return rec_calc(number)


numb = int(input("Введите число: "))
print(f'Количество четных и нечетных цифр равно: {func(numb)}')

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14     19.4 MiB     19.4 MiB           1   @profile
    15                                         def func(number):
    16     19.4 MiB      0.0 MiB           8       def rec_calc(num, odd=0, even=0):
    17                                                 " Подсчет нечетных цифр"
    18     19.4 MiB      0.0 MiB           7           if num < 1:
    19     19.4 MiB      0.0 MiB           1               return even, odd
    20     19.4 MiB      0.0 MiB           6           if num % 2:
    21     19.4 MiB      0.0 MiB           3               odd += 1
    22                                                 else:
    23     19.4 MiB      0.0 MiB           3               even += 1
    24     19.4 MiB      0.0 MiB           6           return rec_calc(num // 10, odd, even)
    25     19.4 MiB      0.0 MiB           1       return rec_calc(number)
"""

"""
при профилировании рекурсивной функции напрямую, профилируется каждый ее запуск.
Для полных замеров, рекурсивную функцию оборачиваем ее в другую функцию.
"""
