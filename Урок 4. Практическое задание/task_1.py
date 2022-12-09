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
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]
    return new_arr


nums = range(1, 1000)

print(timeit("func_1(nums)", globals=globals(), number=1000))
print(timeit("func_2(nums)", globals=globals(), number=1000))

# Переделала функцию с использованием list comprehension
# Сделала 2 замера - один на 1000 запусков первой функции, один на 1000 запусков второй функции
# У меня получилось, что вторая функция в два раза быстрее отрабатывает

