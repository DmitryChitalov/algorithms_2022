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
from random import randint
from timeit import timeit

my_list = [randint(0, 200) for _ in range(200)]
my_deque = deque(my_list)


# сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее

def list_append(list_in: list):
    for i in range(200):
        list_in.append(50)


def deque_append(deque_in: deque):
    for i in range(200):
        deque_in.append(50)


def pop_list(list_in: list):
    for i in range(200):
        list_in.pop()


def pop_deque(deque_in: deque):
    for i in range(200):
        deque_in.pop()


def extend_list(list_in: list, add_list: list):
    for i in range(200):
        list_in.extend(add_list)


def extend_deque(deque_in: deque, add_list: list):
    for i in range(200):
        deque_in.extend(add_list)


print('append list:', round(timeit("list_append(my_list)", globals=globals(), number=1000), 3))
print('append deque:', round(timeit("deque_append(my_deque)", globals=globals(), number=1000), 3))
print('pop list:', round(timeit("pop_list(my_list)", globals=globals(), number=1000), 3))
print('pop deque:', round(timeit("pop_deque(my_deque)", globals=globals(), number=1000), 3))
print('extend list:', round(timeit("extend_list(my_list, [1, 2, 3, 4, 5])", globals=globals(), number=1000), 3))
print('extend deque:', round(timeit("extend_deque(my_deque, [1, 2, 3, 4, 5])", globals=globals(), number=1000), 3))

# Выполнение операций append и pop и extend с deque  немного быстрее, чем с list.
# Иногда результаты по времени примерно равны.


# сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка и сделать выводы что и где быстрее
def list_extendleft(list_in: list, item: list):
    list_in.reverse()
    list_in.extend(reversed(item))
    list_in.reverse()

print('\n''insert list:', round(timeit("my_list.insert(0, 50)", globals=globals(), number=200), 3))
print('appendleft deque:', round(timeit("my_deque.appendleft(50)", globals=globals(), number=200), 6))
print('pop list:', round(timeit("my_list.pop(0)", globals=globals(), number=200), 3))
print('popleft deque:', round(timeit("my_deque.popleft()", globals=globals(), number=200), 6))
print('list_extendleft list:', round(timeit("list_extendleft(my_list, [1, 2, 3, 4, 5])",
                                            globals=globals(), number=200), 3))
print('extendleft deque:', round(timeit("my_deque.extendleft([1, 2, 3, 4, 5])", globals=globals(), number=200), 6))
# Выполнение appendleft, popleft, extendleft с deque выполняются быстрее, чем с list


# cравнить de, и сделать выводы что и где быстрее

def get_my_list(list_in: list):
    for i in range(2000):
        list_in[i] = i


def get_my_deque(deque_in: deque):
    for i in range(2000):
        deque_in[i] = i


print('\n''элемент list:', round(timeit("get_my_list(my_list)", globals=globals(), number=200), 3))
print('элемент deque:', round(timeit("get_my_deque(my_deque)", globals=globals(), number=200), 3))
# Операция получения элемента deque выполняется немного быстрее





