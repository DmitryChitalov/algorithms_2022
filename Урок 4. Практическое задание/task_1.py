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
    res = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return res

temp = [5, 6, 8, 9, 7, 6, 7, 3, 4, 6, 7]

print('append:', timeit('func_1(temp)', globals=globals(), number=1000000))
print('list comprehension:', timeit('func_2(temp)', globals=globals(), number=1000000))

"""Исходная функция, использующая традиционный итератор с функцией append, была заменена на list comprehension.
Эффект не однозначный. Замерив более 10 раз, меняя 'number' функции 'timeit', результаты разнятся, не в пользу 
list comprehension.
Вывод: удалось оптимизировать код, сделать его более понятным, но результат лучше не стал.

p.s. Проверял на своем ПК, Replit. Везде традиционный подход в большинстве случаев выдавал лучшее время.
В редких случаях время было +- одинаковым.

Результаты:
append: 4.330981310005882
list comprehension: 4.613021917000879

append: 0.8067740000551566
list comprehension: 0.850951400003396

append: 0.8130116999382153
list comprehension: 0.8414239999838173

append: 0.8091740000527352
list comprehension: 0.8435304999584332
"""