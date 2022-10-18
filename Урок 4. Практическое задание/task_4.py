"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from cProfile import run

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
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, оно появлялось в массиве {array.count(numb)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print()


def main():
    func_1()
    func_2()
    func_3()


print(
    timeit(
        "func_1()",
        setup="from __main__ import func_1, array", number=10000))

print(
    timeit(
        "func_2()",
        setup="from __main__ import func_2, array", number=10000))

print(
    timeit(
        "func_3()",
        setup="from __main__ import func_3, array", number=10000))

run('main()')

"""
Лучше всего работает третий вариант с использованием встроенной функции MAX, func_3. O(n)
Второе место у функции с циклом FOR ... IN, func_1. O(n).
И наконец третье место у функции с FOR ... IN, но использующую много лишних операций и встроенных функций, func_3. O(n)
Профиллировку работы функции тоже сделана.
Разница работы функций не значительна и видимо ощутима только при большом чимле входных данных и колличестве проходов
func_1() = 0.023585799615830183
func_2() = 0.028392700012773275
func_3() = 0.019423600286245346
"""