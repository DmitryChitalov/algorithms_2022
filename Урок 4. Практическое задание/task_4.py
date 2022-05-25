"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
###############################################################################
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
    res = max(zip((array.count(item) for item in set(array)), set(array)))
    return f'Чаще всего встречается число {res[1]}, ' \
           f'оно появилось в массиве {res[0]} раз(а)'


def func_4():
    res = max(item for item in array if array.count(item) == max(map(array.count, array)))
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {max(map(array.count, array))} раз(а)'


def func_5():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


print(func_1.__name__, timeit("func_1()", globals=globals(), number=1000))
print(func_2.__name__, timeit("func_2()", globals=globals(), number=1000))
print(func_3.__name__, timeit("func_3()", globals=globals(), number=1000))
print(func_4.__name__, timeit("func_3()", globals=globals(), number=1000))
print(func_5.__name__, timeit("func_3()", globals=globals(), number=1000))

print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())
"""
Аналитика:
Написал код в одну строку для нахождения числа,
которое встречается в массиве чаще всего.
"""
