"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

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

    my_list = {}
    for i in array:
        my_list[i] = array.count(i)
    my_list = sorted(my_list.items(), key=lambda x: x[0])
    return f'Чаще всего встречается число {my_list[0][0]}, ' \
           f'оно появилось в массиве {my_list[0][1]} раз(а)'

def func_4():
    a = max({array.count(x): x for x in array}.items())
    return f'{a[0]} - {a[1]}'

#не ускорил
print(func_1())
print(func_2())
print(func_4())
print(timeit.timeit('func_1()', number=100000, globals=globals()))
print(timeit.timeit('func_2()', number=100000, globals=globals()))
print(timeit.timeit('func_4()', number=100000, globals=globals()))
