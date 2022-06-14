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


#                                               1
def list_append():
    for i in range(1000):
        lst_test.append(i)
    return lst_test


def list_pop():
    for i in range(1000):
        lst_test.pop()
    return lst_test


def list_extend():
    lst_test.extend(lst_test)
    return lst_test


def deque_append():
    for i in range(1000):
        deq_test.append(i)
    return deq_test


def deque_pop():
    for i in range(1000):
        deq_test.pop()
    return deq_test


def deque_extend():
    deq_test.extend(deq_test)
    return deq_test


deq_test = deque()
lst_test = []

print(timeit("list_append()", globals=globals(), number=10000))
print(timeit("deque_append()", globals=globals(), number=10000))
print(timeit("list_pop()", globals=globals(), number=10000))
print(timeit("deque_pop()", globals=globals(), number=10000))
print(timeit("list_extend()", globals=globals(), number=10000))
print(timeit("deque_extend()", globals=globals(), number=10000))
print('_' * 100)


# разница в скорости выполнения незначительна

def list_append_left():
    for i in range(1000):
        lst_test_sec.insert(0, i)
    return lst_test_sec


def list_pop_left():
    for i in range(1000):
        del lst_test_sec[0]
    return lst_test_sec


def list_extend_left():
    for i in range(1000):
        lst_test_sec.insert(0, lst_test_sec)


def deque_append_left():
    for i in range(1000):
        deq_test_sec.appendleft(i)
    return deq_test_sec


def deque_pop_left():
    for i in range(1000):
        deq_test_sec.popleft()
    return deq_test_sec


def deque_extend_left():
    for i in range(1000):
        deq_test_sec.extendleft(deq_test_sec)
    return deq_test_sec


deq_test_sec = deque()
lst_test_sec = []

print(timeit("list_append_left()", globals=globals(), number=100))
print(timeit("deque_append_left()", globals=globals(), number=100))
print(timeit("list_pop_left()", globals=globals(), number=100))
print(timeit("deque_pop_left()", globals=globals(), number=100))
print(timeit("list_extend_left()", globals=globals(), number=100))
print(timeit("deque_extend_left()", globals=globals(), number=100))
print('_' * 100)

# deque быстрее из-за константной сложности, в то время как у списка линейная
lst_test_third = []
deq_test_third = deque()


def lst_append():
    for i in range(1000):
        lst_test_third.append(i)
    return lst_test_third


def deq_append():
    for i in range(1000):
        deq_test_third.append(i)
    return deq_test_third


lst_append()
deq_append()


def list_get():
    for i in range(1000):
        lst_test_third[i] = i


def deque_get():
    for i in range(1000):
        deq_test_third[i] = i


print(timeit("list_get()", globals=globals(), number=100000))
print(timeit("deque_get()", globals=globals(), number=100000))
#  получение элемента быстрее у списка
