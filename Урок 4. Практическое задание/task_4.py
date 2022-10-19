"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 5, 5, 5, 3, 4, 5, 1, 1, 3, 1, 5, 5, 5, 3, 4, 5, 1]


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
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    element = max((array.count(el), el) for el in set(array))
    return f'Чаще всего встречается число {element[1]}, ' \
           f'оно появилось в массиве {element[0]} раз(а)'


if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(func_3())
    print(func_4())

    print(timeit("func_1()", globals=globals(), number=10000))
    print(timeit("func_2()", globals=globals(), number=10000))
    print(timeit("func_3()", globals=globals(), number=10000))
    print(timeit("func_4()", globals=globals(), number=10000))

# функция func_3 - чуть усовершенствовал функцию func_1, за счёт преобразования массива в set.
# Теперь не надо проходить по каждому повторяющемуся элементу.
# На больших массивах должно хорошо работать.
# функция func_4 - так же использовал set и сделал в одну строку с помощью генератора,
# работает чуть медленнее третьего, но значительно быстрее первых двух
