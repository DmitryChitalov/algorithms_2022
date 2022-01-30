"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from collections import Counter
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


def func_3():
    _max = max([(array.count(elem), elem) for elem in set(array)])
    # _max = {elem: array.count(elem) for elem in array}
    # _max = Counter(array).most_common(1)
    return f'Чаще всего встречается число {_max[1]}, ' \
           f'оно появилось в массиве {_max[0]} раз(а)'


print(timeit("func_1()", number=100000, globals=globals()))
print(timeit("func_2()", number=100000, globals=globals()))
print(timeit("func_3()", number=100000, globals=globals()))

"""
ускорить задачу можно при большом количестве одинаковых элементов
"""