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
    counters = {}
    for i in array:
        if i in counters:
            counters[i] += 1
        else:
            counters[i] = 1

    max_item = max(counters, key=counters.get)

    return f'Чаще всего встречается число {max_item}, ' \
           f'оно появилось в массиве {counters[max_item]} раз(а)'


def func_4():
    max_ = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {max_[0]}, ' \
           f'оно появилось в массиве {max_[1]} раз(а)'


def func_5():
    max_ = max(array, key=array.count)
    return f'Чаще всего встречается число {max_}, ' \
           f'оно появилось в массиве {array[max_]} раз(а)'


if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(func_3())
    print(func_4())
    print(func_5())
    print(timeit('func_1()', 'from __main__ import func_1', number=10000))
    print(timeit('func_2()', 'from __main__ import func_2', number=10000))
    print(timeit('func_3()', 'from __main__ import func_3', number=10000))
    print(timeit('func_4()', 'from __main__ import func_4', number=10000))
    print(timeit('func_5()', 'from __main__ import func_5', number=10000))

    """
    0.018256703
    0.023835256
    0.018811392999999996
    0.042498045999999984
    0.017347190999999984
    Вариант с max(key=array.count) оказался самым быстрым.
    """
