"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from collections import Counter
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
    elem, nums = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {nums} раз(а)'


def func_4():
    el = sorted(array, key=lambda x: array.count(x))[-1]
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {array.count(el)} раз(а)'


def func_5():
    nums, el = max({array.count(key): key for key in set(array)}.items())
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {nums} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(f'Время работы функции {func_1.__name__} - {timeit("func_1()", globals=globals())}')
print(f'Время работы функции {func_2.__name__} - {timeit("func_2()", globals=globals())}')
print(f'Время работы функции {func_3.__name__} - {timeit("func_3()", globals=globals())}')
print(f'Время работы функции {func_4.__name__} - {timeit("func_4()", globals=globals())}')
print(f'Время работы функции {func_5.__name__} - {timeit("func_5()", globals=globals())}')


"""
Время работы функции func_1 - 3.3639583999993192
Время работы функции func_2 - 4.346648899998399
Время работы функции func_3 - 7.4237278000000515
Время работы функции func_4 - 5.131565100000444
Время работы функции func_5 - 3.851553199998307

Сделал замеры, ускорить задачу не получилось
"""
