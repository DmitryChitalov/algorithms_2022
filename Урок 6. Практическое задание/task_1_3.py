"""
Задание 1.

Это файл для третьего скрипта
"""
"""
Урок 4
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from pympler import asizeof
from numpy import array


some_array = [1, 3, 1, 3, 4, 5, 16, 21, 2, 1, 1, 43, 12]
print(asizeof.asizeof(some_array))      # 448
some_array = array([1, 3, 1, 3, 4, 5, 16, 21, 2, 1, 1, 43, 12])
print(asizeof.asizeof(some_array))      # 232


def func_1():
    m = 0
    num = 0
    for i in some_array:
        count = some_array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in some_array:
        count2 = array.some_array(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = some_array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_elem = max(some_array, key=some_array.count)
    return f'Чаще всего встречается число {max_elem}, '\
           f'оно появилось в массиве {some_array.count(max_elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print('-' * 50)
print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("func_3()", globals=globals()))

'''
При использовании numpy память занимаемая массивом значительно меньше - 232 против 448 
'''