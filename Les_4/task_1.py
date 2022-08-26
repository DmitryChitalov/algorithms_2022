"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit, repeat
from random import randint

"""
1. Тест функций на списке из 1000 элементов. Простые замеры на 1000 раз и с repeat 5 раз
2. Тест функций на списке из 100000 элементов. Простые замеры на 1000 раз и с repeat 5 раз
3. ускорение за счёт использования list comprehension func_fast

Что выдал мне код (первое число от func_1, второе от func_fast):
замеры на списки из 100 элементов
0.006408833000023151
0.0056074449994412134
замеры на списки из 100000 элементов
7.271690378999665
6.363429039000039
замеры на списки из 100 элементов с repeat 5 раз, минимальное время
0.006144156000118528
0.0053588330001730355
замеры на списки из 100000 элементов с repeat 5 раз, минимальное время
7.125867296999786
6.209995103000438

На всех замерах list comprehension сработал быстрее, чем .append() в цикле
сложность в обоих случаях О(n), но на деле в func_1 есть append, что всё-таки имеет влияние на время

"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# создадим список из 100 и 100000 случайных чисел для замеров
lst = []
for i in range(100):
    lst.append(randint(0, 5000))
lst_1 = []
for i in range(100000):
    lst_1.append(randint(0, 5000))


# подозреваю, что можно ускорить процесс создания списка с помощью list comprehension
def func_fast(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# проведём замеры на выполнение 1000 раз обеих функций на списках разной длины
print('замеры на списки из 100 элементов')
print(timeit('func_1(lst)', globals=globals(), number=1000))
print(timeit('func_fast(lst)', globals=globals(), number=1000))
print('замеры на списки из 100000 элементов')
print(timeit('func_1(lst_1)', globals=globals(), number=1000))
print(timeit('func_fast(lst_1)', globals=globals(), number=1000))
# попробуем посмотреть с repeat, оценим минимальное время
statements = ['''
new_arr = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        new_arr.append(i)''', '[i for i in range(len(nums)) if nums[i] % 2 == 0]']

print('замеры на списки из 100 элементов с repeat 5 раз, минимальное время')

for st in statements:
    print(min(repeat(st, setup=f"nums={lst}", repeat=5, number=1000)))

print('замеры на списки из 100000 элементов с repeat 5 раз, минимальное время')

for st in statements:
    print(min(repeat(st, setup=f"nums={lst_1}", repeat=5, number=1000)))
