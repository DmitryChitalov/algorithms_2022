"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
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
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'



def func_4():
    dict_1 = {}
    count = itm = 0
    for item in reversed(array):
        dict_1[item] = dict_1.get(item, 0) + 1
        if dict_1[item] >= count:
            count, itm = dict_1[item], item
    return f'Чаще всего встречается число {itm}, ' \
           f'оно появилось в массиве {count} раз(а)'



print(func_1())
print(func_2())
print(func_3())
print(func_4())


print(timeit("func_1()", globals=globals(), number=1000))
print(timeit("func_2()", globals=globals(), number=1000))
print(timeit("func_3()", globals=globals(), number=1000))
print(timeit("func_4()", globals=globals(), number=1000))

# время выполнения func_1  - 0.0761689
# время выполнения func_2 - 0.07905859999999999
# время выполнения func_3 - 0.07725869999999999
# время выполнения func_4 - 0.009335799999999977
# наиболее эффективный алгоритм func_4, с использованием словаря

