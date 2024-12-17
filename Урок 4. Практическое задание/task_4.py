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
    return ("Чаще всего встречается число {0}, "
            "оно появилось в массиве {1} раз(а)").format(*max(Counter(array).items(), key=lambda x: (x[1], x[0])))


def func_4():
    max_count = max(array, key=array.count)
    return f"Чаще всего встречается число {max_count}, " \
           f"оно появилось в массиве {array.count(max_count)} раз(а)"


def time_func(func):
    time_taken = timeit(func, number=10000)
    return f"Time taken by {func.__name__}: {time_taken} seconds"


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(time_func(func_1))
print(time_func(func_2))
print(time_func(func_3))
print(time_func(func_4))
