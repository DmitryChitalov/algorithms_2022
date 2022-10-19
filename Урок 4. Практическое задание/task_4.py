"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit, default_timer

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
    dct ={}
    for el in array:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1

    # dct = {k: v for k, v in dct.items() if v == max_count}
    # max_count = max(dct.values())
    max_count = max(dct.values())
    res_dct = {k: v for k, v in dct.items() if v == max_count}
    elem = list(res_dct.keys())[0]
    # elem = res_dct.popitem[0]


    # return max_count, elem
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'

# def func_3():
#     array.sort()
#     elem = array[-1]
#     for el in array:
#         count = array.count(el)
#     return elem, count


print(func_1())
print(func_2())
print(func_3())

print(timeit('func_1()', 'from __main__ import func_1', default_timer, 10000))
print(timeit('func_2()', 'from __main__ import func_2', default_timer, 10000))
print(timeit('func_3()', 'from __main__ import func_3', default_timer, 10000))

# Выводы: Ускорения не удалось добиться
