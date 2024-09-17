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


li = [i for i in range(100)]

quantity_calls = 100000
for_append = timeit('func_1(li)', number=quantity_calls, globals=globals())
list_compr = timeit('[i for i in li if i%2==0]', globals=globals(), number=quantity_calls)

print(f'''Используя for-append и списковая сборка для {quantity_calls} вызовов
for-append выполняется за {for_append} секунд
list_comprehension выполняется за {list_compr} секунд
заметно ускорение списковой сборки в {round(for_append/list_compr, 1)} раза по сравнению с for-append''')


'''
Используя for-append и списковая сборка для 10000 вызовов
for-append выполняется за 0.08187698200003979 секунд
list_comprehension выполняется за 0.05170710000015788 секунд
заметно ускорение списковой сборки в 1.6 раза по сравнению с for-append

Используя for-append и списковая сборка для 10000 вызовов
for-append выполняется за 0.0831515219999801 секунд
list_comprehension выполняется за 0.054725379000046814 секунд
заметно ускорение списковой сборки в 1.5 раза по сравнению с for-append
'''