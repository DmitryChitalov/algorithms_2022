"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
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
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    answer = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {answer[0]}, ' \
           f'оно появилось в массиве {answer[1]} раз(а)'


print(func_1(), timeit(
    'func_1()', 'from __main__ import func_1', number=10000
))
print(func_2(), timeit(
    'func_2()', 'from __main__ import func_2', number=10000
))
print(func_3(), timeit(
    'func_3()', 'from __main__ import func_3', number=10000
))
'''
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) 0.031028
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) 0.037758500000000014
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) 0.0846664
Ускорить задачу не получилось, но код получился более компактным.
'''