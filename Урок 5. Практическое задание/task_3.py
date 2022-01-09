"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

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
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from timeit import timeit


list_1 = [_ for _ in range(10 ** 4)]

dek_1 = deque([_ for _ in range(10 ** 4)])

n = 10 ** 3
# Задание 1
# Append (добавить элементы в список и очередь)

def app_list_1(list_1):
    for i in range(n):
        list_1.append(i)
    return list_1



def app_dek_1(dek_1):
    for i in range(n):
        dek_1.append(i)
    return dek_1


print(timeit('app_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('app_dek_1(dek_1.copy())', globals=globals(), number=1000))
# Операции со списками list проходят в 2 раза быстрее чем с очередями deque
# 0.0810884
# 0.15935200000000002


# Pop (извлечь элементы из списка и очереди)
def pop_list_1(list_1):
    for i in range(n):
        list_1.pop()
    return list_1


def pop_dek_1(dek_1):
    for i in range(n):
        dek_1.pop()
    return dek_1


print(timeit('pop_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('pop_dek_1(dek_1.copy())', globals=globals(), number=1000))
# Операции со списками list проходят почти в 1,5 раза быстрее чем с очередями deque
# 0.0916864
# 0.14129119999999995

# Extend (добавить элементы в конце списка и очереди)
def ext_list_1(list_1):
    for i in range(n):
        list_1.extend([5, 9, 30])
    return list_1


def ext_dek_1(dek_1):
    for i in range(n):
        dek_1.extend([5, 9, 30])
    return dek_1


print(timeit('ext_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('ext_dek_1(dek_1.copy())', globals=globals(), number=1000))
# Операции со списками list проходят почти в 2 раза быстрее чем с очередями deque
# 0.11656010000000006
# 0.20657729999999996

# Задание 2

# insert вставить влево в список со сдвигом всех элементов списка
def insert_left_list_1(list_1):
    for i in range(n):
        list_1.insert(0, i)
    return list_1


# appendleft добавить слева в очередь
def app_left_dek(dek_1):
    for i in range(n):
        dek_1.appendleft(i)
    return dek_1


print(timeit('insert_left_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('app_left_dek(dek_1.copy())', globals=globals(), number=1000))
# Операции по добавлению элементов в список list проходят очень медленно, т.к. список создается заново
# и все его элементы индексируются
#
# 6.099939099999999
# 0.11444089999999996

# pop извлечение первого элемента списка
def pop_left_list_1(list_1):
    for i in range(n):
        list_1.pop(0)
    return list_1


# popleft извлечение первого элемента списка
def pop_left_dek(dek_1):
    for i in range(n):
        dek_1.popleft()
    return dek_1


print(timeit('pop_left_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('pop_left_dek(dek_1.copy())', globals=globals(), number=1000))
# Операции по извлечению элементов из списка list проходят гораздо медленнее, т.к. список
# и все его оставшиеся элементы индексируются
1.1679203000000005
0.11754420000000021


# insert вставить в список c левой стороны список со сдвигом всех элементов списка
def ext_left_list_1(list_1):
    for i in range(n):
        list_1.insert(0, [5, 9, 30])
    return list_1


# extend
def ext_left_dek(dek_1):
    for i in range(n):
        dek_1.extendleft([5, 9, 30])
    return dek_1


print(timeit('ext_left_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('ext_left_dek(dek_1.copy())', globals=globals(), number=1000))
# Операции по добавлению списка в список проходят почти в 26 раз медленнее чем такая же операция с очередью
# 5.598703199999999
# 0.21676529999999872


# 3 получение элементов

def get_elem_list_1(list_1):
    for i in range(n):
        list_1[i] = i
    return list_1


def get_elem_dek(dek_1):
    for i in range(n):
        dek_1[i] = i
    return dek_1

print(timeit('get_elem_list_1(list_1.copy())', globals=globals(), number=1000))
print(timeit('get_elem_dek(dek_1.copy())', globals=globals(), number=1000))
# Операции со списками list проходят в 2 раза быстрее чем с очередями deque
# 0.06677550000000032
# 0.11656889999999898