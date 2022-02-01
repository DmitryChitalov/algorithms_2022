"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit


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
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    my_dict = {}
    for i in array:
        my_dict.setdefault(i, 0)
        my_dict[i] += 1
    max_val = max(list(my_dict.items()), key=lambda j: j[1])
    return f'Чаще всего встречается число {max_val[0]}, ' \
           f'оно появилось в массиве {max_val[1]} раз(а)'


def func_4(array):
    max_val1 = max(list(dict((x, array.count(x)) for x in set(array)).items()), key=lambda j: j[1])
    return f'Чаще всего встречается число {max_val1[0]}, оно появилось в массиве {max_val1[1]} раз(а)'


array = [1, 3, 1, 3, 4, 5, 1]
array2 = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]


print(func_1(array))
print(timeit("func_1(array)", setup="from __main__ import func_1, array", number=1000))
# 0.0018184000000000047
print(func_2(array))
print(timeit("func_2(array)", setup="from __main__ import func_2, array", number=1000))
# 0.0018588999999999967
print(func_3(array))
print(timeit("func_3(array)", setup="from __main__ import func_3, array", number=1000))
# 0.002740599999999996
print(func_4(array))
print(timeit("func_4(array)", setup="from __main__ import func_4, array", number=1000))
# 0.002879699999999999
# При небольшом входном массиве изначальные алгоритмы работают быстрее.


print(func_1(array2))
print(timeit("func_1(array2)", setup="from __main__ import func_1, array2", number=1000))
# 0.009771599999999998
print(func_2(array2))
print(timeit("func_2(array2)", setup="from __main__ import func_2, array2", number=1000))
# 0.012465899999999995
print(func_3(array2))
print(timeit("func_3(array2)", setup="from __main__ import func_3, array2", number=1000))
# 0.005186999999999997
print(func_4(array2))
print(timeit("func_4(array2)", setup="from __main__ import func_4, array2", number=1000))
# 0.004168900000000003
# На массиве побольше ситуация поменялась, исходные алгоритмы работают медленнее.
