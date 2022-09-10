"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile


def count_numbers(number, odd=0, even=0):
    if number == 0:
        return f'Количество чисел: чётных {even} , нечётных {odd}'
    else:
        num = number % 10
        if num % 2 == 1:
            odd += 1
        else:
            even += 1
        return count_numbers(number // 10, odd, even)


@profile
def my_func():
    user_num = int(input('Введите число: '))
    print(count_numbers(user_num))


my_func()


"""
При профилировании памяти рекурсивной функции напрямую,
будет выводится количество информации равное количеству вызовов рекурсии 
для решения этой проблемы можно вложить рекурсивную функцию в обычную функцию
и произвести профилирование

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    28     19.3 MiB     19.3 MiB           1   @profile
    29                                         def my_func():
    30     19.4 MiB      0.0 MiB           1       user_num = int(input('Введите число: '))
    31     19.4 MiB      0.0 MiB           1       print(count_numbers(user_num))
"""
