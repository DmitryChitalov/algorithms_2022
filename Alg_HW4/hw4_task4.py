"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
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
    dictionary = {elem: 0 for elem in array}
    for el in array:
        dictionary[el] += 1
    m = 0
    num = 0
    for key in dictionary.keys():
        if dictionary[key] > m:
            m = dictionary[key]
            num = key
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    dictionary = {elem: 0 for elem in array}
    for el in array:
        dictionary[el] += 1
    for key, el in dictionary.items():
        if el == max(dictionary.values()):
            return f'Элемент {key} встречается {el} раз(a)'


def func_5():
    # просто постарался сделать функцию в одну строчку)
    dictionary = max(({array.count(elem): elem for elem in array}).items())
    return f'Чаще всего встречается число {dictionary[1]} ' \
           f'оно появилось в массиве {dictionary[0]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())
print(timeit('func_1()', number=1000000, globals=globals()))
print(timeit('func_2()', number=1000000, globals=globals()))
print(timeit('func_3()', number=1000000, globals=globals()))
print(timeit('func_4()', number=1000000, globals=globals()))
print(timeit('func_5()', number=1000000, globals=globals()))
#
# 1.9587552049999999 - самая лучшая первая
# 2.456988682
# 2.15088526 - третья - лучшая из тех, что вышли, в целом похожа на первую
# 2.244016959999999 - похожа на третью, но чуть другая
# 2.5567178419999994 - плохо, зато лаконично)
