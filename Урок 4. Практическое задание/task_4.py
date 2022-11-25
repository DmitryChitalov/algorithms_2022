"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]

import collections
def func_3():
    num = dict(collections.Counter(array))
    return f'Чаще всего встречается число {list(num.keys())[0]}, ' \
           f'оно появилось в массиве {list(num.values())[0]} раз(а)'





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
    nums = {}
    n, nm = None, 0
    for i in array:
        count = array.count(i)
        nums[i] = t = nums.get(i, 0) + 1
        if t > nm:
            n, nm = i, t
        return f'Чаще всего встречается число {n}, ' \
        f'оно появилось в массиве {count} раз(а)'



print(func_1())
print(func_2())
print(func_3())

print(f'1 - {timeit("func_1()", "from __main__ import func_1", number=100000)}')
print(f'2 - {timeit("func_2()", "from __main__ import func_2", number=100000)}')
print(f'3 - {timeit("func_3()", "from __main__ import func_3", number=100000)}')

"""
Первая функция быстрее, потому, что во второй функции создается еще один список. Временная сложность поиска в списке в среднем составляет O (n). 
В третьем варианте использовал словарь, средняя временная сложность поиска ключа словаря составляет O (1),
поскольку они реализованы в виде хэш-таблиц. 
"""