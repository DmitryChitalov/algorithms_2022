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
    max_count_el = max(array, key=array.count)
    return f'Чаще всего встречается число {max_count_el}, ' \
           f'оно появилось в массиве {array.count(max_count_el)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print("func_1:", timeit(f"func_1()", globals=globals()))

print("func_2:", timeit(f"func_2()", globals=globals()))

print("func_3:", timeit(f"func_3()", globals=globals()))

"""
Результаты
func_1: 0.6875375999952666
func_2: 0.9235323999891989
func_3: 0.7715817000134848
func_3 имеет среднюю по скорости длительность выполнения. 
Она выполняется быстрее, чем func_2, но медленее, чем func_1.
"""
