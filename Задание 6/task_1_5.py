"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""
# Урок 4, задание 4

from timeit import timeit
from random import randrange
from pympler.asizeof import asizeof
import numpy as np

# исходное решение

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

print('Размер списка:', asizeof(array))

# print(f'func_1: время = {timeit("func_1()", globals=globals())}')
# print(f'func_2: время = {timeit("func_2()", globals=globals())}')
# print(f'func_3: время = {timeit("func_3()", globals=globals())}')
# print(f'func_4: время = {timeit("func_3()", globals=globals())}')

# Оптимизация - исходный массив хранится в numpy array
arr = np.array(array)

def func_5():
    m = 0
    num = 0
    for i in arr:
        count = np.sum(arr==i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

print('--- После оптимизации')
print(func_5())
print('Размер массива:', asizeof(arr))

# Результат - уменьшился объём использованной памяти
