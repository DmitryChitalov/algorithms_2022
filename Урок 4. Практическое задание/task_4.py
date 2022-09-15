"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]  # + [5] * 15 + [1] * 32 + [3] * 8
SETUP = 'from __main__ import func_1, func_2, func_3, array'
NUMBER = 100_000


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
    return max([(array.count(el), el) for el in set(array)])
    # n, num = max([(array.count(el), el) for el in set(array)])
    # return f'Чаще всего встречается число {num}, ' \
    #        f'оно появилось в массиве {n} раз(а)'


print(timeit('func_1()', SETUP, number=NUMBER))
print(timeit('func_2()', SETUP, number=NUMBER))
print(timeit('func_3()', SETUP, number=NUMBER))

print(func_1())
print(func_2())
# print(func_3())
n, num = func_3()
print(f'Чаще всего встречается число {num}, оно появилось в массиве {n} раз(а)')

"""
В примере все три функции имеют квадратичную сложность, но func_3 за счет преобразования списка во множество, 
элементов будет меньше, значит и работать будет быстрее с увеличением длины списка
"""
