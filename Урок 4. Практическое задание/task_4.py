"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 3, 3]


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
    counted_nums = {}

    for el in array:
        if el in counted_nums:
            counted_nums[el] += 1
        else:
            counted_nums[el] = 1
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {max(counted_nums.values())} раз(а)'


def func_4():
   num = max(array, key=array.count)
   return f'Чаще всего встречается число {num}, ' \
          f'оно появилось в массиве {array.count(num)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())


print(timeit("func_1()", globals=globals(), number=1000))       # 0.001927200000000004
print(timeit("func_2()", globals=globals(), number=1000))       # 0.0025773999999999936
print(timeit("func_3()", globals=globals(), number=1000))       # 0.0017983000000000027  получилось ускорить за счет
                                                                # использования словаря
print(timeit("func_4()", globals=globals(), number=1000))       # 0.002022999999999997   скорость сопоставима с циклом
