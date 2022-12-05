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

lst = []
deq = deque()

# list for extend
ext = list([x for x in range(50)])


# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстре
# lst
# append
def append_lst():
    for el in range(1000):
        lst.append(el)


# pop
def pop_lst():
    for el in range(900):
        lst.pop()


# extend
def ext_lst():
    lst.extend(ext)


# deque
# append
def append_deq():
    for el in range(1000):
        deq.append(el)


# pop
def pop_deq():
    for el in range(900):
        deq.pop()


# extend
def ext_deq():
    deq.extend(ext)


append_lst()
append_deq()
print('List')
print('Append\n',
      timeit(
          "append_lst()",
          setup='from __main__ import append_lst',
          number=10000),
      '\npop_lst\n',
      timeit(
          "pop_lst()",
          setup='from __main__ import pop_lst',
          number=10000),
      '\next_lst\n',
      timeit(
          "ext_lst()",
          setup='from __main__ import ext_lst',
          number=10000))

print('\nDeque\n')
print('Append\n',
      timeit(
          "append_deq()",
          setup='from __main__ import append_deq',
          number=10000),
      '\npop_deq\n',
      timeit(
          "pop_deq()",
          setup='from __main__ import pop_deq',
          number=10000),
      '\next_deq\n',
      timeit(
          "ext_deq()",
          setup='from __main__ import ext_deq',
          number=10000))

"""
Аналитика

дэк работает чуть быстрее со всеми операциями кроме extend он у списка занимает меньше времени
"""


# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее
# Lst
def lst_appendleft():
    for el in range(10):
        lst.insert(0, el)


def lst_popleft():
    for el in range(10):
        elem = lst[0]
        lst.remove(elem)


def lst_extendleft():
    lst.reverse()
    ext.reverse()
    lst.extend(ext)
    lst.reverse()


# deq
def deq_appendleft():
    for el in range(10):
        deq.appendleft(el)


def deq_popleft():
    for el in range(10):
        deq.popleft()


def deq_extendleft():
    deq.extendleft(ext)


print('List')
print('lst_appendleft\n',
      timeit(
          "lst_appendleft()",
          setup='from __main__ import lst_appendleft',
          number=10000),
      '\nlst_popleft\n',
      timeit(
          "lst_popleft()",
          setup='from __main__ import lst_popleft',
          number=10000),
      '\nlst_extendleft\n',
      timeit(
          "lst_extendleft()",
          setup='from __main__ import lst_extendleft',
          number=10000))

print('\nDeque\n')
print('deq_appendleft\n',
      timeit(
          "deq_appendleft()",
          setup='from __main__ import deq_appendleft',
          number=10000),
      '\ndeq_popleft\n',
      timeit(
          "deq_popleft()",
          setup='from __main__ import deq_popleft',
          number=10000),
      '\ndeq_extendleft\n',
      timeit(
          "deq_extendleft()",
          setup='from __main__ import deq_extendleft',
          number=10000))

"""
Расширение в левую строну у дека во много раз быстрее чем у списка мне даже пришлось сменить счет элементов 
так как скрипт выполнялся довольно долго 
"""


# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

def get_lst():
    for i in range(len(lst)):
        elem = lst[i]


def get_dec():
    for i in range(len(deq)):
        elem = deq[i]


print('get_lst\n',
      timeit(
          "get_lst()",
          setup='from __main__ import get_lst',
          number=10000))

print('get_dec\n',
      timeit(
          "get_dec()",
          setup='from __main__ import get_dec',
          number=10000))


"""
Получение элемента по индексу у списка немного быстрее
"""