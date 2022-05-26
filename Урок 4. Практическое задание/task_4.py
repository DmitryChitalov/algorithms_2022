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

def my_func():
    return  f'Чаще всего встречается число {max(array,key=lambda x : array.count(x))}'

if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(my_func())

    print(f'Замер функции func_1: {timeit("func_1()", number=10000, globals=globals())}')  # 0.01
    print(f'Замер функции func_2: {timeit("func_2()", number=10000, globals=globals())}')  # 0.014
    print(f'Замер функции my_func: {timeit("func_2()", number=10000, globals=globals())}')  # 0.013

    """
    В задаче требуется найти число которое встречается наиболшее количество раз. В задании не требуется указывать
    сколько раз оно встречается. Поэтому удалось решить задачу используя встроенную функцию max. Но все равно 
    первый алгоритм работает быстрее
    
    """