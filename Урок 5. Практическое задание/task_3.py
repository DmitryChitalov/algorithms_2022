"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit

some_lst = [i for i in range(100)]
deq_obj = deque([i for i in range(100)])


# 1 сравнение append, pop, extend
def append_lst(some_lst):
    for i in range(50):
        some_lst.append(i)


def append_deq(deq_obj):
    for i in range(50):
        deq_obj.append(i)


print(timeit("append_lst(some_lst)", globals=globals(), number=1000))
print(timeit("append_deq(deq_obj)", globals=globals(), number=1000))
'''
0.00330359999999999 list
0.0022485999999999895 deque
Через append deque чуть быстрее, чем list. Это больше похоже на погрешность, 
поэтому можно сделать вывод, что операция для дека и списка выполняется примерно с одной скоростью
'''


def pop_lst(some_lst):
    for i in range(50):
        some_lst.pop()


def pop_deq(deq_obj):
    for i in range(50):
        deq_obj.pop()


print(timeit("pop_lst(some_lst)", globals=globals(), number=1000))
print(timeit("pop_deq(deq_obj)", globals=globals(), number=1000))
'''
0.002545699999999998 list
0.0019843000000000083 deque
Из deque элементы удаляются чусть быстрее. Это больше похоже на погрешность, 
поэтому можно сделать вывод, что операция для дека и списка выполняется примерно с одной скоростью
'''


def extend_lst(some_lst):
    for i in range(50):
        some_lst.extend([1, 2, 3])


def extend_deq(deq_obj):
    for i in range(50):
        deq_obj.extend([1, 2, 3])


print(timeit("extend_lst(some_lst)", globals=globals(), number=1000))
print(timeit("extend_deq(deq_obj)", globals=globals(), number=1000))
'''
0.00863520000000001 list
0.0060382999999999964 deque
Через extend deque заполняется чуть быстрее. Это больше похоже на погрешность, 
поэтому можно сделать вывод, что операция для дека и списка выполняется примерно с одной скоростью
'''

# Сравнить appendleft, popleft, extendleft дека и соответствующих им операций списка
some_lst2 = [i for i in range(100)]
deq_obj2 = deque([i for i in range(100)])


def appendleft_lst(some_lst):
    for i in range(50):
        some_lst.insert(0, i)


def appendleft_deq(deq_obj):
    for i in range(50):
        deq_obj.appendleft(i)


print(timeit("appendleft_lst(some_lst2)", globals=globals(), number=1000))
print(timeit("appendleft_deq(deq_obj2)", globals=globals(), number=1000))
'''
0.47743890000000005 list
0.002408100000000024 deque
deque заполняется слева быстрее, разница по скорости очень большая, так как используем специальную функцию для дэка
'''


def popleft_lst(some_lst):
    for i in range(50):
        some_lst.pop(0)


def popleft_deq(deq_obj):
    for i in range(50):
        deq_obj.popleft()


print(timeit("popleft_lst(some_lst2)", globals=globals(), number=1000))
print(timeit("popleft_deq(deq_obj2)", globals=globals(), number=1000))
'''
0.2413577 list
0.00193500000000002 deque
Из deque элементы слева удаляются быстрее, разница по скорости очень большая, так как используем специальную функцию для дэка
'''


def extendleft_lst(some_lst):
    for i in range(50):
        some_lst.insert(0, [1, 2, 3])


def extendleft_deq(deq_obj):
    for i in range(50):
        deq_obj.extendleft([1, 2, 3])


print(timeit("extendleft_lst(some_lst2)", globals=globals(), number=1000))
print(timeit("extendleft_deq(deq_obj2)", globals=globals(), number=1000))
'''
0.48264150000000006 list
0.0062363000000000834 deque
deque быстрее, разница по скорости очень большая, так как используем специальную функцию для дэка
'''
# сравнить операции получения элемента списка и дека


def getelem_lst(some_lst2):
    for i in range(50):
        some_lst2[i] = i


def getelem_deq(deq_obj2):
    for i in range(50):
        deq_obj[i] = i


print(timeit("getelem_lst(some_lst2)", globals=globals(), number=1000))
print(timeit("getelem_deq(deq_obj2)", globals=globals(), number=1000))
'''
0.001517100000000049 list
0.0019876000000000893 deque
Получение эдемента чуть Deque медленнее.Это больше похоже на погрешность, 
поэтому можно сделать вывод, что операция для дека и списка выполняется примерно с одной скоростью
'''