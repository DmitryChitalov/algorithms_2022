"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
    

# Избавилась от пробега по индексу внутри range(), теперь мы работаем с элементами напрямую, что сократило время выполнения кода    
def func_2(nums):
    new_arr = []
    new_list = range(len(nums))
    for elem in new_list:
        if elem % 2 == 0:
            new_arr.append(elem)
    return new_arr

NUMS = [el for el in range(1000)]
print(timeit("func_1(NUMS[:])", globals=globals(), number=1000))

NUMS1 = [el for el in range(1000)]
print(timeit("func_2(NUMS1[:])", globals=globals(), number=1000))

