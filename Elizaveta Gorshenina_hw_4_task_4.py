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


def func_3():
    elem, frequency = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {frequency} раз(а)'


print(func_1())
print('Время выполнения func_1 (100000000 раз): ', timeit('func_1', 'from __main__ import func_1', number=100000000))
print(func_2())
print('Время выполнения func_2 (100000000 раз): ', timeit('func_2', 'from __main__ import func_2', number=100000000))
print(func_3())
print('Время выполнения func_3 (100000000 раз): ', timeit('func_3', 'from __main__ import func_3', number=100000000))


# Время выполнения func_1 (100000000 раз):  2.3103126999922097
# Время выполнения func_2 (100000000 раз):  2.1630599000054644
# Время выполнения func_3 (100000000 раз):  2.1368032999889692

# Удалось немного ускорить задачу, но все три алгоритма работают
# достаточно быстро.
