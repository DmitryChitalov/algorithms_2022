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

my_list = []
my_deque = deque()


def append_list():
    for i in range(10000):
        my_list.append(i)


def append_deque():
    for i in range(10000):
        my_deque.append(i)


def appendleft_deque():
    for i in range(10000):
        my_deque.appendleft(i)

    # my_deque.appendleft(i for i in range(1000))
def pop_list():
    for i in range(1000):
        my_list.pop()


def pop_deque():
    for i in range(1000):
        my_deque.pop()


def popleft_deque():
    for i in range(1000):
        my_deque.popleft()


def extend_list():
    my_list.extend(i for i in range(1000))


def extend_deque():
    my_deque.extend(i for i in range(1000))


def extendleft_deque():
    my_deque.extendleft(i for i in range(1000))


print(f'{"-" * 30}\nСкорость добавление элементов в очередь(deque) быстрее чем в список(list),\n'
      f'Разница между appendleft и append незначительна, но appendleft быстрее')
print(timeit("append_list()", globals=globals(), number=1000))
print(timeit("append_deque()", globals=globals(), number=1000))
print(timeit("appendleft_deque()", globals=globals(), number=1000))
print(f'{"-" * 30}\nСкорость удаления элементов в deque быстрее чем list,\n'
      f'Разница между appendleft и append незначительна, но append быстрее')
print(timeit("pop_list()", globals=globals(), number=1000))
print(timeit("pop_deque()", globals=globals(), number=1000))
print(timeit("popleft_deque()", globals=globals(), number=1000))
print(f'{"-" * 30}\nСкорость добавления элементов в list быстрее чем deque')
print(timeit("extend_list()", globals=globals(), number=1000))
print(timeit("extend_deque()", globals=globals(), number=1000))
print(timeit("extendleft_deque()", globals=globals(), number=1000))
print(f'{"-" * 30}\n')

