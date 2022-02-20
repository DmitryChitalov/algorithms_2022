"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit
from collections import Counter


array = [1, 3, 1, 3, 4, 5, 1]

# Функция 1. Время 0,08 сек - быстрее чем вариант 2
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

# Функция 1. Время 0,12 сек  - медленее чем вариант 1 т.к. идет наполнение массива новыми значениями,
# из которых потом находим максимальное значение.
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Самый быстрый вариант к тому же с элегантным кодом. Функция MAX для массива с ключом по кол-ву - 0,06 сек.

def func_3():
    return max(array, key=array.count)

print(timeit('func_1()', globals=globals(), number=100000))
print(timeit('func_2()', globals=globals(), number=100000))
print(timeit('func_3()', globals=globals(), number=100000))
