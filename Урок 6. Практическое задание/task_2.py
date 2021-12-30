"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
from memory_profiler import memory_usage


def dec(func):
    def wrapper(*args):
        start = memory_usage()

        res = func(*args)
        return f'Заняло пямяти = {memory_usage()[0] - start[0]}'

    return wrapper


@dec
def get_rev(n):
    return my_func(n)


def my_func(num, reversed=''):
    if num == 0:
        return reversed
    reversed += str(num % 10)
    return my_func(num // 10, reversed)


# print(get_rev(123123123))


"""
Пришел к выводу, что для профилировки нужно делать отдельную функцию,
которая вызывает функцию уже с рекурсией, чтобы замер использования памяти делался 
один раз.
"""