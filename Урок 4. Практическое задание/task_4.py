"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit
from collections import Counter

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
    sorted_array = sorted([(i, array.count(i)) for i in set(array)], key=lambda x: x[1])[-1]
    return f'Чаще всего встречается число {sorted_array[0]}, ' \
           f'оно появилось в массиве {sorted_array[1]} раз(а)'


def func_4():
    max_val = Counter(array).most_common(1)[0][0]
    max_count = Counter(array).most_common(1)[0][1]
    return f'Чаще всего встречается число {max_val}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


def func_5():
    new_array = [array.count(el) for el in array]

    maximum = max(new_array)
    elem = array[new_array.index(maximum)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {maximum} раз(а)'


print('Функция 1.')
print(func_1())
print(timeit(f'func_1()', globals=globals()))
print('Функция 2.')
print(func_2())
print(timeit(f'func_2()', globals=globals()))
print('Функция 3.')
print(func_3())
print(timeit(f'func_3()', globals=globals()))
print('Функция 4.')
print(func_4())
print(timeit(f'func_4()', globals=globals()))
print('Функция 5.')
print(func_5())
print(timeit(f'func_5()', globals=globals()))

"""
Функция 1.
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.7167291000005207
Функция 2.
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.9372978999999759
Функция 3.
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
1.1768367000004218
Функция 4.
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
3.9678601999985403
Функция 5.
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.9134387999984028

Process finished with exit code 0

"""

"""
Вывод: Функция 1 - самая быстрая, так как есть только цикл и одно условие переопределения счетчика.
    Функция 2 - медленее функции 1, так как есть два перебора в цикле и методе count.
    Функция 3 - медленее функции 2, так как есть итератор sorted и lambda функция.
    Функция 4 - самая медленная, так как идет извлечение элементов из класса Counter с методом most_common.
    Функция 5 - медленее функции 1, но быстрее функции 2, так как цикл перевели в LC.
"""