"""
Курс Основы Python, урок 5. Задание 2:
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.
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

n = int(input('Введите значение n: '))
odd_nums_gen = (n for n in range(1, n + 1, 2))
print((next(odd_nums_gen)))

# Для удобства замеров приведу это решение в виде функции


@memory
def odd_numb_gen(n):
    lst_odd_numb = (n for n in range(1, n + 1, 2))
    return lst_odd_numb


odd_numb_gen(125)
# 0.00390625 Mib

"""Выполним оптимизацию с использованием возможностей функции filter
Получлось уменьшить объём потребляемой памяти.
"""


@memory
def opti_odd_numb_gen(lst):
    lst_odd_numb = filter(lambda i: i in range(1, n + 1, 2), lst)
    return lst_odd_numb


opti_odd_numb_gen(list(range(125)))
# 0.0 Mib

