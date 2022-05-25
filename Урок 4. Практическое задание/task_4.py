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
    elemList = []
    for elem in array:
        elemList.append(array.count(elem))
        return f'Чаще всего встречается число {elem}, ' \
               f'оно появилось в массиве {max(elemList)} раз(а)'


print(timeit("func_1()", setup="from __main__ import func_1", number=1000))
print(timeit("func_2()", setup="from __main__ import func_2", number=1000))
print(timeit("func_3()", setup="from __main__ import func_3", number=1000))

"""
Результат:

0.000795760000073642
0.0010890170001403021
0.00046327299969561864

Самая быстрая функция - func_3()
"""
