"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу

Описание 3-го решения:
Создается словарь где значения элеменов массива в качестве ключей,
количество повторений этого элемента - значение словаря
Находим максимум из значений словаря, для этого значения находим ключ - элемент заданного списка.

Тайминг решений (для 10000 вызовов) :
 func_1 > 0.8404927 sec - с помощью count
 func_2 > 1.1213426 sec - с помошью 2-го массива с количеством повторений
 func_3 > 1.1753663 sec - с помощью словаря

С помощью 3-го варианта решение ускорить не получилось.
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
    new_dict = {}
    for el in array:
        if el in new_dict:
            new_dict[el] += 1
        else:
            new_dict[el] = 1
    # print (new_dict)
    max_count = max(new_dict.values())
    # print (max_value )
    max_count_value = max(new_dict, key=new_dict.get)

    return f'Чаще всего встречается число {max_count_value}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


print('')
print(func_1())
print(func_2())
print(func_3())

print('')
print(f' func_1 > {timeit("func_1()", globals=globals())} sec')
print(f' func_2 > {timeit("func_2()", globals=globals())} sec')
print(f' func_3 > {timeit("func_3()", globals=globals())} sec')

# script listing
#
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
#
#  func_1 > 0.8404927999999999 sec
#  func_2 > 1.1213426 sec
#  func_3 > 1.1753663 sec
#
# Process finished with exit code 0

