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
    a = max(array, key=array.count)
    return f'Чаще всего встречается число {a}, ' \
           f'оно появилось в массиве {array.count(a)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print("First: " + str(timeit("func_1()", "from __main__ import func_1, array", number=1000)))
print("Second: " + str(timeit("func_2()", "from __main__ import func_2, array", number=1000)))
print("Third: " + str(timeit("func_3()", "from __main__ import func_3, array", number=1000)))

"""
First: 0.0016771000809967518
Second: 0.0041584999999031425
Third: 0.0015302000101655722
Третий вариант самый быстрый
"""
