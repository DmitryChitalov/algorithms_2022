"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import random
from timeit import timeit

array = []
for _ in range(100):
    array.append(random.randrange(100, 199))

print(array)


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
    lc_list = [array.count(el) for el in array]
    max_value = max(lc_list)
    return \
        f'Чаще всего встречается число {array[lc_list.index(max_value)]}, ' \
        f'оно появилось в массиве {max_value} раз(а)'


lc_max = max({el: array.count(el) for el in array if array.count(el) > 0}.items(), key=lambda i: i[1])
# lc_max = max([[el, array.count(el)] for el in array if array.count(el) > 0], key=lambda i: i[1])

print(lc_max)
print(
    f'Чаще всего встречается число {lc_max[0]}, '
    f'оно появилось в массиве {lc_max[1]} раз(а)'
)

print(func_1())
print(func_2())
print(func_3())
print(
    timeit(
        "func_1()",
        globals=globals(),
        number=1000
    )
)
print(
    timeit(
        "func_2()",
        globals=globals(),
        number=1000
    )
)
print(
    timeit(
        "func_3()",
        globals=globals(),
        number=1000
    )
)

# Замер lc
print(
    timeit(
        "max({i: array.count(i) for i in array if array.count(i) > 0}.items(), key=lambda i: i[1])",
        globals=globals(),
        number=1000
    )
)

"""
Вывод:
func_3 работает чуть быстрее, но не на много, все 3 функции работают примерно с одной скоростью,
единственное func_3 получилась компактнее
решение в 1 строку получилось самое медленное и выполняется в 2 раза дольше функций, 
но за то получается сгруппированный словарь в котором каждое значение имеет кол-во повторений
к примеру если будет требоваться дальнейшее использование
"""
