from timeit import timeit


array = [1, 3, 3, 4, 5, 4, 4, 3]


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
    new_array = [array.count(i) for i in array]
    numb = array[new_array.index(max(new_array))]
    return f'Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals())) # Ускорить не получилось - второе решение быстрее