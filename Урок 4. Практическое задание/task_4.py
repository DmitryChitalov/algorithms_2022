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


def func_3():
    num = max(array, key=lambda x: array.count(x))
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


print(timeit("func_1", globals=globals()))  # 0.03171569999994972
print(timeit("func_2", globals=globals()))  # 0.02477889999954641
print(timeit("func_3", globals=globals()))  # 0.023863800000071933

''' Моя функция самая быстрая, т.к. в ней используются max() и count(). 
    Это встроеные функции, поэтому они работают быстрее циклов. '''
