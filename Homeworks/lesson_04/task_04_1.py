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

lst = []
for _ in range(50000):
    lst.append(_)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':
    print(timeit("func_1(lst)", globals=globals(), number=1000))
    print(timeit("func_2(lst)", globals=globals(), number=1000))


# В функции func_2 реализовано добавление в массив индексов чётных элементов входящего массива
# с помощью List Comprehension, что позволило уменьшить время выполнения данной операции
# по сравнению с функцией func_1, в которой добавление в массив реализовано с помощью
# традиционного итератора с методом append.
