"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import memory_usage


def mib_size(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        return mem_dif, res

    return wrapper


@mib_size
def my_func(num, even=0, odd=0):
    if num == 0:
        return fr'Четные числа: {even}, Не четные числа: {odd}'
    if (num % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    return my_func(num // 10, even, odd)


if __name__ == '__main__':
    mem_dif_1, res_1 = my_func(23430)
    print(f'Выполнение заняло {mem_dif_1} Mib')

'''
Используя memory_usage, написал свой декоратор по замеру памяти mem_size,
и при помощи своего декоратора получилось замерить память всей рекурсивной функции,
а не отдельных шагов рекурсии.
Размер занимаемой памяти: 0.00390625 Mib
'''
