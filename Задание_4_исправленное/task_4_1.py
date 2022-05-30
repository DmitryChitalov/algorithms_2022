"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from random import randrange

#array = [1, 3, 1, 3, 4, 5, 1]
#array = [1, 3, 1, 3, 4, 5, 1] * 5
array = []
for n in range(50):
    array.append(randrange(10))

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
    arr = array.copy()
    cnt_max = 1
    value_max = arr[-1]
    while len(arr) > 1:
        p = len(arr)-1
        value = arr[p]
        del arr[p]
        cnt = 1
        while p > 0:
            p -= 1
            if arr[p] == value:
                cnt += 1
                del arr[p]
        if cnt > cnt_max:
            cnt_max = cnt
            value_max = value
    return f'Чаще всего встречается число {value_max}, ' \
           f'оно появилось в массиве {cnt_max} раз(а)'

def func_4():
    freq_item = sorted([[item, array.count(item)] for item in set(array)], key=lambda x: x[1])[-1]
    return f'Чаще всего встречается число {freq_item[0]}, ' \
           f'оно появилось в массиве {freq_item[1]} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f'func_1: время = {timeit("func_1()", globals=globals())}')
print(f'func_2: время = {timeit("func_2()", globals=globals())}')
print(f'func_3: время = {timeit("func_3()", globals=globals())}')
print(f'func_4: время = {timeit("func_3()", globals=globals())}')

'''
На коротком исходном массиве длительность, в порядке возрастания: func_1, func_2, func_3 и func_4
На увеличенном массиве, полученном умножением исходного на 5: func_3 ~ func_4, func_1, func_2
Превосходство func_3 и func_4 возрастает с увеличением коэффициента <число элементов> / <число различных элементов>.
Дополнительно оно возрастает при расположении самых частых в конце списка
и снижается, при их расположении в начале.
'''