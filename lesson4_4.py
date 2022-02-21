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
    return f'"Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)"'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'"Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)"'


def func_3():
    res = list(Counter(array).items())[0]
    return f'"Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)"'


print(f'Вариант 1: {func_1()} за {timeit("func_1", globals=globals(), number=10000000)}')  # 0.22
print(f'Вариант 1: {func_2()} за {timeit("func_2", globals=globals(), number=10000000)}')  # 0.20
print(f'Вариант 1: {func_3()} за {timeit("func_2", globals=globals(), number=10000000)}')  # 0.18

"""
Оценки получаются практически одинаковые с учетом погрешности, первые два алгоритма работают при помощи циклов, поэтому
скорость совпадает, третий вариант "под копотом" имеет схожий механизм с первыми, но код его более лаконичен.
"""
