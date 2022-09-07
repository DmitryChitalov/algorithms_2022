"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit


array = [3, 1, 1, 3, 4, 5, 1]


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
    max_count_elem = max(array, key=array.count)
    max_count = array.count(max_count_elem)
    return f'Число {max_count_elem} встречается чаще всего: {max_count} раз(а)'


print(func_1())
print(timeit('func_1()', globals=globals()))
print(func_2())
print(timeit('func_2()', globals=globals()))
print(func_3())
print(timeit('func_3()', globals=globals()))

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
2.62306929999977
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
3.0135897000000114
Число 1 встречается чаще всего: 3 раз(а)
2.5803303000002416
Получилось немного ускорить задачу"""
