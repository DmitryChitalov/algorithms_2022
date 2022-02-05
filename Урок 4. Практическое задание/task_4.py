"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
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
    x = max(zip((array.count(item) for item in set(array)), set(array)))
    return f'Чаще всего встречается число {x[1]}, оно появилось в массиве {x[0]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("func_3()", globals=globals()))
"""
1)Самый быстрый алгоритм, так как тут только присвоение значений переменным.
1.6747713000000002
2)Быстрее первого так как происходит создание нового списка со всеми элементами из первого
2.3089058
3)Мое решение получилось самым долгим, так как создается набор из всех чисел и потом выводит: максимальное число 
повторений и какое именно число.
2.6119959999999995
"""
