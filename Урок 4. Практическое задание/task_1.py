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

numbers = []
for j in range(1000):
    numbers.append(j)


def func_1(nums):  # извлечение индексов с помощью range
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # извлечение четных индексов с помощью шага в range
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr


def func_3(nums):  # извлечение индексов с помощью enumerate
    new_arr = []
    for i, v in enumerate(nums):
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_4(nums):  # извлечение индексов с помощью предусловия в while
    new_arr = []
    i = 0
    while i < len(nums):
        if i % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr


def func_5(nums):  # извлечение четных индексов и создание списка с ними с помощью LC
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


print(f"range: {timeit('func_1(numbers)', globals=globals(), number=10000)}")

print(f"range with step: {timeit('func_2(numbers)', globals=globals(), number=10000)}")

print(f"enumerate: {timeit('func_3(numbers)', globals=globals(), number=10000)}")

print(f"while: {timeit('func_4(numbers)', globals=globals(), number=10000)}")

print(f"LC: {timeit('func_5(numbers)', globals=globals(), number=10000)}")

print('\nВывод: я добавил 3 функции которые производят извлечение четных индексов из списка (и добавляют их в другой)\n\
и выяснил, что использование шага в range является лучшим способом извлечь четные индексы,\n\
худшим же является функция с while, также неплохой результат у LC,\n\
range без шага и enumerate показывают примерно одинаковый результат с небольшим преимуществом у range')
