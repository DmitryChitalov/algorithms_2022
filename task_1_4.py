# Задача: подсчитать четные и нечетные цифры введенного натурального числа. (Алгоритмы - урок 2)

from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def even_odd_amount(num, even_nums, odd_nums):
    if num == 0:
        return even_nums, odd_nums
    else:
        num = int(num)
        last_num = num % 10
        if last_num % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1
        return even_odd_amount(num // 10, even_nums, odd_nums)


try:
    test_1 = even_odd_amount('123456789654123589654741258', 0, 0)
    print(test_1)
except ValueError:
    print('Нужно вводить числа')

# Вместо рекурсии - цикл. Рекурсия -  0.0625 Mib, цикл - 0.0 Mib


@decor
def even_odd_amount_2(num):
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


try:
    test_2 = even_odd_amount_2('23456789654123589654741258')
    print(test_2)
except ValueError:
    print('Нужно вводить числа')
