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

lst = [i for i in range(10000)]
deq = deque(lst)
# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее
# lst.append('i')
# deq.append('q')
# lst.pop()
# deq.pop()
# lst.extend(['z', 'g', 'u'])
# deq.extend(['y', 'm', 'j'])


def appnd_lst():
    for i in range(1000):
        lst.append(i)


def deq_appnd():
    for i in range(1000):
        deq.append(i)


def pop_lst():
    for i in range(1000):
        lst.pop()


def pop_deq():
    for i in range(1000):
        deq.pop()


def lst_extend():
    ext = [i for i in range(1000)]
    lst.extend(ext)


def deq_extend():
    ext = [i for i in range(1000)]
    deq.extend(ext)


print(timeit("appnd_lst()", globals=globals(), number=1000))
print(timeit("deq_appnd()", globals=globals(), number=1000))
print(timeit("pop_lst()", globals=globals(), number=1000))
print(timeit("pop_deq()", globals=globals(), number=1000))
print(timeit("lst_extend()", globals=globals(), number=1000))
print(timeit("deq_extend()", globals=globals(), number=1000))
"""
0.07474700012244284
0.0578724998049438
0.07589720003306866
0.05802160012535751
0.058881100034341216
0.03922059992328286
"""
# при применении классических операций pop, append, extend дек выигрывает в скорости, но не сильно

# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


def lst_left():
    for i in range(1):
        lst.insert(0, i)


def deq_left():
    for i in range(1):
        deq.appendleft(i)


def lst_pop_left():
    for i in range(1):
        lst.pop(0)


def deq_pop_left():
    for i in range(1):
        deq.popleft()


def ext_left_lst():
    ext = [i for i in range(1)]
    lst.insert(0, ext)


def ext_left_deq():
    ext = [i for i in range(1)]
    deq.extendleft(ext)


print(timeit("lst_left()", globals=globals(), number=1000))
print(timeit("deq_left()", globals=globals(), number=1000))
print(timeit("lst_pop_left()", globals=globals(), number=1000))
print(timeit("deq_pop_left()", globals=globals(), number=1000))
print(timeit("ext_left_lst()", globals=globals(), number=1000))
print(timeit("ext_left_deq()", globals=globals(), number=1000))
"""
0.9462262999732047
0.019600900122895837
1.287388099823147
0.00023370003327727318
0.5307761000003666
0.00044659990817308426
"""
# тут документайия действительно не врет, операции с деком быстрее

# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее


def get_from_lst():
    for i in range(1000):
        lst[i]


def get_from_deq():
    for i in range(1000):
        deq[i]


print(timeit("get_from_lst()", globals=globals(), number=1000))
print(timeit("get_from_deq()", globals=globals(), number=1000))
"""
0.03416930022649467
0.07008099998347461
"""
# лидирует классический список

# если вам нужно
# что-то быстро дописать или вытащить, используйте deque.
# Если вам нужен быстрый случайный доступ, используйте list -  ЭТО УТРВЕРЖДЕНИЕ ИСТИННО