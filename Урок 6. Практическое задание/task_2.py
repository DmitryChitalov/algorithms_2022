"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage


def mem_info(func):
    def wrapper():
        m1 = memory_usage()
        result = func()
        m2 = memory_usage()
        memory_diff = m2[0] - m1[0]
        return result, memory_diff
    return wrapper


@mem_info
def check_mem():
    def revers(num=12368, num_str=''):
        if num == 0:
            print(num_str)
        else:
            num_next = num // 10
            num_tmp = num % 10
            num_str += str(num_tmp)
            return revers(num_next, num_str)
    return revers()


print(check_mem())


#декоратор срабатывает каждый раз при рекурсивном шаге,
#чтобы этого избежать можно обернуть рекурсивную функцию другой функцией.
