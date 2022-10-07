"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект

Аналитика:
сделал задачу 4 способами:
1.  Цикл for + appent                                   0.0006823000000000003
2. list comprehension                                   0.0007577
3. с использованием итератора                           0.0010196000000000024
4. с использованием  list concatination + enumerate     0.0006533000000000025

самый быстрый способ с enumerate
самый медленный способ  с использованием итератора

"""


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
#    new_arr = [i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    iter_nums = iter(nums)
    i = 0
    new_arr =[]
    while True:
        try:
            a = next(iter_nums)
        except StopIteration:
            return new_arr
        if a % 2 == 0:
            new_arr.append(i)
        i += 1


def func_4(nums):
    new_arr = []
    new_arr += [ k for k, v in enumerate(nums) if not v % 2]
    return new_arr


if __name__ == '__main__':
    my_list1 = [0, 2, 4, 5, 7, 9, 6, 8, 11, 13]
    print(func_1(my_list1))
    print(func_2(my_list1))
    print(func_3(my_list1))
    print(func_4(my_list1))

print(timeit("func_1(my_list1)", globals=globals(), number=1000))
print(timeit("func_2(my_list1)", globals=globals(), number=1000))
print(timeit("func_3(my_list1)", globals=globals(), number=1000))
print(timeit("func_4(my_list1)", globals=globals(), number=1000))

# script list:
# [0, 1, 2, 6, 7]
# [0, 1, 2, 6, 7]
# [0, 1, 2, 6, 7]
# [0, 1, 2, 6, 7]
# 0.0006823000000000003
# 0.0007577
# 0.0010196000000000024
# 0.0006533000000000025
#
# Process finished with exit code 0