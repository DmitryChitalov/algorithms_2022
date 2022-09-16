#Это файл для первого скрипта

from memory_profiler import memory_usage
# четвертое задание второго дз с курса алгоритм


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return res

    return wrapper


@decor
def func_sum_n(x, i=0, res=0, num=1):
    if x != i:
        res += num
        num /= -2
        i += 1
        return func_sum_n(x, i, res, num)
    if x == i:
        return res


@decor
def func_sum_2(count, start=1, result=0):
    while count > 0:
        result += start
        count -= 1
        start /= -2
    else:
        return result


# func_sum_n(100)
# 0.25
# print('\n')
print(func_sum_2(100))
# 0.01171875
"""
цикл использует меньше памяти чем рекурсия, поэтому и применил цикл
рекурсия использует стек для хранения вызовов, поэтому она ест больше памяти
"""