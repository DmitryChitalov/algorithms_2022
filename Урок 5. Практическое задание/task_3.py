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
import timeit

nums = 2000
my_list = []
my_deque = deque()


def list_append():
    for i in range(nums):
        my_list.append(i)
    return my_list


list_append()


def deque_append():
    for i in range(nums):
        my_deque.append(i)
    return my_deque


deque_append()


def list_pop():
    for i in range(nums):
        my_list.pop()
    return my_list


list_pop()


def deque_pop():
    for i in range(nums):
        my_deque.pop()
    return my_deque


deque_pop()


def list_extend():
    for i in range(nums):
        my_list.extend(range(1, 6))
    return my_list


list_extend()


def deque_extend():
    for i in range(nums):
        my_deque.extend(range(1, 6))
    return my_deque


deque_extend()

print(list_append.__name__, timeit.timeit('list_append()', globals=globals(), number=1000))
print(deque_append.__name__, timeit.timeit('deque_append()', globals=globals(), number=1000))
print(list_pop.__name__, timeit.timeit('list_pop()', globals=globals(), number=1000))
print(deque_pop.__name__, timeit.timeit('deque_pop()', globals=globals(), number=1000))
print(list_extend.__name__, timeit.timeit('list_extend()', globals=globals(), number=1000))
print(deque_extend.__name__, timeit.timeit('deque_extend()', globals=globals(), number=1000))

'''list_append 0.43569786800071597
deque_append 0.24264599103480577
list_pop 0.2082758799660951
deque_pop 0.21727060014382005
list_extend 1.5429263319820166
deque_extend 0.8700296960305423'''

my_list2 = []
my_deque2 = deque()


def list_insert():
    for i in range(nums):
        my_list2.insert(0, i)
    return my_list2


list_insert()


def deque_appendleft():
    for i in range(nums):
        my_deque2.appendleft(i)
    return my_deque2


deque_appendleft()


def list_popleft():
    for i in range(nums):
        my_list2.pop(0)
    return my_list2


list_popleft()


def deque_popleft():
    for i in range(nums):
        my_deque2.popleft()
    return my_deque2


deque_popleft()


def list_extendleft():
    for i in range(nums):
        my_list2.insert(0, range(1, 6))
    return my_deque2


list_extendleft()


def deque_extendleft():
    for i in range(nums):
        my_deque2.extendleft(range(1, 6))
    return my_deque2


deque_extendleft()

print(list_insert.__name__, timeit.timeit('list_insert()', globals=globals(), number=10))
print(deque_appendleft.__name__, timeit.timeit('deque_appendleft()', globals=globals(), number=10))
print(list_popleft.__name__, timeit.timeit('list_popleft()', globals=globals(), number=10))
print(deque_popleft.__name__, timeit.timeit('deque_popleft()', globals=globals(), number=10))
print(list_extendleft.__name__, timeit.timeit('list_extendleft()', globals=globals(), number=10))
print(deque_extendleft.__name__, timeit.timeit('deque_extendleft()', globals=globals(), number=10))
'''
list_insert 0.18331923009827733
deque_appendleft 0.0018961362075060606
list_popleft 0.10272084106691182
deque_popleft 0.0019028079695999622
list_extendleft 0.19258438516408205
deque_extendleft 0.008560584159567952'''


def list_take():
    for i in range(nums):
        my_list2[i] = i
    return my_list2


list_take()


def deque_take():
    for i in range(nums):
        my_deque2[i] = i
    return my_deque2


deque_take()

print(list_take.__name__, timeit.timeit('list_take()', globals=globals(), number=10))
print(deque_take.__name__, timeit.timeit('deque_take()', globals=globals(), number=10))

'''list_take 0.001547698862850666
deque_take 0.0023133379872888327'''
'''
Во всех операциях, кроме получения значения из списка, функции с использованием deque быстрее.
Это объясняется тем, что  deque двусвязанный список, а для поиска по индексу deque приходится выполнять итерацию,
поэтому получения элемента из списка с использованием функций с deque занимает больше времени.
'''