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
    res = Counter(array).most_common(1)
    return f'Чаще всего встречается число {res[0][0]}, ' \
           f'оно появилось в массиве {res[0][1]} раз(а)'


print('Результат функции 1: ', func_1(), ', время: ', timeit('func_1()', number=1000, globals=globals()))
print('Результат функции 2: ', func_2(), ', время: ', timeit('func_2()', number=1000, globals=globals()))
print('Результат функции 3: ', func_3(), ', время: ', timeit('func_3()', number=1000, globals=globals()))


# Использован счетчик Counter из collections, но по замерам он проигрывает в скорости