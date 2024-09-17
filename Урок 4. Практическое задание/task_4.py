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
from collections import OrderedDict
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
    count = Counter(array)
    res = count.most_common(1)
    res = res[0]
    num, quantity = res
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {quantity} раз(а)'


def func_4():
    di = OrderedDict()
    for i in array:
        if di.get(i):
            di[i] += 1
        else:
            di[i] = 1
    max = 0
    di = {v:k for k,v in di.items()}
    for k, v in di.items():
        if max< k:
            max=k

    return f'Чаще всего встречается число {di[max]}, ' \
           f'оно появилось в массиве {max} раз(а)'


print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))
print(timeit('func_4()', globals=globals()))
print(func_1())
print(func_2())
print(func_3())
print(func_4())


'''
быстрее всего срабатывает func_1() т.к. в ней всего 1 цикл
func_2() кроме цикла нагружена append что замедляет ее быстродействие
func_3() самая долгая т.к. происходит создание новой коллекции и встроеной
     функции нахождения часто встречающегося
func_4() самая долгая т.к. в ней есть и dict_comprehension и 2 цикла
'''