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

list_1 = list('asdfWEFEkgkgkkk')
list_2 = deque(list_1)


def check_1(list_check):
    for i in range(5):
        list_check.append('elem')
    return list_check


def check_2(list_check):
    for i in range(5):
        list_check.pop()
    return list_check


def check_3(list_check):
    new_list = list('new')
    for i in range(5):
        list_check.extend(new_list)
    return list_check


def check_4(list_check):
    for i in range(5):
        list_check.insert(0, 'elem')
    return list_check


def check_5(list_check):
    for i in range(5):
        list_check.appendleft('elem')
    return list_check


def check_6(list_check):
    for i in range(5):
        list_check.pop(0)
    return list_check


def check_7(list_check):
    for i in range(5):
        list_check.popleft()
    return list_check


def check_8(list_check):
    new_list = list('new')
    for i in range(5):
        k = 0
        for elem in new_list[::-1]:
            list_check.insert(k, elem)
            k += 1
    return list_check


def check_9(list_check):
    new_list = list('new')
    for i in range(5):
        list_check.extendleft(new_list)
    return list_check


print('append list:',
      timeit(
          'check_1(list_1)',
          globals=globals()))

print('append deque:',
      timeit(
          'check_1(list_2)',
          globals=globals()))

print('pop list:',
      timeit(
          'check_2(list_1)',
          globals=globals()))

print('pop deque:',
      timeit(
          'check_2(list_2)',
          globals=globals()))

print('extend list:',
      timeit(
          'check_3(list_1)',
          globals=globals()))

print('extend deque:',
      timeit(
          'check_3(list_2)',
          globals=globals()))

# Вывод - методы append, pop и extend работают немного быстрее с deque и медленее с list
# Разница ощущается при большом количестве повторов

list_1 = list('easy-list')
list_2 = deque(list_1)

print('appendleft (insert) for list -:',
      timeit(
          'check_4(list_1)',
          number=10000,
          globals=globals()))

print('appendleft for deque -:',
      timeit(
          'check_5(list_2)',
          number=10000,
          globals=globals()))

print('popleft for list -:',
      timeit(
          'check_6(list_1)',
          number=10000,
          globals=globals()))

print('popleft for deque -:',
      timeit(
          'check_7(list_2)',
          number=10000,
          globals=globals()))

print('extendleft for list -:',
      timeit(
          'check_8(list_1)',
          number=1000,
          globals=globals()))

print('extendleft for deque -:',
      timeit(
          'check_9(list_2)',
          number=1000,
          globals=globals()))

# Вывод - методы appendleft, popleft, extendleft работают значительно быстрее с deque и медленее с list
