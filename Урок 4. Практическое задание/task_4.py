"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

"""
Написал 2 функции с использованием сторонних библиотек и без, получилось медленнее.
Пробовал через преобразование в str, тоже дольше.
С использованием np - медленнее.
Вариант быстрее, чем первый, мне в голову не пришел.
"""

from collections import Counter
from timeit import timeit
import np

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
    _b = Counter(array)
    el_and_max = _b.most_common(1)
    el = el_and_max[0][0]
    max = el_and_max[0][1]

    return f'Чаще всего встречается число {el}, ' \
          f'оно появилось в массиве {max} раз(а)'


def func_4():
    return f'Чаще всего встречается число {max(array, key=array.count)}, ' \
          f'оно появилось в массиве {max(map(array.count, array))} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())


print(timeit("func_1()", "from __main__ import func_1", number=100000))
print(timeit("func_2()", "from __main__ import func_2", number=100000))
print(timeit("func_3()", "from __main__ import func_3", number=100000))
print(timeit("func_4()", "from __main__ import func_4", number=100000))

