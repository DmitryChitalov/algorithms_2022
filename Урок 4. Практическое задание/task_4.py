"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
import collections

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


print('func_1:', timeit('func_1()', globals=globals(), number=1000))


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print('func_2:', timeit('func_2()', globals=globals(), number=1000))


def func_3(array):
    a = collections.Counter(array).most_common()[0][0]
    return f'Чаще всего встречается число {a}, ' \
           f'оно появилось в массиве {array.count(a)} раз(а)'


print('func_3:', timeit('func_3(array)', globals=globals(), number=1000))

'''Познакомился с данной функцией из модуля, но работу он не ускорил'''


def func_4(array):
    a = max(map(lambda val: (array.count(val), val), set(array)))
    return f'Чаще всего встречается число {a[1]}, ' \
           f'оно появилось в массиве {a[0]} раз(а)'


print('func_4:', timeit('func_4(array)', globals=globals(), number=1000))

print()
print(func_1())
print(func_2())
print(func_3(array))
print(func_4(array))

'''func_4 сразу определяет максимум включений числа в массив, за счёт этого, работает быстрее'''
