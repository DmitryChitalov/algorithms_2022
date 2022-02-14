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


# Сравниваю операции append, pop, extend
my_list = []
my_deque = deque()
for_extend = [1, 2, 3]


print('append_func(my_list)', timeit("""for i in range(100): my_list.append(1)""", globals=globals()))

print('pop_func(my_list)', timeit("""for i in range(100): my_list.pop()""", globals=globals()))

print('extend_func(my_list)', timeit("""for i in range(100): my_list.extend(for_extend)""", globals=globals()))
my_list.clear()

print('append_func(my_deque)', timeit("""for i in range(100): my_deque.append(1)""", globals=globals()))

print('pop_func(my_deque)', timeit("""for i in range(100): my_deque.pop()""", globals=globals()))

print('extend_func(my_deque)', timeit("""for i in range(100): my_deque.extend(for_extend)""", globals=globals()))
my_deque.clear()

# Результаты списка и дека почти одинаковые

for i in range(201):
    my_list.append(i)
    my_deque.append(i)

print('Получение элемента - list = ', timeit("""
for i in range(200):
    a = my_list[i]""", globals=globals()))

print('Получение элемента - deque = ', timeit("""
for i in range(200):
    a = my_deque[i]""", globals=globals()))
