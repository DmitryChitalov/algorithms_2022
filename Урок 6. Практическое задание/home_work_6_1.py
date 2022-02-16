'''
Из задания 4.1  взят код, который позволяет сохранить в массиве индексы четных элементов другого массива.
Мы там оптимизировали код и делали замеры времени выполнения кода с помощью модуля timeit.
Теперь смотрим память.
'''

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


if __name__ == '__main__':
    res, mem_diff = func_1(list(range(10000)))
    print(f"Выполнение заняло {mem_diff} Mib")


# Оптимизирую с помощью метода ленивых вычислений (генератора), без хранения массива
@decor
def func_3(nums):
    for num in nums:
        if num % 2 == 0:
            #генератор:
            yield num


if __name__ == '__main__':

    my_generator, mem_diff = func_3(list(range(10000)))
    print(f"Выполнение заняло {mem_diff} Mib")
#    for i in my_generator:
#        print(i)

'''
Выполнение заняло 0.18359375 Mib
Выполнение заняло 0.0 Mib - заполнение массива с помощью генератора занимает меньше всего памяти.
'''