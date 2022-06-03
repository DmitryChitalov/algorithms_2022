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

Это файл для второго скрипта
"""
# Урок 1, задание 2

from pympler.asizeof import asizeof
from memory_profiler import memory_usage

def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res
    return wrapper

# исходное решение
@memory
def min_2(lst): # O(n)
    res = lst[0] # O(1)
    for item in lst: # O(n)
        if item < res: # O(1)
            res = item # O(1) 
    return res # O(1)

lst = [10200, 130, -852, 566, -136]
print('Размер list: ', asizeof(lst))
print(min_2(lst))

'''
Размер list:  128
Выполнение заняло 0.00390625 Mib
-852
'''

# Оптимизация - исходный массив задан в кортеже, перебор массива в генераторе
@memory
def min_opt(lst, res):
    for item in lst:
        if item < res:
            res = item
        yield res

lst_tuple = (10200, 130, -852, 566, -136)
print('Размер tuple:', asizeof(lst_tuple))
for res in min_opt(lst_tuple, 100000):
    pass
print(res)

'''
Размер tuple: 120
Выполнение заняло 0.00390625 Mib
-852
'''

# Результат - уменьшился объём использованной памяти
