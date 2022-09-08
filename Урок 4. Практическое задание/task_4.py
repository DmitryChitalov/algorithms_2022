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
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print('время выполнения функции func_1()')
print(
    timeit(
        'func_1()',
        globals = globals(),
        number=1000000))
print('*'*30)
print('время выполнения функции func_2()')
print(
    timeit(
        'func_2()',
        globals = globals(),
        number=1000000))
print('*'*30)
print('время выполнения функции func_3()')
print(
    timeit(
        'func_3()',
        globals = globals(),
        number=1000000))

"""
время выполнения функции func_1()
1.5710236879986041
******************************
время выполнения функции func_2()
2.4076299789994664
******************************
время выполнения функции func_3()
1.7337812620007753

третий вариант не дает оптимизации по сравнению с первым вариантом
второй вариант самый затратный.
"""