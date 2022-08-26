"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

"""
При заданном массиве:
func_1: 0.009387132999108871
func_2: 0.015834796999115497
func_3: 0.012004563999653328
func_4: 0.009891459998470964
Функция func_2 работает медленно, т.к. делает очень много дел:
    перебирает элементы списка, 
    считает каждый элемент, 
    закидывает рассчитанные числа в новый список,
    перебирает весь новый список и находит максимум.
Так что func_1 выигрывает
челлендж придумать медленный вариант: func_3 
    перебирает список, набирает словарь, потом перебирает словарь и ищет максимум
func_4 пользуемся поиском максимума с сортировкой по ключу, работает шустро со встроенными методами
Казалось бы, задача решена, наиболее быстрый метод найден
Но если мы набьём массив большим количеством элементов, где будет достаточно много повторений,
то func_3 со словарём оставляет всех далеко позади, а все остальные методы работают примерно одинаково по времени,
ведь остальные методы перебирают весь список по два раза
func_1: 19.899675740998646
func_2: 19.974268167003174
func_3: 0.42210044899911736
func_4: 19.77736821399958

"""
from timeit import timeit
from random import randint

array = [1, 3, 1, 3, 4, 5, 1]
big_array = [randint(0, 100) for i in range(500)]


def func_1(lst):
    m = 0
    num = 0
    for i in lst:
        count = lst.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(lst):
    new_array = []
    for el in lst:
        count2 = lst.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = lst[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(lst):
    dict_nums = {}
    for x in lst:
        dict_nums[x] = dict_nums.get(x, 0) + 1
    return max(dict_nums.items(), key=lambda x: x[1])


# всего одна строчка
def func_4(lst):
    search = max(lst, key=lst.count)
    return f'Чаще всего встречается число {search}, ' \
           f'оно появилось в массиве {array.count(search)} раз(а)'


print('func_1: ', end='')
print(timeit('func_1(array)', globals=globals(), number=10000))
print('func_2: ', end='')
print(timeit('func_2(array)', globals=globals(), number=10000))
print('func_3: ', end='')
print(timeit('func_3(array)', globals=globals(), number=10000))
print('func_4: ', end='')
print(timeit('func_4(array)', globals=globals(), number=10000))
print('func_1: ', end='')
print(timeit('func_1(big_array)', globals=globals(), number=10000))
print('func_2: ', end='')
print(timeit('func_2(big_array)', globals=globals(), number=10000))
print('func_3: ', end='')
print(timeit('func_3(big_array)', globals=globals(), number=10000))
print('func_4: ', end='')
print(timeit('func_4(big_array)', globals=globals(), number=10000))
