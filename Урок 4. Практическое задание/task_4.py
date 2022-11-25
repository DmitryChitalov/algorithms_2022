"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit


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
    kv = {}
    max_i = None
    max_numbers = 0

    for i in array:
        numbers = array.count(i)

        kv[i] = numbers
        if numbers > max_numbers:
            max_i = i
            max_numbers = numbers

    return f"Цифра {max_i} встречается {max_numbers} раз(а)"


print(func_1())
print(func_2())
print(func_3())

test_func_1 = timeit.timeit('func_1()', 'from __main__ import func_1, array', number=10_000)
test_func_2 = timeit.timeit('func_2()', 'from __main__ import func_2, array', number=10_000)
test_func_3 = timeit.timeit('func_3()', 'from __main__ import func_3, array', number=10_000)

print(test_func_1)  # 0.0325442999965162
print(test_func_2)  # 0.04349170000205049
print(test_func_3)  # 0.041860500001348555

# Собственная функция выполняется чуть быстрее, чем вторая. Вероятно, из за того, что элементы в словаре перемещаются
# быстрее, чем в списке.
