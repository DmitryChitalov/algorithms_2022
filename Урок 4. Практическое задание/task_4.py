"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

import timeit
import time

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
    dictionary = dict()
    for i in array:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    res = (max(dictionary, key=dictionary.get))
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {dictionary[res]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit.timeit(stmt='func_1()', setup='from __main__ import func_1', number=1000))
time.sleep(1)
print(timeit.timeit(stmt='func_2()', setup='from __main__ import func_2', number=1000))
time.sleep(1)
print(timeit.timeit(stmt='func_3()', setup='from __main__ import func_3', number=1000))

'''
Результаты замера:
0.003993100021034479
0.009997099870815873
0.0064656001050025225
Написанная мной функция показала средний результат.
'''