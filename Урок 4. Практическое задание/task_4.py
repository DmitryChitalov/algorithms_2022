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
    return f'Чаще всего встречается число {max(array, key=array.count)}.'


def func_4():
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit('func_1()', globals=globals(), number=100000))
print(timeit('func_2()', globals=globals(), number=100000))
print(timeit('func_3()', globals=globals(), number=100000))
print(timeit('func_4()', globals=globals(), number=100000))

"""
Вариант func_3 получается самым компактным и самым быстрым, но при этом мы не получаем количество повторений элемента.
Скорость достигается за счет внутренней оптимизации стандартной функции max.
Еще удалось ускорить алгоритм func_1 за счет того, что список сначала преобразовывается в set, что позволяет не вычислять
по несколько раз количество повторений для повторяющихся чисел.
"""