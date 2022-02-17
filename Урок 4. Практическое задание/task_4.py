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

# array = [1, 3, 1, 3, 4, 5, 1]
# array = [random.randint(1,100) for _ in range(1000)]
array = [i for i in range(1000)]

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
    # number = max(array, key=array.count)
    number = max([array.count(num) for num in set(array)])  #  можно ли сделать тоже самое, используя параметр key \
    # без формирования списка?
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'


print(f"func_1() {timeit('func_1()', globals=globals(), number=1000)}")
print(f"func_2() {timeit('func_2()', globals=globals(), number=1000)}")
print(f"func_3() {timeit('func_3()', globals=globals(), number=1000)}")


print(func_3())
"""
func_1() 9.588701499999999
func_2() 9.6678929
func_3() 1.086963500000003

func_3 вычисляет число повторов без повторных вычислений, поэтому выигрывает в скорости,
если в массиве есть повторы элементов. Однако, если элементы не повторяются, скорость вычисления примерно одинакова. 
Если в первых двух функциях цикл осуществлять по множеству, а не по списку, быстродействие будет примерно одинаковым.
Поэтому для подсчета числа повторов элементов, лучше использовать множества.


func_1() 11.548514599999999
func_2() 12.0105266
func_3() 12.3177576

"""