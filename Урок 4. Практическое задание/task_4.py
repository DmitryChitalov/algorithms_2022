"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import collections
import operator
import random
import itertools
from timeit import timeit

array = [random.randint(1, 100) for _ in range(1000)]
print('start')


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return num, m


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return elem, max_2


def func_3():
    return max({i: array.count(i) for i in set(array)}.items(), key=operator.itemgetter(1))


def func_4():  # как func_1, но без count()
    d, max0 = {}, (0, 0)
    for i in array:
        d[i] = d.get(i, 0) + 1
        max0 = max0 if (d[i], i) < max0 else (d[i], i)
    return max0[1], max0[0]


def func_5():
    d = {i: len(list(j)) for i, j in itertools.groupby(sorted(array))}
    key = max(d, key=d.get)
    return key, d[key]


def func_6():
    d = {}
    for i in array:
        d[i] = d.get(i, 0) + 1
    key = max(d, key=d.get)
    return key, d[key]


def func_7():
    return collections.Counter(array).most_common(1)[0]


# запуск функций и вывод результатов
[print(f"func_{i}: (число, кол-во) {eval(f'func_1()')}") for i in range(1, 8)]
# профилировка каждого алгоритма через timeit
times = [timeit(f"func_{n}()", f"from __main__ import func_{n}", number=100) for n in range(1, 8)]
t_otn = [t / min(times) for t in times]
[print(f'func_{i + 1}:{t:8.3f}') for i, t in enumerate(t_otn)]
'''
результаты приведены в величинах относительно функции с минимальным временем выполнением
func_1: 212.237
func_2: 224.253
func_3:  21.381
func_4:   3.199
func_5:   2.311
func_6:   1.696
func_7:   1.000
1 место - func_7: алгоритм из библиотеки collections
2 место - func_6: 1 проход по array с формированием словаря в цикле {знач:к-во} и max()
3 место - func_5: неожиданно. Сортировка sorted(array), группировка itertools.groupby(), DC, max()
4 место - func_4: расчитывал, что он будет 1,2-м. Как и func_6, но максимальный вычисляется в цикле. Без max().
5 место - func_3: преобразование array в set(), DC c формированием словаря в цикле {знач:к-во}, count() и max()
6,7 место - удивили. Такое отсавание по времени > чем в 200 раз. count() для каждого элемента.
Вывод: Если есть возможность - использовать библиотеки словари.
'''
