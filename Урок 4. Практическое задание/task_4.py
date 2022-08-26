"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from statistics import mode
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
    result = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]
    return result


def func_4():
    return max(set(array), key=array.count)


print(func_1())
print(func_2())
print(func_3())
print(func_4())
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# (1, 3) - число 1, 3 раза
# 1
print(timeit('func_1()', globals=globals(), number=1000))
print(timeit('func_2()', globals=globals(), number=1000))
print(timeit('func_3()', globals=globals(), number=1000))
print(timeit('func_4()', globals=globals(), number=1000))
"""
вариант func_4 получился самым быстрым из всех
0.0011127999750897288
0.001579799922183156
0.0013827000511810184
0.0008330999407917261
"""