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


def append_list():
    my_list = []
    for i in range(1, 100):
        my_list.append(i)
    return my_list


my_list = append_list()


def append_deque():
    my_list = deque()
    for i in range(1, 100):
        my_list.append(i)
    return my_list


my_deque = append_deque()


def pop_list():
    for i in my_list:
        my_list.pop()


def pop_deque():
    for i in range(len(my_deque)):
        my_deque.pop()


def extend_list():
    my_list_1 = []
    my_list_1.extend(my_list)


def extend_deque():
    my_deque_1 = deque()
    my_deque_1.extend(my_deque)


print('append_list()', timeit("append_list()", globals=globals()))
print('append_deque()', timeit("append_deque()", globals=globals()))
print('pop_list()', timeit("pop_list()", globals=globals()))
print('pop_deque()', timeit("pop_deque()", globals=globals()))
my_deque = append_deque()
my_list = append_list()
print('extend_list()', timeit("extend_list()", globals=globals()))
print('extend_deque()', timeit("extend_deque()", globals=globals()))
print('####################################')


## Операции append, pop, extend элементов списка и дека по времени примерно равны по скорости.
################################  2  #######################


def appendleft_list():
    my_list = []
    for i in range(1, 100):
        my_list.insert(0, i)
    return my_list


my_list = appendleft_list()


def appendleft_deque():
    my_list = deque()
    for i in range(1, 100):
        my_list.appendleft(i)
    return my_list


my_deque = appendleft_deque()


def popleft_list():
    for i in my_list:
        my_list.pop()


def popleft_deque():
    for i in range(len(my_list)):
        my_list.popleft()


def extendleft_list():
    my_list_1 = []
    my_list_1.extend(my_list)


def extendleft_deque():
    my_deque_1 = deque()
    my_deque_1.extendleft(my_deque)


print('appendleft_list ', timeit("appendleft_list()", globals=globals()))
print('appendleft_deque() ', timeit("appendleft_deque()", globals=globals()))

print('popleft_list() ', timeit("popleft_list()", globals=globals()))
print('popleft_deque() ', timeit("popleft_deque()", globals=globals()))
my_list = appendleft_list()
my_deque = appendleft_deque()
print('extendleft_list() ', timeit("extendleft_list()", globals=globals()))
print('extendleft_deque() ', timeit("extendleft_deque()", globals=globals()))
print('####################################')
### Операции добавления, удаления и замены элементов дека быстрее, чем у списка.
################################  3  #######################


my_list = appendleft_list()
my_deque = appendleft_deque()


def get_list():
    for i in range(30):
        my_list[i] = i
    return list


def get_deque():
    for i in range(30):
        my_deque[i] = i
    return my_deque


print('get_list', timeit('get_list()', globals=globals()))
print('get_deque', timeit('get_deque()', globals=globals()))

"""
Операции получения элемента из списка быстрее, так как элемент в списке по индексу, а в деке перебором.
"""