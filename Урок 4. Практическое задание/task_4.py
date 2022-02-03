"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from collections import Counter
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
    number = Counter(array).most_common(1)
    return f'Чаще всего встречается число {number[0][0]},' \
           f'оно появилось в массиве {number[0][1]} раз(а)'


def func_4():
    return f'Чаще всего встречающееся число и количество вхождений в массив: {str(Counter(array).most_common(1)).strip("[()]")}'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f'Замер времени функции func_1: {timeit("func_1", "from __main__ import func_1", number=10000)}')
print(f'Замер времени функции func_2: {timeit("func_2", "from __main__ import func_2", number=10000)}')
print(f'Замер времени функции func_3: {timeit("func_3", "from __main__ import func_3", number=10000)}')
print(f'Замер времени функции func_3: {timeit("func_4", "from __main__ import func_4", number=10000)}')
