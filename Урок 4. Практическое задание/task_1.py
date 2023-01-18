"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit, default_timer, Timer


n = list(range(1000))


"""вариант добавление из списка в список по условию методом append"""
def list_append(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""вариант добавление из списка в список c функцией list_comprehension"""
def list_comprehension(nums):
    new_arr = [i for i in range(len(nums)) if not nums[i] % 2]
    return new_arr



"""фнункция list_append отработала за 2.2608875 сек.
   фнункция list_comprehension отработала за 1.2962740999999998 сек.
   
   В данном примере, при добавлении в список с условием if nums[i] % 2 == 0
   считаю самым оптимальным вариантом функцию list_comprehension.
   Она отработала на 0.97 сек. быстрее, почти на секунду."""



t1 = timeit('list_append(n)', globals=globals(), number=5000)
t2 = timeit('list_comprehension(n)', globals=globals(), number=5000)
#t3 = timeit('func_3(n)', globals=globals(), number=10000)
print(f'фнункция {list_append.__name__} отработала за {t1} сек.')
print(f'фнункция {list_comprehension.__name__} отработала за {t2} сек.')
