"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    @ @-19

    , 3 + 20, 50 @ @

    def func_1(nums):

        if nums[i] % 2 == 0:
            new_arr.append(i)


return new_arr

'''
Реализация  без метода index(), т.к. индекс текущего элемента совпадает с счетчиком цикла i, поэтому в новый список 
добавляем i

'''


def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


'''
Реализация  c помощью генератора позволяет не перебирать заново исхожный список при каждой итерации и отсутствует
вспомогательный список.
Генератор реализован в функции для выполнения условия задания - вывод списка с индексами,  что замедляет функцию из за 
метода list()
'''


def func_3(nums):
    def func_3_gen(nums):
        for i in range(len(nums)):
            if i % 2 == 0:
                yield i

    return list(func_3_gen(nums))


numbers = []
for i in range(10000):
    numbers.append(i)

t1 = timeit('func_1(numbers)', globals=globals(), number=1000)
t2 = timeit('func_2(numbers)', globals=globals(), number=1000)
t3 = timeit('func_3(numbers)', globals=globals(), number=1000)
print(f'Время выполнения функции func_1  {t1}')
print(f'Время выполнения функции func_2  {t2}')
print(f'Время выполнения функции func_3  {t3}')
print(f'После оптимизации функции func_1 в func_2 время выполенния уменьшилось на {t1 - t2}')
print(f'После оптимизации функции func_1 в func_3 время выполенния уменьшилось на {t1 - t3}')