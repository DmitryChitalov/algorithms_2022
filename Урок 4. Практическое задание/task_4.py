"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from random import randint
from timeit import timeit

# array = [1, 3, 1, 3, 4, 5, 1]
array = [randint(1, 5) for i in range(100)]  # для большей информативности теста производительности увеличил массив


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_3 = max([(array.count(el), el) for el in set(array)])
    return f'Чаще всего встречается число {max_3[1]}, оно появилось в массиве {max_3[0]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

for func in (func_1, func_2, func_3):
    print(f'{func.__name__}: {timeit("func()", globals=globals(), number=1000)}')


"""
При маленьком размере исходного списка первая функция кажется самой производительной, но func_3 выглядит гораздо
лаконичнее. С увеличением размера массива становится понятно, что помимо лаконичности func_3 обладает высокой
производительностью. Скорость выполнения func_3 при размере массива в 100 элементов выше в 14 раз. 
"""