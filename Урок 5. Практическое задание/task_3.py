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

test_list = []
test_deque = deque()

# append, pop, extend


def fill_list(n):
    for i in range(n):
        test_list.append(i)


def fill_deque(n):
    for i in range(n):
        test_deque.append(i)


def pop_list(n):
    for i in range(n):
        test_list.pop()


def pop_deque(n):
    for i in range(n):
        test_deque.pop()


def extend_list(n):
    for i in range(n):
        test_list.extend([i, i - 1, i - 2])


def extend_deque(n):
    for i in range(n):
        test_deque.extend([i, i - 1, i - 2])


print(timeit('fill_list(100)', globals=globals(), number=100000))
print(timeit('fill_deque(100)', globals=globals(), number=100000))
print(timeit('pop_list(100)', globals=globals(), number=100000))
print(timeit('pop_deque(100)', globals=globals(), number=100000))
print(timeit('extend_list(100)', globals=globals(), number=100000))
print(timeit('extend_deque(100)', globals=globals(), number=100000))

# Скорости в данных операциях для list и deque примерно одинаковы, хотя deque оказался незначительно быстрее (на ~5%)

# appendleft, popleft, extendleft

def ap_left_list(n):
    for i in range(n):
        test_list.insert(0, i)


def ap_left_deque(n):
    for i in range(n):
        test_deque.appendleft(i)


def popleft_list(n):
    for i in range(n):
        test_list.pop(0)


def popleft_deque(n):
    for i in range(n):
        test_deque.popleft()


def exleft_list(n):
    for i in range(n):
        test_list.insert(0, [i, i + 1, i + 2])


def exleft_deque(n):
    for i in range(n):
        test_deque.extendleft([i, i + 1, i + 2])


print(timeit('ap_left_list(100)', globals=globals(), number=500))
print(timeit('ap_left_deque(100)', globals=globals(), number=100000))
print(timeit('popleft_list(100)', globals=globals(), number=500))
print(timeit('popleft_deque(100)', globals=globals(), number=100000))
print(timeit('exleft_list(100)', globals=globals(), number=500))
print(timeit('exleft_deque(100)', globals=globals(), number=100000))

# Эти три операции выполняются с deque намного быстрее, чем их аналоги с list, время на выполнение 100000 повторений
# с deque примерно равно 500 повторениям с list

# Получение элемента

def get_list(n):
    for i in range(n):
        p = test_list[i]


def get_deque(n):
    for i in range(n):
        p = test_deque[i]

print(timeit('get_list(1000)', globals=globals(), number=100000))
print(timeit('get_deque(1000)', globals=globals(), number=100000))

# Операция проходит быстрее со списком (2.2 сек против 3.0 сек). Документация не лжет, к списку более быстрый доступ,
# а в дек быстрее добавлять элементы в начало
