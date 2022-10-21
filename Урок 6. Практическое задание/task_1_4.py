"""
Задание 1.4.

"""
# Алгоритмы Python. DZ_2.4
# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...

from memory_profiler import memory_usage


def mem_usage(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение функции заняло {mem_diff} Mib")
        return res

    return wrapper


@mem_usage
def wrapper(num):
    def func(num_row, el_row=1.0, res=0.0):
        if num_row == 0:
            return res
        res = res + el_row
        el_row = (el_row / 2) * -1
        num_row -= 1
        return func(num_row , el_row, res)
    print(func(num))


@mem_usage
def func_opt(count, start=1.0, res=0.0):
    while count > 0:
        res += start
        count -= 1
        start /= -2
    else:
        print(res)


if __name__ == '__main__':
    wrapper(500)
    func_opt(500)

"""
0.6666666666666667
Выполнение функции заняло 0.6875 Mib
0.6666666666666667
Выполнение функции заняло 0.0 Mib

Вместо рекурсии применён цикл.
Кажется всё что угодно будет быстрее и эффективнее рекурсии, 
с её стеком для хранения вызовов.
"""
