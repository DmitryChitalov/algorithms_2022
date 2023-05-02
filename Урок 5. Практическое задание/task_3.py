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


lst = list(range(100000))
deque_ = deque(list(range(100000)))
n = 10000

'''append
0.32672009999999996 list
0.23736270000000004 deque'''
print('append')

def append_list(lst):
    for i in range(n):
        lst.append(i)
    return lst


def deque_deq(deque_):
    for i in range(n):
        deque_.append(i)
    return deque_


print(timeit('append_list(lst)', globals=globals(), number=100))
print(timeit('deque_deq(deque_)', globals=globals(), number=100))

print(15*'*')
'''pop
0.3277743000000001 list
0.29661840000000006 deque'''
print('pop')

def list_pop(lst):
    for i in range(n):
        lst.pop()
    return lst


def deque_pop(deque_):
    for i in range(n):
        deque_.pop()
    return deque_


print(timeit('list_pop(lst)', globals=globals(), number=100))
print(timeit('deque_pop(deque_)', globals=globals(), number=100))

print(15*'*')
print('extend')
num = list(range(10))

def list_extend(lst, num):
    for i in range(n):
        lst.extend(num)
    return lst


'''extend
3.3131214 list
1.3108608000000004 deque'''
def deque_extend(deque_, num):
    for i in range(n):
        deque_.extend(num)
    return deque_


print(timeit('list_extend(lst, num)', globals=globals(), number=100))
print(timeit('deque_extend(deque_, num)', globals=globals(), number=100))

print('insert')

'''appendleft_list компьютер завис
   appendleft_deque 0.24'''
def appendleft_list(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst



def appendleft_deque(deque_):
    for i in range(n):
        deque_.appendleft(i)
    return deque_


#print(timeit('appendleft_list(lst)', globals=globals(), number=100))
print(timeit('appendleft_deque(deque_)', globals=globals(), number=100))
print(15*'*')
print('popleft')

'''list_popleft комп завис
   popleft_deque 0.25'''
def list_popleft(lst):
    for i in range(n):
        lst.pop(i)
    return lst



def popleft_deque(deque_):
    for i in range(n):
        deque_.popleft()
    return deque_


#print(timeit('list_popleft(lst)', globals=globals(), number=100))
print(timeit('popleft_deque(deque_)', globals=globals(), number=100))
print(15*'*')
print('leftextend')

'''extendleft_list комп завис
   extendleft_deque 0.58'''

def extendleft_list(lst):
    for i in range(n):
        lst.insert(0, num)
    return lst



def extendleft_deque(deque_):
    for i in range(n):
        deque_.extendleft(num)
    return deque_


# print(timeit('extendleft_list(lst)', globals=globals(), number=100))
print(timeit('extendleft_deque(deque_)', globals=globals(), number=100))
print(15*'*')
print('receive_element')

'''receive_element
0.20662219999999998 lst
0.7980778000000002 deque'''
def receive_elem_lst(lst):
    for i in range(n):
        lst[i] = i
    return lst


def receive_elem_deq(deque):
    for i in range(n):
        deque[i] = i
    return deque


print(timeit('receive_elem_lst(lst)', globals=globals(), number=100))
print(timeit('receive_elem_deq(deque_)', globals=globals(), number=100))








