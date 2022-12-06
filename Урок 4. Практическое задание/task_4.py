"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import Timer

array = [1, 3, 1, 3, 4, 5, 1, 1]

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


print(func_1())
print(func_2())

def func_3():
    res = [array.count(array[i]) for i in range(len(array))]    
    return f'Чаще всего встречается число {array[res.index(max(res))]}, ' \
           f'оно появилось в массиве {max(res)} раз(а)'

print(func_3())

t1 = Timer(stmt= "func_1", setup="from __main__ import func_1")
print(t1.timeit(number = 10000000))

t2 = Timer(stmt= "func_2", setup="from __main__ import func_2")
print(t2.timeit(number = 10000000))

t3 = Timer(stmt= "func_3", setup="from __main__ import func_3")
print(t3.timeit(number = 10000000))

#Списковое включение работает быстрее, чем циклы, функция стала работать быстрее 