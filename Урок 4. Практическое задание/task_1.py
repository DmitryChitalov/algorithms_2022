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

SETUP = 'lst = range(1000)'
NUMBER = 10_000


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if not nums[i] % 2]


def func_3(nums):
    return [i for i, v in enumerate(nums) if not v % 2]


def func_4(nums):
    return (i for i, v in enumerate(nums) if not v % 2)
    # return list((i for i, v in enumerate(nums) if not v % 2))


def func_5(nums):
    return map(lambda item: item[0], filter(lambda x: not x[1] % 2, enumerate(nums)))


print(timeit('func_1(lst)', setup=SETUP, globals=globals(), number=NUMBER))
print(timeit('func_2(lst)', setup=SETUP, globals=globals(), number=NUMBER))
print(timeit('func_3(lst)', setup=SETUP, globals=globals(), number=NUMBER))
print(timeit('func_4(lst)', setup=SETUP, globals=globals(), number=NUMBER))
print(timeit('func_5(lst)', setup=SETUP, globals=globals(), number=NUMBER))

print(func_1(range(1000)))
print(func_2(range(1000)))
print(func_3(range(1000)))
print(list(func_4(range(1000))))
print(list(func_5(range(1000))))

"""
В функциях func_2, func_3 применен list_comprehension.
Преимущества lc:  1) Использует меньше памяти и выполняется быстрее, чем обычные циклы
                  2) Пишется как правило в одну строку
Итог: func_2 работает быстрее чем func_1

В функции func_2 на очередной итерации получаем элемент по индексу из списка, что дополнительно занимает какое-то время.
В функции func_3 работаем напрямую со значением.
Итог: func_3 работает быстрее чем func_2

func_4, func_5 - функции генераторы (возвращают объекты-итераторы).
func_4 Отрабатывает быстро. Но преобразование итератора в список занимает какое-то время (сложность O(n)). 
func_5 тоже что и func-4. Работает еще быстрей за счет встроенных функций map() и filter(). 
Если не нужен сразу весь набор данных, то работаем с функциями-генераторами. 
"""
