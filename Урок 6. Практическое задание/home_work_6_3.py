from numpy import array, where
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
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


NUMS = [el for el in range(100000000)]


if __name__ == '__main__':
    res, mem_diff = func_1(NUMS)
    print(f"Выполнение заняло {mem_diff} Mib")


# Оптимизирую заполнение массива с помощью модуля numpy
@decor
def func_2(nums):
    intarray = array(nums)
    return where(intarray % 2 == 0)


if __name__ == '__main__':
    res, mem_diff = func_2(NUMS)
    print(f"Выполнение с использованием {mem_diff} Mib")


'''
Выполнение заняло 1514.65625 Mib
Выполнение заняло 101.171875 Mib
Экономия памяти очевидна.
'''



