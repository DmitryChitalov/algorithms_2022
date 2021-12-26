"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
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
    return f'Чаще всего встречается число {num}, оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)'


def my_func_counter():
    result = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {result[0]}, ' \
           f'оно появилось в массиве {result[1]} раз(а)'


# def my_func():
#     return f'Чаще всего встречается число {}, ' \
#            f'оно появилось в массиве {} раз(а)'

"""
В своей функции использую класс Counter из встроенного модуля collections. 
Но данный метод замедляет скорость выполнения почти в 2 раза
"""
print(func_1())
print(func_2())
print(my_func_counter())
print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("my_func_counter()", globals=globals()))
