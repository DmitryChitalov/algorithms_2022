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


from timeit import timeit
from collections import deque

tlist = []
tdeque = deque()
n = 1000

# сравнить операции append, pop, extend списка и дека

def list_app(list):
    for i in range(n):
        list.append(i)


def deq_app(dq_obj):
    for i in range(n):
        dq_obj.append(i)


def list_pop(list):
    for i in range(n):
        list.pop()


def deq_pop(dq_obj):
    for i in range(n):
        dq_obj.pop()


def list_ext(list):
    for i in range(n):
        list.extend([1, 2, 3, 4, 5])


def deq_ext(dq_obj):
    for i in range(n):
        dq_obj.extend([1, 2, 3, 4, 5])


print('1) сравнить операции append, pop, extend списка и дека')
print('list.append : ', timeit('list_app(tlist)', globals=globals(), number=100))
print('deque.append : ', timeit('deq_app(tdeque)', globals=globals(), number=100))
print('list.pop : ', timeit('list_pop(tlist)', globals=globals(), number=100))
print('deque.pop : ', timeit('deq_pop(tdeque)', globals=globals(), number=100))
print('list.extend : ', timeit('list_ext(tlist)', globals=globals(), number=100))
print('deque.extend : ', timeit('deq_ext(tdeque)', globals=globals(), number=100))

# сравнить операции appendleft, popleft, extendleft дека и соответствующих
# им операций списка

def list_appleft(list):
    for i in range(100):
        list.insert(0, i)


def deq_appleft(dq_obj):
    for i in range(n):
        dq_obj.appendleft(i)


def list_popleft(list):
    for i in range(100):
        list.pop(0)


def deq_popleft(dq_obj):
    for i in range(n):
        dq_obj.popleft()


def list_extendleft(list):
    for i in range(100):
        list.extend([1, 2, 3, 4, 5])
        list.sort()


def deq_extendleft(dq_obj):
    for i in range(n):
        dq_obj.extendleft([1, 2, 3, 4, 5])


print('2) сравнить операции appendleft, popleft, extendleft дека '
      'и соответствующих им операций списка')
print('list.appendleft : ', timeit('list_appleft(tlist)', globals=globals(), number=100))
print('deque.appendleft : ', timeit('deq_appleft(tdeque)', globals=globals(), number=100))
print('list.popleft : ', timeit('list_popleft(tlist)', globals=globals(), number=100))
print('deque.popleft : ', timeit('deq_popleft(tdeque)', globals=globals(), number=100))
print('list.extendleft : ', timeit('list_extendleft(tlist)', globals=globals(), number=100))
print('deque.extendleft : ', timeit('deq_extendleft(tdeque)', globals=globals(), number=100))

# сравнить операции получения элемента списка и дека

def list_get(list):
    for i in range(n):
        tmp = list[i]


def deq_get(dq_obj):
    for i in range(n):
        tmp = list[dq_obj]

print('3) сравнить операции получения элемента списка и дека')
print('list.get : ', timeit('list_get(tlist)', globals=globals(), number=100))
print('deque.get : ', timeit('deq_get(tdeque)', globals=globals(), number=100))

"""
1) сравнить операции append, pop, extend списка и дека
list.append :  0.00472260000242386
deque.append :  0.003957500011892989
list.pop :  0.004036199999973178
deque.pop :  0.004172300003119744
list.extend :  0.013945400001830421
deque.extend :  0.011563599997316487
2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
list.appendleft :  1.5743289999954868
deque.appendleft :  0.003958800007239915
list.popleft :  3.03037160000531
deque.popleft :  0.0038653999945381656
list.extendleft :  20.52312389999861
deque.extendleft :  0.011173000006237999
3) сравнить операции получения элемента списка и дека
list.get :  0.002459600000292994
deque.get :  0.010606099996948615

1) операции append, pop, extend показвают схожие цифры что в списе, что в деке
2) операции appendleft, popleft, extendleft гораздо быстрее работают в деке
3) операции получения элемента быстрее работают в списке
"""
