"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import Timer, timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(nums.index(i))
    return new_arr


def func_4(nums):
    new_arr = [nums.index(i) for i in nums if i % 2 == 0]
    return new_arr


mas = [i for i in range(1000)]
a = func_1(mas)
b = func_2(mas)
c = func_3(mas)
d = func_4(mas)

if (a == b) and (a == c) and (a == d): print('OK')
t1 = Timer(stmt="func_1(mas)", globals=globals())

print("func_1", t1.timeit(number=2000), "seconds")
t2 = Timer(stmt="func_2(mas)", globals=globals())
print("func_2", t1.timeit(number=2000), "seconds")
t3 = Timer(stmt="func_3(mas)", globals=globals())
print("func_3", t1.timeit(number=2000), "seconds")
t4 = Timer(stmt="func_4(mas)", globals=globals())
print("func_4", t1.timeit(number=2000), "seconds")

print('----------Only timeit------------')

print("func_1", timeit("func_1(mas)", number=2000, globals=globals()), "seconds")
print("func_2", timeit("func_2(mas)", number=2000, globals=globals()), "seconds")
print("func_3", timeit("func_3(mas)", number=2000, globals=globals()), "seconds")
print("func_4", timeit("func_4(mas)", number=2000, globals=globals()), "seconds")

# честно говоря разница особо не заметна, результаты пляшут при разных проходах.
#
# проход 1 - здесь мы видим,
# что самое быстрое - comprehention с использованием функции range  и вычислением длинны списка
# func_1 26.46454138 seconds
# func_2 26.291605072000003 seconds
# func_3 25.915140109 seconds
# func_4 26.545174911000004 seconds

# проход 2 здесь мы видим, что самое быстрое - comprehention с использованием метода .index
# func_1 27.667482725000003 seconds
# func_2 27.652101732 seconds
# func_3 27.451681834000006 seconds
# func_4 27.026021016 seconds

# Проход 3 Здесь вообще самый быстрый - первоначальный вариант
# func_1 26.816063585000002 seconds
# func_2 27.306893406999997 seconds
# func_3 27.235876381000004 seconds
# func_4 26.974640136999994 seconds

# Проход 4 - самое быстрое comprehention с использованием функции range  и вычислением длинны списка
# func_1 27.631519046 seconds
# func_2 26.630037083999998 seconds
# func_3 27.308635097 seconds
# func_4 26.844591506 seconds

# Проход 5 , здесь comprehention с использованием функции range - наоборот самое медленное
# func_1 27.980311965 seconds
# func_2 30.370606108000004 seconds
# func_3 27.330380147 seconds
# func_4 28.133311057 seconds

# Проход 6 , самый быстрый - перебор массива с использованием метода .index
# func_1 27.347917369 seconds
# func_2 26.981167558 seconds
# func_3 26.497584183999997 seconds
# func_4 26.58576010200001 seconds
#
# все проходы были сделаны подряд, без подбора по результатам

# Однако при замерах с использованием ТОЛЬКО функции timeit - последние два варианта стали работать ощутимо медленне. В чем причина - загадка.
# Значит это все таки не равнозначные методы измерения времени?
# Вот  пример, количество повторений уменьшено в 100 раз
#
# func_1 0.278636332 seconds
# func_2 0.29593977000000005 seconds
# func_3 0.288870085 seconds
# func_4 0.27463777 seconds
# ----------Only timeit------------
# func_1 0.259166115 seconds
# func_2 0.2328024059999998 seconds
# func_3 7.215676302 seconds
# func_4 7.154397805 seconds

