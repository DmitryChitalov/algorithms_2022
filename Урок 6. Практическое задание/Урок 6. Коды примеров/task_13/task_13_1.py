"""Профилирование времени и памяти"""

from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def check_even_1(lst):
    # списковое включение
    new_list = [str(i) for i in lst]
    return new_list


if __name__ == '__main__':

    res, mem_diff = check_even_1(list(range(100000)))
    print(f"Выполнение заняло {mem_diff} Mib")

# Выполнение заняло 8.33984375 Mib
