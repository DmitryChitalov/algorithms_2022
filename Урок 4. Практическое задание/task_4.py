"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import random
from timeit import timeit
from collections import defaultdict

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
    m = 0
    num = 0
    result = defaultdict(int)
    for i in array:
        result[i] += 1
        if result[i] > m:
            m = result[i]
            num = i

    return f'Чаще всего встречается число {num}, ' \
               f'оно появилось в массиве {m} раз(а)'


if __name__ == '__main__':
    print("На небольшом списке")
    print("func_1:", timeit("func_1()", globals=globals(), number=10000))
    print("func_2:", timeit("func_2()", globals=globals(), number=10000))
    print("func_3:", timeit("func_3()", globals=globals(), number=10000))
    print("На большом списке")
    array = [random.randint(1,10) for i in range(100)]
    print("func_1:", timeit("func_1()", globals=globals(), number=10000))
    print("func_2:", timeit("func_2()", globals=globals(), number=10000))
    print("func_3:", timeit("func_3()", globals=globals(), number=10000))

"""
На небольшом списке
func_1: 0.011661083999999999
func_2: 0.0140115
func_3: 0.011966124999999994
На большом списке
func_1: 0.786646583
func_2: 0.8068924169999999
func_3: 0.07637120800000008

На небольшом массиве разница в алгоритмах не заметна, но при увеличении размера входного массива, третий алгоритм
имеет приемущество, т.к. имеет линейную алгоритмическую сложность O(n).
"""
