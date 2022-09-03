"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit

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


def func_3(arr):
    max_arr = [arr.count(i) for i in arr]
    count = max(max_arr)
    elem = array[max_arr.index(count)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3(array))

"""
func_1 - быстрее всего, потому что все проверки идут сразу в цикле. единственно, что используется это count()
func_2 - медленней, так как после переборки элементов идут две функции, которые перебирают элементы списка
func_3 - быстрее func_2, так как вместо цикла используется list comprehension
"""

print(timeit.timeit('func_1()', globals=globals()))
print(timeit.timeit('func_2()', globals=globals()))
print(timeit.timeit('func_3(array)', globals=globals()))
