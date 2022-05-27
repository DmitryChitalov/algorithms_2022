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

def func_3():
    # print(len(array))
    # print(array)
    # print(set(array))
    x = max(array, key=array.count)
    # print(x)
    # return len(set(array))
    return f'Чаще всего встречается число {x}, ' \
           f'оно появилось в массиве {array.count(x)} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))

print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))

print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=10000))

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.015254299999999991
0.02257129999999999
0.016508400000000006

Ускорить не получилось, первый вариант самый быстрый
"""
