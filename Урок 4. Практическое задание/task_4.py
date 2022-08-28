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
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def my_func():
    return f'Чаще всего встречается число ' \
           f'{max({i: array.count(i) for i in array}.items(), key=lambda x: x[1])[0]}'


def my_func2():
    return f'Чаще всего встречается число ' \
            f'{Counter(array).most_common(1)[0][0]}'


print(func_1())
print(func_2())
print(my_func())
print(my_func2())

print(timeit('func_1()', globals=globals(), number=100000))
print(timeit('func_2()', globals=globals(), number=100000))
print(timeit('my_func()', globals=globals(), number=100000))
print(timeit('my_func2()', globals=globals(), number=100000))

"""
Вывод: ускорить задачу не получилось.
"""
