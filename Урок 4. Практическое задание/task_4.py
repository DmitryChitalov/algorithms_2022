"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
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
    ar_tup = set(array)
    max_count = 0
    max_val = 0
    for i in ar_tup:
        if array.count(i) > max_count:
            max_val = i
            max_count = array.count(i)
    return f'Чаще всего встречается число {max_val}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


print(func_1())

print(
    timeit(
        'func_1()',
        globals=globals(),
        number=10000))

print(func_2())

print(
    timeit(
        'func_2()',
        globals=globals(),
        number=10000))

print(func_3())

print(
    timeit(
        'func_3()',
        globals=globals(),
        number=10000))

'''
У меня получилось совсем немного ускорить работу функции.
Я усовершенствовал первую функцию посредством того, что исключил лишние
итерации в цикле, сделав кортеж из списка и получил последовательность с уникальными значениями,
пройдясь по котором циклом я определил число встречающееся в списке больше всего 
'''