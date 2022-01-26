"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from collections import Counter

array = [x for x in range(1000)]
array.append(1)


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
    return f'Чаще всего встречается число {Counter(array).most_common()[0][0]}' \
           f'оно появилось в массиве {Counter(array).most_common()[0][1]} раз(а)'


setup = 'from __main__ import '

print('func_1 = ', timeit('func_1()', setup=setup + 'func_1', number=1000))
print('func_2 = ', timeit('func_2()', setup=setup + 'func_2', number=1000))
print('func_3 = ', timeit('func_3()', setup=setup + 'func_3', number=1000))

"""
Время выполнения алгоритмов:
                            func_1() - 41.5063634
                            func_2() - 41.5063634
                            func_3() - 0.7994585999999941

Вывод: 
        Выполнение алгоритма получилось ускорить в 40 раз
        (конкретно на этих входных данных)
        Погуглив нашел сложность Counter.most_common() - O(n log n)
        против двух изначальных функций со сложностью  - O(n2)
 """
