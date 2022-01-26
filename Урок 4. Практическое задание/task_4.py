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
# array = [1, 3, 1, 3, 4, 5, 1, 8, 9, 5, 7, 1, 4, 9, 2, 5, 5, 2, 3, 7, 5, 6, 7, 8, 9, 4, 3, 4, 6]


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
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


def func_4():
    num = 0
    m = 0
    for i in set(array):
        if m < array.count(i):
            m = array.count(i)
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print('Время работы func_1 - ', end='')
print(timeit('func_1()', setup='from __main__ import func_1, array', number=1000000))
print('Время работы func_2 - ', end='')
print(timeit('func_2()', setup='from __main__ import func_2, array', number=1000000))
print('Время работы func_3 - ', end='')
print(timeit('func_3()', setup='from __main__ import func_3, array', number=1000000))
print('Время работы func_4 - ', end='')
print(timeit('func_4()', setup='from __main__ import func_4, array', number=1000000))


'''
func_3 сокращенная версия func_2. Работает быстрее за счет исключения промежуочных переменных, и цыкла.
func_4 сокращеная версия func_1. Работает быстрее всех за счет использования множеств, для перебора только уникальных 
значений, сорашение итераций цикла.
Время работы func_1 - 1.5178515
Время работы func_2 - 2.3941559000000003
Время работы func_3 - 1.3317020000000004
Время работы func_4 - 1.2659409000000004

Скорость работы func_4 особенно заметно при большем списке, и большем кол-ве повторяющихся значений.
array = [1, 3, 1, 3, 4, 5, 1, 8, 9, 5, 7, 1, 4, 9, 2, 5, 5, 2, 3, 7, 5, 6, 7, 8, 9, 4, 3, 4, 6]
Время работы func_1 - 12.0993135
Время работы func_2 - 14.580288599999998
Время работы func_3 - 11.164420800000002
Время работы func_4 - 5.285316899999998
'''

