"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import Timer
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
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


def func_4():
    return f'Чаще всего встречается число {Counter(array).most_common(1)[0][0]}, ' \
           f'оно появилось в массиве {Counter(array).most_common(1)[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

t1 = Timer(stmt='func_1', setup='from __main__ import func_1')
print("функция func_1  ", t1.timeit(number=10000000), 'seconds')

t2 = Timer(stmt='func_2', setup='from __main__ import func_2')
print("функция func_2  ", t1.timeit(number=10000000), 'seconds')

t3 = Timer(stmt='func_3', setup='from __main__ import func_3')
print("функция func_3  ", t1.timeit(number=10000000), 'seconds')

t4 = Timer(stmt='func_4', setup='from __main__ import func_4')
print("функция func_4  ", t1.timeit(number=10000000), 'seconds')

# функция func_1   0.23617290006950498 seconds
# функция func_2   0.21995980013161898 seconds
# функция func_3   0.216214100131765 seconds
# функция func_4   0.223549900110811 seconds

# в третьем варианте (func_3) замеры показали маленькое улучшение производительности
