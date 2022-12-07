"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit
from random import randint

# array = [1, 3, 1, 3, 4, 5, 1]  # Исходный массив
array = [randint(0, 9) for _ in range(10000)]


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
    """
    аботает нестабильно на больших массивах.
    Предполагаю, что это может быть связано с функцией сортировки sorted()
    """
    my_dict = {}
    sorted_array = sorted(array)
    count = 1
    for i in range(1, len(array)):
        if sorted_array[i] != sorted_array[i - 1]:
            count = 1
        else:
            count += 1
        my_dict[sorted_array[i]] = count
    key = max(my_dict, key=my_dict.get)
    return f'Чаще всего встречается число {key}, '\
           f'оно появилось в массиве {my_dict[key]} раз(а)'


def func_4():
    """
    Работает нестабильно на больших массивах.
    Предполагаю, что это может быть связано с функцией сортировки sorted()
    """
    my_list = sorted(array)
    count = 1
    max_rep = 1
    num = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] == my_list[i - 1]:
            count += 1
        else:
            if count > max_rep:
                max_rep = count
                num = my_list[i - 1]
            count = 1
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_rep} раз(а)'


def func_5():
    """
    Работает наиболее эффективно, когда массив состоит из огромного количества простых чисел
    Работает стабильно.
    """
    my_set = set()
    max_rep = 0
    num = 0
    for item in array:
        if item not in my_set:
            rep = array.count(item)
            my_set.add(item)
            if rep > max_rep:
                max_rep = rep
                num = item
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_rep} раз(а)'


print(func_1())
t1 = timeit(stmt="func_1()", setup="from __main__ import func_1", number=1)
print(f'{t1:.7f} сек')
print(func_2())
t2 = timeit(stmt="func_2()", setup="from __main__ import func_2", number=1)
print(f'{t2:.7f} сек')
print(func_3())
t3 = timeit(stmt="func_3()", setup="from __main__ import func_3", number=1)
print(f'{t3:.7f} сек: func_3: '
      f'ускорение относительно func_1 в {t1 / t3:.0f} раз')
print(func_4())
t4 = timeit(stmt="func_4()", setup="from __main__ import func_4", number=1)
print(f'{t4:.7f} сек: func_4: '
      f'ускорение относительно func_1 в {t1 / t4:.0f} раз')
print(func_5())
t5 = timeit(stmt="func_5()", setup="from __main__ import func_5", number=1)
print(f'{t5:.7f} сек: func_5: '
      f'ускорение относительно func_1 в {t1 / t5:.0f} раз(а)')
