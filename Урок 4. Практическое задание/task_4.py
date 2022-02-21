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
    val = max(array,key=array.count)
    return f'Чаще всего встречается число {val}, ' \
           f'оно появилось в массиве {array.count(val)} раз(а)'


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

'''Самые быстрые это встроенные функции, они быстрее  циклов
1.2470711779997146 цикл
1.4442878269996982 цикл
1.0807000609997885 встроенная функция

'''