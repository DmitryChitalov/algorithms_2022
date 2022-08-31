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


test_list = [randint(0, 100) for _ in range(100)]
test_deque = deque(test_list)


# 1
def list_append(list_in: list):
    for i in range(100):
        list_in.append(12)


def deque_append(deque_in: deque):
    for i in range(100):
        deque_in.append(12)


def pop_list(list_in: list):
    for i in range(100):
        list_in.pop()


def pop_deque(deque_in: deque):
    for i in range(100):
        deque_in.pop()


def extend_list(list_in: list, add_list: list):
    for i in range(100):
        list_in.extend(add_list)


def extend_deque(deque_in: deque, add_list: list):
    for i in range(100):
        deque_in.extend(add_list)


print('1) сравнить операции append, pop, extend')
print('Метод append(), list:', timeit("list_append(test_list)", globals=globals(), number=200))
print('Метод append(), deque:', timeit("deque_append(test_deque)", globals=globals(), number=200))
print('Метод pop(), list:', timeit("pop_list(test_list)", globals=globals(), number=200))
print('Метод pop(), deque:', timeit("pop_deque(test_deque)", globals=globals(), number=200))
print('Метод extend(), list:', timeit("extend_list(test_list, [1, 2, 3, 4, 5])", globals=globals(), number=200))
print('Метод extend(), deque:', timeit("extend_deque(test_deque, [1, 2, 3, 4, 5])", globals=globals(), number=200))

# Выполнение операций append и pop и extend с deque и list занимает приблизительно равное время.


# 2
def list_extendleft(list_in: list, item: list):
    list_in.reverse()
    list_in.extend(reversed(item))
    list_in.reverse()


print('\n', '2) сравнить операции appendleft, popleft, extendleft')
print('Метод insert(0, val), list:', timeit("test_list.insert(0, 12)", globals=globals(), number=200))
print('Метод appendleft(), deque:', timeit("test_deque.appendleft(12)", globals=globals(), number=200))
print('Метод pop(0), list:', timeit("test_list.pop(0)", globals=globals(), number=200))
print('Метод popleft(), deque:', timeit("test_deque.popleft()", globals=globals(), number=200))
print('Функция list_extendleft(), list:', timeit("list_extendleft(test_list, [1, 2, 3, 4, 5])",
                                                 globals=globals(), number=200))
print('Метод extendleft(), deque:', timeit("test_deque.extendleft([1, 2, 3, 4, 5])", globals=globals(), number=200))

# Операции appendleft, popleft, extendleft для deque выполняются быстрее


# 3
def get_list(list_in: list):
    for i in range(2000):
        list_in[i] = i


def get_deque(deque_in: deque):
    for i in range(2000):
        deque_in[i] = i


print('\n', '3) сравнить операции получения элемента списка и дека')
print('Получение элемента по индексу, list:', timeit("get_list(test_list)", globals=globals(), number=200))
print('Получение элемента по индексу, deque:', timeit("get_deque(test_deque)", globals=globals(), number=200))

# Операция получения элемента списка выполняется быстрее
