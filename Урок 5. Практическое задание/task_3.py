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
from timeit import timeit
from collections import deque

#  1

n = 1000
lst = []
lst_deque = deque()
lst_test = [i for i in range(100)]


def lst_append(num):
    for i in range(n):
        lst.append(i)


def deque_append(num):
    for i in range(n):
        lst_deque.append(i)


def pop_lst(num):
    for i in range(len(lst)):
        lst.pop()


def pop_deque(num):
    for i in range(len(lst_deque)):
        lst_deque.pop()


def extend_lst(num):
    for i in range(n):
        lst.extend(lst_test)


def extend_deque(num):
    for i in range(n):
        lst_deque.extend(lst_test)

print(f'Время выполнения функции lst_append = {timeit("lst_append(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции deque_append = {timeit("deque_append(n)", globals=globals(), number=1000)}')


# Время выполнения функции lst_append = 0.076634
# Время выполнения функции deque_append = 0.06123430000000002

print(len(lst), len(lst_deque))
print(f'Время выполнения функции pop_lst = {timeit("pop_lst(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции pop_deque = {timeit("pop_deque(n)", globals=globals(), number=1000)}')
print(len(lst), len(lst_deque))

#  Время выполнения функции pop_lst = 0.05902379999999999
#  Время выполнения функции pop_deque = 0.0633126


print(f'Время выполнения функции extend_lst = {timeit("extend_lst(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции extend_deque = {timeit("extend_deque(n)", globals=globals(), number=1000)}')

#  Время выполнения функции extend_lst = 3.0347542
#  Время выполнения функции extend_deque = 1.3669271999999997

pop_lst(n)
pop_deque(n)


# операции append и pop списка и дека выполняются практически за одинаковое время, операция extend в деке заметно быстрее

#  2

def lst_append_left(num):
    for i in range(n):
        lst.insert(0, i)


def deque_append_left(num):
    for i in range(n):
        lst_deque.appendleft(i)


def pop_left_lst(num):
    for i in range(len(lst)):
        lst.pop(0)


def pop_left_deque(num):
    for i in range(len(lst_deque)):
        lst_deque.popleft()


def extend_left_lst(num):
    for i in range(n):
        lst.insert(0, lst_test)


def extend_left_deque(num):
    for i in range(n):
        lst_deque.extendleft(lst_test)


print(len(lst), len(lst_deque))
print(f'Время выполнения функции lst_append_left = {timeit("lst_append_left(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции deque_append_left = {timeit("deque_append_left(n)", globals=globals(), number=100)}')
print(len(lst), len(lst_deque))

# значения при number=1000
# Время выполнения функции lst_append_left = 511.27046469999993
# Время выполнения функции deque_append_left = 0.06348060000004807
# значения при number = 100
# Время выполнения функции lst_append_left = 2.1979003000000006
# Время выполнения функции deque_append_left = 0.006549299999999647
print(f'Время выполнения функции pop_left_lst = {timeit("pop_left_lst(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции pop_left_deque = {timeit("pop_left_deque(n)", globals=globals(), number=1000)}')
print(len(lst), len(lst_deque))

# Время выполнения функции pop_left_lst = 1.1151693999999992
# Время выполнения функции pop_left_deque = 0.006914699999999385

print(f'Время выполнения функции extend_left_lst = {timeit("extend_left_lst(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции extend_left_deque = {timeit("extend_left_deque(n)", globals=globals(), number=100)}')

# Время выполнения функции extend_left_lst = 2.084512799999999
# Время выполнения функции extend_left_deque = 0.13187740000000048

# скорость выполнения операций appendleft popleft и extendleft с деком в несколько раз превосходят работу со списками

pop_lst(n)
pop_deque(n)
lst_append(n)
deque_append(n)

# 3
def get_lst(num):
    for i in range(n):
        lst[i] = i


def get_lst_deque(num):
    for i in range(n):
        lst_deque[i] = i


print(len(lst), len(lst_deque))
print(f'Время выполнения функции get_lst = {timeit("get_lst(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции get_lst_deque = {timeit("get_lst_deque(n)", globals=globals(), number=1000)}')
print(len(lst), len(lst_deque))

# Время выполнения функции get_lst = 0.043168600000001334
# Время выполнения функции get_lst_deque = 0.05762049999999874

# получение элемента списка и дека у списков происходит быстрее