"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res
    return wrapper


@memory
def my_func(n):
    def count_num(num, even=0, odd=0):
        """Рекурсия"""
        if num == 0:
            return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
        else:
            if num % 10 % 2 == 0:
                even += 1
            elif num % 10 % 2 == 1:
                odd += 1
            return count_num(num//10, even, odd)
    return n


my_func(12345678)

"""
Выводится больше кол-во замеров в рекурсии. 
Решение - необходимо завернуть функцию в функцию.
"""