"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


from timeit import timeit, default_timer


def my_timer(func):
    def wrap(nums):
        start = default_timer()
        func(nums)
        print(default_timer() - start)
    return wrap


@my_timer
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@my_timer
def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


n = [i for i in range(1000)]

func_1(n)
print(timeit("func_1(n)", globals=globals(), number=1))
print()
func_2(n)
print(timeit("func_2(n)", globals=globals(), number=1))

"""
Листинг вывода
0.0001686609994067112 - замер времени декоратором
0.00016259800031548366 - замер времени декоратором обусловленный вызовом timeit
0.00018755200017039897 - замер времени timeit

9.29810003071907e-05 - замер времени декоратором
9.314099952462129e-05 - замер времени декоратором обусловленный вызовом timeit
0.00010140599988517351 - замер времени timeit

Выводы из полученых замеров:
    - самописный декоратор-таймер и timeit дают сопоставимые результаты;
    - lc дало увеличение скорости работы (на n) почти в 2 раза;
"""