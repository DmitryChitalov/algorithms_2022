"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
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
    elem = max(set(array), key=array.count)
    return f'Чаще всего встречается число {elem}, '\
           f'оно появилось в массиве {array.count(elem)} раз(а)'


def func_4():
    mydict = {}
    maxnum = 0
    for i in array:
        num = mydict.get(i)
        if num:
            num = num + 1
            mydict[i] = num
            if num > maxnum:
                maxnum = num
                maxval = i
        else:
            mydict.setdefault(i, 1)
    return f'Чаще всего встречается число {maxval}, '\
           f'оно появилось в массиве {maxnum} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print('Small arrray:')
print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))
print(timeit('func_4()', globals=globals()))

array = [6, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1]

print('Big arrray:')
print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))
print(timeit('func_4()', globals=globals()))

'''
Получилось ускорить выполнение задачи двумя способами. 
Функция 3 работает быстрее, чем первые 2, и на большом и на небольшом объёме данных.
Функция 4 работает быстрее на большом объёме данных.
Аналитика:
Функции 1 и 2 имеют сложность О(n^2), так как при переборе элементов массива вызывается array.count,
          что создаёт вложенный цикл.
Функция 3 также имеет сложность О(n^2), но превращает список в сэт, тем самым убирая повторы, 
          и затем по каждому элементу сэта вызывает array.count().
          Такми образом array.count вызывается только один раз для каждого уникального элемента списка.
Функция 4 перебирвает список только один раз, составля словарь с количеством повторов элементов списка.
 
'''