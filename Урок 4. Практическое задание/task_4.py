"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

"""
---Что сделал и выводы---
При реализации своего варианта (func_3) использовал функцию max() и lambda функцию - код стал немного компактней.
Что касается времени исполнения кода:
1) Если выводить только число которое встречается чаще, то код работает быстрее, 
чем приведенные в задании (func_1, func_2).
2) Если рассматривать, что требуется еще вывести сколько раз встречается число, то код выполняется немного медленнее
представленных в задании (func_1, func_2). Так как при возвращении функцией количества раз сколько встречается число
использовал метод count
"""

from timeit import timeit  # Импорт timeit

array = [1, 3, 1, 3, 4, 5, 3]


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
    max_el = max(array, key=lambda i: array.count(i), default='Введен пустой список')

    return f'Чаще всего встречается число {max_el}, ' \
           f'оно появилось в массиве {array.count(max_el)} раз(а)'


print(func_1())
print('Время выполнения функции func_1')
print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=10000))

print(func_2())
print('Время выполнения функции func_2')
print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=10000))

print(func_3())
print('Время выполнения функции func_3')
print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=10000))
