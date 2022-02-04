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

lst = [x for x in range(10000)]
dqe = deque([x for x in range(10000)])

# 1) сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее
print('Сравнение операции append')


def append_list(lst):
    for x in range(1000):
        lst.append(x)
    return lst


def append_deque(dqe):
    for x in range(1000):
        dqe.append(x)
    return dqe


print(timeit('append_list(lst)', globals=globals(), number=100))  # 0.0044043
print(timeit('append_deque(dqe)', globals=globals(), number=100))  # 0.004266800000000001

print('\nСравнение операции pop')


def pop_list(lst):
    for x in range(1000):
        lst.pop()
    return lst


def pop_deque(dqe):
    for x in range(1000):
        dqe.pop()
    return dqe


print(timeit('pop_list(lst)', globals=globals(), number=100))  # 0.003933899999999997
print(timeit('pop_deque(dqe)', globals=globals(), number=100))  # 0.004016699999999998

print('\nСравнение операции extend')


def extend_list(lst):
    for x in range(1000):
        lst.extend([1, 2])
    return lst


def extend_deque(dqe):
    for x in range(1000):
        dqe.extend([1, 2])
    return dqe


print(timeit('extend_list(lst)', globals=globals(), number=100))  # 0.0.007569900000000004
print(timeit('extend_deque(dqe)', globals=globals(), number=100))  # 0.0087623

'''Операции append, pop и extend у списка и дека приблизительно одинаковые по скорости выполнения.'''

# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
print('\n\nСравнение операций insert и appendleft')


def insert_list(lst):
    for x in range(1000):
        lst.insert(0, x)
    return lst


def appendleft_deque(dqe):
    for x in range(1000):
        dqe.appendleft(x)
    return dqe


print(timeit('insert_list(lst)', globals=globals(), number=100))  # 8.859329
print(timeit('appendleft_deque(dqe)', globals=globals(), number=100))  # 0.004177000000000319

print('\nСравние операций pop(index) и popleft')


def popindex_list(lst):
    for x in range(100):
        lst.pop(x)
    return lst


def popleft_deque(dqe):
    for x in range(100):
        dqe.popleft()
    return dqe


print(timeit('popindex_list(lst)', globals=globals(), number=100))  # 1.7078629000000003
print(timeit('popleft_deque(dqe)', globals=globals(), number=100))  # 0.0003364000000001255

print('\nСравнение операций insert[0] и extendleft')


def insertfirst_list(lst):
    for i in range(1000):
        lst.insert(0, [1, 2])
    return lst


def extendleft_deque(dqe):
    for i in range(1000):
        dqe.extendleft([1, 2])
    return dqe


print(timeit('insertfirst_list(lst)', globals=globals(), number=100))  # 12.099725800000002
print(timeit('extendleft_deque(dqe)', globals=globals(), number=100))  # 0.008966799999999608

'''Операции appendleft, popleft, extendleft у дека быстрее, чем соответствующие операции у списка.'''

# 3) сравнить операции получения элемента списка и дека
print('\n\nСравнение операции получения элемента списка и дека')


def list_elem(lst):
    for x in range(1000):
        lst[x] = x
    return lst


def deque_elem(dqe):
    for x in range(1000):
        dqe[x] = x
    return dqe


print(timeit('list_elem(lst)', globals=globals(), number=100))  # 0.0026532999999986373
print(timeit('deque_elem(dqe)', globals=globals(), number=100))  # 0.00373610000000113

'''Операция получения элемента списка быстрее, чем операция получения элемента дека.'''
