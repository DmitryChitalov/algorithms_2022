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
    n = max(array, key=array.count)
    return f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {array.count(n)} раз(а)'


print(func_1())
print(timeit("func_1()", number=100000, globals=globals()))

print(func_2())
print(timeit("func_2()", number=100000, globals=globals()))

print(func_3())
print(timeit("func_3()", number=100000, globals=globals()))


"""	
func_1 и func_3 работает быстрее, чем func_2, но func_3 проигрывает func_1.
В func_2 использует метод append и создаётся ещё один список и время выполнения функции увеличивается.
""" 