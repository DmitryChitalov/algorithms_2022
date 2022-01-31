"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

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
    cnt = Counter(array).most_common(1)
    return f'Чаще всего встречается число {cnt[0][0]}, ' \
           f'оно появилось в массиве {cnt[0][1]} раз(а)'


if __name__ == '__main__':
    from collections import Counter
    import timeit

    # print(func_1())
    # print(func_2())
    # print(func_3())

    t = timeit.Timer(lambda: func_1())
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_2())
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_3())
    print(t.repeat(3))


# Использование простого цикла с функцией поиска и перезаписи числа вхождений в первом варианте
# оказывается наиболее экономичным решением.
# Второй вариант усложняет первый, используя создание другого массива с количеством вхождений,
# потом поска максимального значения и взятия по индексу.
# третий вариант с использованием функции Counter из Collections оказался самым неудачным по затратам
# времени на выполнение операций.
