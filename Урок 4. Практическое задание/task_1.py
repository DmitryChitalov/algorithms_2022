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

MY_LIST = list(range(100))


def func_1(nums):  # O(N)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # O(N)
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


if __name__ == '__main__':
    print("Заполнение списка с помощью традиционного ирерратора с функцией .append().")
    print(timeit("func_1(list(range(10)))", setup="from __main__ import func_1"))
    print(timeit("func_1(MY_LIST)", globals=globals()))
    print(timeit("func_1(list(range(1000)))", setup="from __main__ import func_1"))
    print("Заполнение списка с помощью list comprehension.")
    print(timeit("func_2(list(range(10)))", setup="from __main__ import func_2"))
    print(timeit("func_2(MY_LIST)", globals=globals()))
    print(timeit("func_2(list(range(1000)))", setup="from __main__ import func_2"))

    # У традиционного ирерратора с функцией .append() и list comprehension скорость
    # выполнения сравнимая (почти одинаковая). Во второй функции оптимизирована запись.
    # У компрехеншена (возможно) чуть быстрее, так как это связано с компилированием кода.
    # У компрехеншена есть встроенная функция .append(), она работает быстрее.
