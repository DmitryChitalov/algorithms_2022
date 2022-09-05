"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit
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
    result = Counter(array).most_common(1)
    return f'Чаще всего встречается число {result[0][0]}, ' \
           f'оно появилось в массиве {result[0][1]} раз(а)'


def func_4():
    result = max(set(array), key=array.count)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

count_func_1 = timeit.timeit('func_1()', setup='from __main__ import func_1, array')
count_func_2 = timeit.timeit('func_2()', setup='from __main__ import func_2, array')
count_func_3 = timeit.timeit('func_3()', setup='from __main__ import func_3, array')
count_func_4 = timeit.timeit('func_4()', setup='from __main__ import func_4, array')
print(count_func_1, "Результат 1 функции, ")
print(count_func_2, "Результат 2 функции, ")
print(count_func_3, "Результат 3 функции, ")
print(count_func_4, "Результат 4 функции, ")

# Аналитика
# В функции № 3 использовал ипорт модуля и кортежи, что заметно увеличило время выполнения
# В Функции № 4 сложность квадратичная, это самая быстрая из всех функций
# 3.7910486000000003 Результат 1 функции,
# 5.156621599999999 Результат 2 функции,
# 9.537008 Результат 3 функции,
# 3.3450510000000016 Результат 4 функции,