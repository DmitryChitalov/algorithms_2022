"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import default_timer
from collections import Counter


def time_it(n):
    def deco(func):
        def wrapper(*args):
            t_sum = 0
            for el in range(n):
                start_time = default_timer()
                func(*args)
                delta = default_timer() - start_time
                t_sum += delta
            return f'{func.__name__}: {func(*args)}, {t_sum}'
        return wrapper
    return deco


array = [1, 3, 1, 3, 4, 5, 1]


@time_it(10000)
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


@time_it(10000)
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@time_it(10000)
def func_3():
    c = Counter(array).most_common(1)
    return f'Чаще всего встречается число {c[0][0]}, ' \
           f'оно появилось в массиве {c[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print('\nВывод: первая функция отрабатывает быстрее остальных, моя добавленная функция с использованием '
      '"батарейки" оказалась лаконичной, но самой медленной')
