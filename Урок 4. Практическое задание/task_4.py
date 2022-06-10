"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
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
    count = Counter(array)
    return count.most_common()[0]


def func_4():
    number = sorted([(i, array.count(i)) for i in set(array)],key=lambda t:t[1])[-1]
    return number


def func_5():
    number = max(array, key=array.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(timeit("func_1()", globals=globals()))  # 2.493648698, 3.087844325, 3.0511523799999996
print(timeit("func_2()", globals=globals()))  # 3.7249438319999997, 3.7758133660000004, 4.11782474
print(timeit("func_3()", globals=globals()))  # 14.003667142000001, 5.105828634, 13.314114329999999
print(timeit("func_4()", globals=globals()))  # 3.7526573749999983, 3.3373737719999994, 3.2496542429999984
print(timeit("func_5()", globals=globals()))  # 2.592655781999998, 3.061455519000001, 2.3903086139999985

# Решением в одну строку является использование функции max в func_5, собственно, эта же функция работает быстрей из
# всех представленных. Время выполнения хадачи было оптимизировано.
