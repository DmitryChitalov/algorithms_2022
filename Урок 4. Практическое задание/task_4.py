"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

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
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# [1, 3, 1, 3, 4, 5, 1] # list
# [3, 2, 3, 2, 1, 1, 3] # count
#

def func_3():
    res = max(array, key=lambda x: array.count(x))
    return f"Чаще всего встречается число {res}, оно появилось в массиве {array.count(res)} раз(а)"


print(func_1())
print(func_2())
print(func_3())
print(f""" func_1
    {timeit(
    'func_1()',
    setup='from __main__ import func_1',
    number=100000)}""")

print(f""" func_2
    {timeit(
    'func_2()',
    setup='from __main__ import func_2',
    number=100000)}""")

print(f""" func_3
    {timeit(
    'func_3()',
    setup='from __main__ import func_3',
    number=100000)}""")

"""
    0.1561984999862034
 func_2
    0.25320179999107495
 func_3
    0.23327990001416765

решение одной строкой не получилось получилось 2 и насчет скорости 2-3 функции примерно одинаково работают 

"""
