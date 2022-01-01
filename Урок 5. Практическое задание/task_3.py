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

def lst():
    lst = []
    for i in range(100000):
        lst.append(i)
    return lst

def deq():
    deq = []
    for i in range(100000):
        deq.append(i)
    return deq

lst = lst()
deq = deque(deq())

print('-- 1 --')

def app_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst

def app_deq(deq):
    for i in range(100):
        deq.append(i)
    return deq

# print(timeit('app_lst(lst)', globals=globals(), number=100))
# print(timeit('app_deq(deq)', globals=globals(), number=100))
'''
0.0023132999999999626
0.0018489999999999895
'''

def pop_lst(lst):
    for i in range(100):
        lst.pop()
    return lst

def pop_deq(deq):
    for i in range(100):
        deq.pop()
    return deq

# print(timeit('pop_lst(lst)', globals=globals(), number=100))
# print(timeit('pop_deq(deq)', globals=globals(), number=100))
'''
0.0014041000000000192
0.001288699999999976
'''

def ex_lst(lst):
    for i in range(100):
        lst.extend([0, 0, 0, 0])
    return lst

def ex_deq(deq):
    for i in range(100):
        deq.extend([0, 0, 0, 0])
    return deq


# print(timeit('ex_lst(lst)', globals=globals(), number=100))
# print(timeit('ex_deq(deq)', globals=globals(), number=100))
'''
0.005617900000000009
0.004812099999999986
'''

'''
Вывод: Время выполнения не много быстрее у дека, чем у списка.
'''
print('-- 2 --')

def app_le_lst(lst):
    for i in range(100):
        lst.insert(0, i)
    return lst

def app_le_deq(deq):
    for i in range(100):
        deq.appendleft(i)
    return deq


# print(timeit('app_le_lst(lst)', globals=globals(), number=100))
# print(timeit('app_le_deq(deq)', globals=globals(), number=100))
'''
3.2278199
0.001625100000000046
'''

def pop_le_lst(lst):
    for i in range(100):
        lst.pop(i)
    return lst

def pop_le_deq(deq):
    for i in range(100):
        deq.popleft()
    return deq


# print(timeit('pop_le_lst(lst)', globals=globals(), number=100))
# print(timeit('pop_le_deq(deq)', globals=globals(), number=100))
'''
10.8149912
0.0012705000000003963
'''

def ex_le_lst(lst):
    for i in range(100):
        lst.insert(0, [0, 0, 0, 0])
    return lst

def ex_le_deq(deq):
    for i in range(100):
        deq.extendleft([0, 0, 0, 0])
    return deq


# print(timeit('ex_le_lst(lst)', globals=globals(), number=100))
# print(timeit('ex_le_deq(deq)', globals=globals(), number=100))
'''
3.7474611999999983
0.007015400000000227
'''

'''
Вывод: Дек гораздо быстрее, чем список.
'''

print('-- 3 --')

def elem_lst(lst):
    for i in range(100):
        lst[i] = i
    return lst

def elem_deq(deq):
    for i in range(100):
        deq[i] = i
    return deq

# print(timeit('elem_lst(lst)', globals=globals(), number=100))
# print(timeit('elem_deq(deq)', globals=globals(), number=100))

'''
0.001001399999999819
0.004516600000002313
'''

'''
Вывод: Получение по индексу в списке быстрее чем в деке.
'''
