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
    array_set = set(array)
    max_quant = 0
    most_common = None
    for i in array_set:
        if array.count(i) > max_quant:
            max_quant = array.count(i)
            most_common = i
    return f'Чаще всего встречается число {most_common}, ' \
           f'оно появилось в массиве {max_quant} раз(а)'


print(func_1())
print(func_2())
print(func_3())


print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))

"""
Замеры времени:
4.4241261000000005
5.6148195
3.7522009
Совсем немного уменьшается время выполнения задачи, если перевести массив во множество, так как во множестве только
уникальные значения, то есть мы не считаем по несколько раз максимальное значение одного и того же числа
"""
