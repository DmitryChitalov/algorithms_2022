from memory_profiler import memory_usage

'''
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.

0.125 рекурсия(стэк)
0.0 обычная функция
'''

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper

@decor
def func(n, s=0):
    if n == 0:
        return s
    else:
        s += n
        return func(n-1, s)

@decor
def func_2(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


n = 100
print(func(n))
print(func_2(n))





