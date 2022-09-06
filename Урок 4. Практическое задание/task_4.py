"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
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
    # try:
    maximum = max(array, key=array.count)
    return f'Чаще всего встречается число {maximum}, ' \
    f'оно появилось в массиве {array.count(maximum)} раз(а)'

t_1 = timeit('func_1()', globals=globals(), number=100000)
t_2 = timeit('func_2()', globals=globals(), number=100000)
t_3 = timeit('func_3()', globals=globals(), number=100000)

print(func_1())
print(f'Время выполнения func_1 = ', round(t_1, 3))
print(func_2())
print(f'Время выполнения func_2 = ', round(t_2, 3))
print(func_3())
print(f'Время выполнения func_3 = ', round(t_3, 3))

#Решение задачи получилось ускорить,т.к. встроенные функции выполняются быстрее.
# Самая быстрая func_3, затем func_2, а самая долгая по выполнению func_1.