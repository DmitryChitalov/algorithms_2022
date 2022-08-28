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
    new_array = [array.count(n) for n in array]
    return f'Чаще всего встречается число {array[new_array.index( max(new_array))]}, ' \
           f'оно появилось в массиве {max(new_array)} раз(а)'



print(func_1())
print(func_2())
print(func_3())


f1 = """
func_1()
"""

f2 = """
func_2()
"""


f3 = """
func_3()
"""

print(timeit(f1, globals=globals(), number=100000))
print(timeit(f2, globals=globals(), number=100000))
print(timeit(f3, globals=globals(), number=100000))

# Результаты замеров:
# func_1: 0.09930220013484359
# func_2: 0.13643720000982285
# func_3: 0.13771019992418587
# Неудалось ускорить алгоритм



