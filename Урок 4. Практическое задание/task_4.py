from timeit import timeit
from collections import Counter
"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

array = [1, 3, 1, 3, 4, 5, 1]

array_2 = [x for x in range(1000)]
array_2.append(1)


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
    return  f"Чаще всего встречается число {Counter(array).most_common()[0][0]}"\
            f" оно появилось в массиве {Counter(array).most_common()[0][1]} раз(а)"

def func_4():
    m = 0
    num = 0
    for i in array_2:
        count = array_2.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

def func_5():
    return f"Чаще всего встречается число {Counter(array_2).most_common()[0][0]}" \
           f" оно появилось в массиве {Counter(array_2).most_common()[0][1]} раз(а)"

print(func_1())
print(func_2())
print(func_3())

setup = 'from __main__ import '

print('func_1 = ', timeit('func_1()', setup=setup + 'func_1', number=1000))
print('func_2 = ', timeit('func_2()', setup=setup + 'func_2', number=1000))
print('func_3 = ', timeit('func_3()', setup=setup + 'func_3', number=1000))
print('func_4 = ', timeit('func_4()', setup=setup + 'func_4', number=1000))
print('func_5 = ', timeit('func_5()', setup=setup + 'func_5', number=1000))


"""     Анализ
    Время выполнения операций:
        func_1 =  0.0023877000000000065
        func_2 =  0.003768300000000002
        func_3 =  0.010669300000000007
    Вывод1 когда массив мелкий мой вариант с применением класса Counter() будет менее эфективным
    Время выполнения операций 2:
        func_4 =  12.012341399999999
        func_5 =  0.25204119999999897
    Вывод 2 чем больше массив тем эффективней по времени становится класс Counter()
"""