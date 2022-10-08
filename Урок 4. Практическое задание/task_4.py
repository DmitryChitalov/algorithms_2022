"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import Timer


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
    return f'Чаще всего встречается число {max(sorted(array, reverse=True), key = lambda x: array.count(x))}'


# print(func_1())
# print(func_2())
# print(func_3())

t1 = Timer(stmt="func_1()", setup="from __main__ import func_1", globals=globals())
print("Время func_1(): ", t1.timeit(number=10000), "seconds")

t2 = Timer(stmt="func_2()", setup="from __main__ import func_2", globals=globals())
print("Время func_2(): ", t2.timeit(number=10000), "seconds")

t3 = Timer(stmt="func_3()", setup="from __main__ import func_3", globals=globals())
print("Время func_3(): ", t3.timeit(number=10000), "seconds")

"""
Ускорить не удалось. Самый быстрый способ указан в самой простой функции func_1
func_2 - чуть медленнее, т.к. формируется 2-ой список, на который тратится время
func_3 - еще медленнее, т.к. помимо формирования неявного второго списка, он еще и подвергается сортировке,
с определением максимального значения
"""
