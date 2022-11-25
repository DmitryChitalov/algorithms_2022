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
    count_dict = {array.count(x): x for x in array}
    max_3 = max(count_dict)
    el = count_dict[max_3]
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


print(timeit("func_1", setup='from __main__ import func_1', number=100000))
print(timeit("func_2", setup='from __main__ import func_2', number=100000))
print(timeit("func_3", setup='from __main__ import func_3', number=100000))


"""
При запуске всего кода в 3х из 5 случаев func_3 дает лучшие результаты по времени. 
Получилось написать короткое решение с использованием dict comprehenshion,
который работает быстрее традиционного итератора.
"""