from collections import Counter
from timeit import timeit
"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

array = [1, 3, 1, 3, 4, 5, 1]

def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
def func_3(array):
    res = Counter(array).most_common()
    return f'Чаще всего встречается число {res[0][0]}' \
           f', оно появилось в массиве {res[0][1]} раз(а)'
def func_4(array):
    res = max(zip((array.count(item) for item in set(array)), set(array)))
    return f'Чаще всего встречается число {res[1]},оно появилось в массиве {res[0]} раз(а)'


def func_5(array):
    cnt = max(map(array.count, array))
    return f'Чаще всего встречается число {max(a for a in array if array.count(a) == cnt)},оно появилось в массиве {cnt} раз(а)'

def func_6(array):
    num = max((array), key=array.count)
    return f'Чаще всего встречается число {num},  оно появилось в массиве {array.count(num)} раз(а)'



# print(func_1())
# print(func_2())
# print(func_3())
# print(func_4())
# print(func_5())
# print(func_6())

print(timeit("func_1(array)",
        globals=globals(),
        number=100000))

print(timeit("func_2(array)",
        globals=globals(),
        number=100000))

print(timeit("func_3(array)",
        globals=globals(),
        number=100000))

print(timeit("func_4(array)",
        globals=globals(),
        number=100000))

print(timeit("func_5(array)",
        globals=globals(),
        number=100000))

print(timeit("func_6(array)",
        globals=globals(),
        number=100000))


"""Получилось минимально ускорить решение с помощью функции func_6 (Можно объяснить тем, что этот способ не требует большого количества щагов в и тем, что
строенная функция- работает быстрее). """



