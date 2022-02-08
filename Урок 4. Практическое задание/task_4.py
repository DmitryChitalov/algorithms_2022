"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import collections
from timeit import timeit


#array = [1, 3, 1, 3, 4, 5, 1]
array = [1, 3, 1, 3, 4, 5, 1, 7, 8, 5, 8, 5, 7, 5]


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
    """
    Используем функцию макс, в которой в качестве функции сортировки указана count
    То есть, первым будет число, которое больше всех встречается.
    """

    num = max(set(array), key=array.count)
    return f'Чаще всего встречается число {num}' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


print('Обычная реализация:')
print(
    timeit(
        "func_1()",
        globals=globals(),
        number=10000))
print('Реализация с max')
print(
    timeit(
        "func_2()",
        globals=globals(),
        number=10000))
print('Реализация с max и count')
print(
    timeit(
        "func_3()",
        globals=globals(),
        number=10000))
