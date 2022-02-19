"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

##############################################################################
"""
- Реализация 3: является копией реализации 2, укомплектованной в одну строку,
поэтому по времени практически совпадает с реализациями 1 и 2, где основное
время уходит на то, чтобы пробежать все элементы в списке 

- Реализация 4: аналог реализации 3, только перебор идет не по всем элементам
исходного списка, а лишь по уникальным, за счет чего удается добиться существенного
увеличения скорости работы (при условии, что число уникальных элементов в списке
сильно меньше числа всех элементов в списке).

"""

from timeit import timeit
from random import randint


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
    max_el = max([(x, array.count(x)) for x in array], key=lambda x: x[1])
    return f'Чаще всего встречается число {max_el[0]}, ' \
           f'оно появилось в массиве {max_el[1]} раз(а)'

def func_4():
    max_el = max([(x, array.count(x)) for x in set(array)], key=lambda x: x[1])
    # max_4 = array.count(elem)
    return f'Чаще всего встречается число {max_el[0]}, ' \
           f'оно появилось в массиве {max_el[1]} раз(а)'

array = [randint(1, 10) for i in range(1000)]
print(f'{func_1()} -> {timeit("func_1()", globals=globals(), number=1000):.7f}')
print(f'{func_2()} -> {timeit("func_2()", globals=globals(), number=1000):.7f}')
print(f'{func_3()} -> {timeit("func_3()", globals=globals(), number=1000):.7f}')
print(f'{func_4()} -> {timeit("func_4()", globals=globals(), number=1000):.7f}')