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
def check_even_1(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0: 
            even.append(num*num)
    return even


if __name__ == '__main__':

    res, mem_diff = check_even_1(list(range(100000)))
    print(f"Выполнение заняло {mem_diff} Mib")

# Выполнение заняло 2.2890625 Mib
