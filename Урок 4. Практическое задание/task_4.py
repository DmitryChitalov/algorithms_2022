"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit, default_timer, repeat
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
    dct = {}
    for el in array:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1

    max_count = max(dct.values())
    res_dct = {k: v for k, v in dct.items() if v == max_count}
    elem = list(res_dct.keys())[0]
    # elem = res_dct.popitem[0]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


def func_4():
    obj = Counter(array).most_common(1)
    return f'Чаще всего встречается число {obj[0][0]}, ' \
           f'оно появилось в массиве {obj[0][1]} раз(а)'
def func_5():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print('func_1', timeit('func_1()', 'from __main__ import func_1', default_timer, 10000))
print('func_1', repeat('func_1()', 'from __main__ import func_1', default_timer, 3, 10000))
print('func_2', timeit('func_2()', 'from __main__ import func_2', default_timer, 10000))
print('func_2', repeat('func_2()', 'from __main__ import func_2', default_timer, 3, 10000))
print('func_3', timeit('func_3()', 'from __main__ import func_3', default_timer, 10000))
print('func_3', repeat('func_3()', 'from __main__ import func_3', default_timer, 3, 10000))
print('func_4', timeit('func_4()', 'from __main__ import func_4', default_timer, 10000))
print('func_4', repeat('func_4()', 'from __main__ import func_4', default_timer, 3, 10000))
print('func_5', timeit('func_5()', 'from __main__ import func_5', default_timer, 10000))
print('func_5', repeat('func_5()', 'from __main__ import func_5', default_timer, 3, 10000))

# func_1 - цикл
#   0.014843399985693395
# func_2 - массив
#   0.017082299920730293
# func_3 - словарь
#   0.022876799921505153
# func_4 - Counter
#   0.04486410005483776
# func_5 - функция max
#   0.01233269996009767

# Выводы: Варианты 3, 4 (операции со словарем) - ускорения не удалось добиться, т.к. при добавлении элементов в словарь - вычисляется хэш и требуется дополнительное время.
# вариант 5  с функцией max - ускорение.