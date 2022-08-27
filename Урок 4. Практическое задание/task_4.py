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
    max_num = max(array, key=array.count)
    # print(max_num)
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {array.count(max_num)} раз(а)'


# print(func_1())
# print(func_2())
# print(func_3())

# 18.80056587099898  # func_1
# 25.219938842001284  # func_2
# 21.753042074000405  # func_3

"""
При увеличении размера списка, то мы увидим, что встроенная функция, явно работает быстрее, других.
"""
