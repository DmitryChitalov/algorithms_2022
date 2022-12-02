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

lst_test = [5, 60, 900]
deq_test = deque('307981456820')

num = 50

# Список


def insert_to_lst_left(lst_test):
    for i in range(num):
        lst_test.insert(0, i)
    return lst_test


def pop_from_lst_left(lst_test):
    for i in range(30):
        lst_test.pop(i)
    return lst_test


def extend_lst_left(lst_test):
    for i in range(30):
        lst_test.insert(0, [1, 9])
    return lst_test

# Дек


def append_to_deq_left(deq_test):
    for i in range(num):
        deq_test.appendleft(i)
    return deq_test


def pop_from_deq_left(deq_test):
    for i in range(num):
        deq_test.popleft()
    return deq_test


def extend_deq_left(deq_test):
    for i in range(num):
        deq_test.extendleft([1, 9])
    return deq_test


# Замеры времени
print(timeit("insert_to_lst_left(lst_test)", globals=globals(), number=1000))
print(timeit("append_to_deq_left(deq_test)", globals=globals(), number=1000))
print(timeit("pop_from_lst_left(lst_test)", globals=globals(), number=1000))
print(timeit("pop_from_deq_left(deq_test)", globals=globals(), number=1000))
print(timeit("extend_lst_left(lst_test)", globals=globals(), number=1000))
print(timeit("extend_deq_left(deq_test)", globals=globals(), number=1000))

"""
0.7176218000000001
0.005631200000000058
0.14863749999999998
0.006039200000000022
0.5663323000000001
0.014118399999999864

Все операции по изменению дека выполняются быстрее
"""