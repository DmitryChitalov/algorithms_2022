"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from collections import Counter


array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return  f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    dict = {}
    count, itm = 0, ''
    for i in array:
        dict[i] = dict.get(i, 0) + 1
        if dict[i] >= count:
            count, itm = dict[i], i
    return f'Чаще всего встречается число {itm}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_4():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'



print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f'функция {func_1.__name__} отработала за', timeit('func_1()', globals=globals() , number=10000), 'сек.')
print(f'функция {func_2.__name__} отработала за', timeit('func_2()', globals=globals(), number=10000), 'сек.')
print(f'функция {func_3.__name__} отработала за', timeit('func_3()', globals=globals(), number=10000),  'сек.')
print(f'функция {func_4.__name__} отработала за', timeit('func_4()', globals=globals(), number=10000),  'сек.')

"""функция func_1 отработала за 0.06446959999999999 сек.
функция func_2 отработала за 0.08903319999999998 сек.
функция func_3 отработала за 0.07620300000000002 сек.
функция func_4 отработала за 0.07852560000000003 сек.

Вывод, при запуске в 10000 раз, самой быстрой оказалась func_1, одинаково
показали себя функция func_4 с встроенной функцией max и добавлением в словарь func_3"""

