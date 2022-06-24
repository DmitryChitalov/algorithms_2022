from collections import Counter
from timeit import timeit
"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
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


def func_3(arr):
    count_max = Counter(arr).most_common()
    return f'Чаще всего встречается число {count_max[0][0]}, ' \
           f'оно появилось в массиве {count_max[0][1]} раз(а)'


def func_4(arr):
    new_arr = [arr.count(i) for i in arr]

    return f'Чаще всего встречается число ' \
           f'{arr[new_arr.index(max(new_arr))]}, ' \
           f'оно появилось в массиве {max(new_arr)} раз(а)'


print(func_1())
print(func_2())
print(func_3(array))
print(func_4(array))

print(timeit(stmt='func_1()', number=1000, globals=globals()))
print(timeit(stmt='func_2()', number=1000, globals=globals()))
print(timeit(stmt='func_3(array)', number=1000, globals=globals()))
print(timeit(stmt='func_4(array)', number=1000, globals=globals()))

"""
Результаты:
func_1 0.0019342000014148653
func_2 0.002612499985843897
func_3 0.0034590999712236226
func_4 0.0026227000053040683

Выаод:
Исходя из результатов замера, наилучшей скорость выполнения обладает func_1
Предложенное мною решение func_3 при помощи класса Counter выполняется дольше 
всех, однако самое компактное. Ускорить работу не получилось.
"""
