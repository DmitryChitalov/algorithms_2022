"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 12, 32, 34, 545, 343, 23, 23, 2, 2313, 32, 3342, 34, 21]


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
    a = max(array.count(i) for i in array)
    return f'Чаще всего встречается число {array.index(a)},' \
           f'оно появилось в массиве {a} раз(а)'


def func_4():
    a = max(array, key=array.count)
    return f'Чаще всего встречается число {a}, ' \
           f'оно появилось в массиве {array.count(a)} раз(а)'


'''второе решение самое медленное так как использует цикл и создает новый список и обрабатывает его, первое и третье 
решение являются более оптимальными и сопоставимыми по скорости выполнения ну а самым оптимальным является 4 решение 
так как не использует циклов, а решается с помощью встроенных функций'''

print(func_1())
print(timeit('func_1()', globals=globals(), number=10000))
print(func_2())
print(timeit('func_2()', globals=globals(), number=10000))
print(func_3())
print(timeit('func_3()', globals=globals(), number=10000))
print(func_4())
print(timeit('func_4()', globals=globals(), number=10000))
