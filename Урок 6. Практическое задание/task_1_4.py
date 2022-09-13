"""
Курс "Алгоритмы и структуры данных на Python. Базовый курс".
Урок 2 "Циклы. Рекурсия. Функции". Задание 7.
Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


# https://github.com/DmitryChitalov/algorithms_2022/pull/853
@decor
def theorem(n):
    def theorem_1(n, sum_n=0):
        if n < 1:
            return sum_n
        return theorem_1(n - 1, sum_n + n)

    return f'{theorem_1(n)} - левая часть равенства,\n{int(n * (n + 1) / 2)} - правя часть равенства'


# Обновлённый вариант
@decor
def theorem_adv(n):
    sum_n = 0
    for i in range(n + 1):
        sum_n += i
    return f'{sum_n} - левая часть равенства,\n{int(n * (n + 1) / 2)} - правя часть равенства'


res, mem_diff = theorem(500)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.5078125 Mib
print('----------------- Новый вариант -----------------')
res, mem_diff = theorem_adv(500)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.0 Mib

"""
Отказ от рекурсии в пользу цикла позволил более эффективно задействовать ресурсы памяти.
"""
