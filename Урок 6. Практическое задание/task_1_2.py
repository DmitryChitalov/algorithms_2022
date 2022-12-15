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

Это файл для первого скрипта
"""
from collections import defaultdict, namedtuple
import pickle
from memory_profiler import profile
from pympler import asizeof
from memory_profiler import memory_usage
from time import time


'''Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

0.0859375 рекурсия
0.0 обычная функция
рекурсия сохраняет стэк вызовов
'''



def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper



@decor
def number(n, even=0, odd=0):
    if n == 0:
        return even, odd
    else:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
    return number(n, even, odd)





@decor
def number_2(n):
    even = 0
    odd = 0
    while n != 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd



numb = 59898949223452345234523452366565645959292929592954879298
print(number(numb))
print(number_2(numb))



'''
сравнение функций выполняющих операцию по колличеству вхождений одинаковых чисел/элементов в массив
функция func_1 потребляет 0.0 mib
функция func_2 потребляет 0.03515625 mib потребляет больше всех т.к. создаётся список
функция func_3 потребляет 0.0 mib
функция func_4 потребляет 0.0 mib
'''

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


#@profile
@decor
def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'



#@profile
@decor
def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return  f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'



#@profile
@decor
def func_3(array):
    dict = {}
    count, itm = 0, ''
    for i in array:
        dict[i] = dict.get(i, 0) + 1
        if dict[i] >= count:
            count, itm = dict[i], i
    return f'Чаще всего встречается число {itm}, ' \
           f'оно появилось в массиве {count} раз(а)'



#@profile
@decor
def func_4(array):
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


array = [randint(1, 100) for i in range(5000)]
print(f'функция func_1 потребляет {func_1(array)} mib')
print(f'функция func_2 потребляет {func_2(array)} mib')
print(f'функция func_3 потребляет {func_3(array)} mib')
print(f'функция func_4 потребляет {func_4(array)} mib')
