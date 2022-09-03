"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit

array_ = [1, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1, 4]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    try:
        new_array = []
        for el in array:
            count2 = array.count(el)
            new_array.append(count2)

        max_2 = max(new_array)
        elem = array[new_array.index(max_2)]
        return f'Чаще всего встречается число {elem}, ' \
               f'оно появилось в массиве {max_2} раз(а)'
    except ValueError:
        return 'Передан пустой список'


def func_3(array):
    try:
        maximum = max(array, key=array.count)
        return f'Чаще всего встречается число {maximum}, ' \
               f'оно появилось в массиве {array.count(maximum)} раз(а)'
    except ValueError:
        return 'Передан пустой список'


print(timeit("func_1(array_)", globals=globals(), number=10000))
print(timeit('func_2(array_)', globals=globals(), number=10000))
print(timeit('func_3(array_)', globals=globals(), number=10000))

'''

0.02892789989709854
0.05609810003079474
0.024536399985663593

Встроенные функции работают быстрее, чем написанные вручную алгоритмы.

'''