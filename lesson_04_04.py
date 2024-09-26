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


# Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
def func_3():
    return f'Чаще всего встречающееся число и количество вхождений в массив: {str(Counter(array).most_common(1)).strip("[()]")}'


# Сделайте профилировку каждого алгоритма через timeit


print(f'Замер времени функции func_1: {timeit("func_1", "from __main__ import func_1", number=1000)}')
print(f'Замер времени функции func_2: {timeit("func_2", "from __main__ import func_2", number=1000)}')
print(f'Замер времени функции func_3: {timeit("func_3", "from __main__ import func_3", number=1000)}')

"""
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Использование Counter позволило ускорить время выполнения задачи и длину кода
***
Замер времени функции func_1: 1.409999999999953e-05
Замер времени функции func_2: 1.559999999999756e-05
Замер времени функции func_3: 1.1799999999999311e-05
***

"""
