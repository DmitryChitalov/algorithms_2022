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

array = [1, 3, 1, 3, 4, 5, 1, 3, 3, 5, 5, 5, 5, 5]


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


print(func_1())
print(timeit('func_1', globals=globals(), number=10000000))
print(func_2())
print(timeit('func_2', globals=globals(), number=10000000))


def func_3():
    num = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {num[0]} ' \
           f'оно встречается в массиве {num[1]} раз(а)'


print(func_3())
print(timeit('func_3', globals=globals(), number=10000000))

# Первый алгоритм отработал за 0.2985780000453815
# Второй отработал за 0.26736559998244047
# Мой алгоритм с использованием коллекций отработал за 0.2457509000087157
# Что быстрее и код лаконичнее
