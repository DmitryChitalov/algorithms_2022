from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 5, 3, 5, 4, 8, 9, 8, 7, 5, 2, 2, 2]


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
    elem = max(array, key=lambda x: array.count(x))
    count = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit('func_1()', globals=globals(), number=100000))
print(timeit('func_2()', globals=globals(), number=100000))
print(timeit('func_3()', globals=globals(), number=100000))

'''
1.4969273
1.6708124999999998
1.5430853999999998
Выполнить задачу быстрее не получилось, func_1 выполнает задачу быстрее, 
однако func_3 более лаконична и решается в одну строку!
'''
