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



lst = []
deq = deque()

def lst_append(n, fl):

    for j in range(n):
        if fl ==0:
            lst.append(j)
        else:
            lst.insert(0,j)
    return lst
def deq_append(n, fl):

    for j in range(n):
        if fl == 0:
            deq.append(j)
        else:
            deq.appendleft(j)
    return deq

def lst_pop(n, fl):

    for j in range(n):
        if fl == 0:
            lst.pop()
        else:
            lst.pop(0)

def deq_pop(n, fl):
    for j in range(n):
        if fl == 0:
            deq.pop()
        else:
            deq.popleft()

def lst_get(n):

    for j in range(n):
        i = lst[j]

def deq_get(n):

    for j in range(n):
        i = deq[j]

print('сравнить append, pop, extend списка и дека и сделать выводы что и где быстрее')
print(lst_append.__name__, timeit.timeit('lst_append(100, 0)', globals=globals(), number=10000))
print(deq_append.__name__, timeit.timeit('deq_append(100, 0)', globals=globals(), number=10000))
print(lst_pop.__name__, timeit.timeit('lst_pop(100, 0)', globals=globals(), number=10000))
print(deq_pop.__name__, timeit.timeit('deq_pop(100, 0)', globals=globals(), number=10000))
print('lst_extend', timeit.timeit('lst.extend([j for j in range(100)])', globals=globals(), number=10000))
print('deq_extend', timeit.timeit('deq.extend([j for j in range(100)])', globals=globals(), number=10000))
'''
list и deque приблизительно все одинаково. list потому, что идет стандартное удаление, добавление, а deque за счет 
оптимизированного кода 
'''
print('сравнить appendleft, popleft, extendleft дека и соответствующих им операций списка')
print(lst_append.__name__, timeit.timeit('lst_append(100, 1)', globals=globals(), number=10))
print(deq_append.__name__, timeit.timeit('deq_append(100, 1)', globals=globals(), number=10))
print(lst_pop.__name__, timeit.timeit('lst_pop(100, 1)', globals=globals(), number=10))
print(deq_pop.__name__, timeit.timeit('deq_pop(100, 1)', globals=globals(), number=10))
print('lst_extend', timeit.timeit('lst.extend([j for j in range(100)])', globals=globals(), number=10))
print('deq_extend', timeit.timeit('deq.extendleft([j for j in range(100)])', globals=globals(), number=10))
'''
добавление в list по индексу проигрывает значительно, каждый раз требуется переделывать массив.
pop - чтение по индексу из list быстре, extend - одинаков. 
'''

print('сравнить операции получения элемента списка и дека')
print(lst_get.__name__, timeit.timeit('lst_get(100)', globals=globals(), number=100))
print(deq_get.__name__, timeit.timeit('deq_get(100)', globals=globals(), number=100))
'''
получение значения лист быстрее в 2 раза
'''