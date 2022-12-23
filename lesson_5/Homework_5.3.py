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


some_lst = [i for i in range(1000)]
some_deque = deque([i for i in range(1000)])

print('Заполнение:')
print('Обычный список -', timeit(f'{[i for i in range(10 ** 3)]}', globals=globals(), number=10**5))
print('-'*100)
print('Deque - ', timeit(f'deque({[i for i in range(10 ** 3)]})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 0.1503240999954869
----------------------------------------------------------------------------------------------------
Deque -  0.5890656999981729
----------------------------------------------------------------------------------------------------
Deque медленнее
"""


def pop_smth(lst_or_deque):
    for i in range(1000):
        lst_or_deque.pop()
    return lst_or_deque


print('Удаление:')
print('Обычный список -', timeit(f'pop_smth({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'pop_smth({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 3.659404199999699
----------------------------------------------------------------------------------------------------
Deque 3.8117654000016046
----------------------------------------------------------------------------------------------------
Значительной разницы нет
"""


def append_smth(lst_or_deque):
    for i in range(1000):
        lst_or_deque.append(i)
    return lst_or_deque


print('Добавление:')
print('Обычный список -', timeit(f'append_smth({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'append_smth({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 4.016290100000333
----------------------------------------------------------------------------------------------------
Deque 4.73362189999898
----------------------------------------------------------------------------------------------------
Deque чуть медленнее
"""


def extend_smth(lst_or_deque):
    for i in range(1000):
        lst_or_deque.extend([1, 2, 3])
    return lst_or_deque


print('Дополнение:')
print('Обычный список -', timeit(f'extend_smth({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'extend_smth({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 8.230585299999802
----------------------------------------------------------------------------------------------------
Deque 11.126517900003819
----------------------------------------------------------------------------------------------------
Deque медленнее
"""


def appendleft_list(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_deque(dqe):
    for i in range(1000):
        dqe.appendleft(i)
    return dqe


print('AppendLeft:')
print('Обычный список -', timeit(f'appendleft_list({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'appendleft_deque({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 47.400774199995794
----------------------------------------------------------------------------------------------------
Deque 4.6743306999997
----------------------------------------------------------------------------------------------------
Deque ЗНАЧИТЕЛЬНО быстрее
"""


def popleft_list(lst):
    for i in range(1000):
        lst.pop(0)
    return lst


def popleft_deque(dqe):
    for i in range(1000):
        dqe.popleft()
    return dqe


print('PopLeft:')
print('Обычный список -', timeit(f'popleft_list({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'popleft_deque({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 10.562002099999518
----------------------------------------------------------------------------------------------------
Deque 3.818671399996674
----------------------------------------------------------------------------------------------------
Deque ЗНАЧИТЕЛЬНО быстрее
"""


def extendleft_list(lst):
    for i in range(1000):
        lst.insert(0, [1, 2, 3])
    return lst


def extendleft_deque(dqe):
    for i in range(1000):
        dqe.extendleft([1, 2, 3])
    return dqe


print('Extendleft:')
print('Обычный список -', timeit(f'extendleft_list({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'extendleft_deque({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 54.101555199995346
----------------------------------------------------------------------------------------------------
Deque 11.066942299999937
----------------------------------------------------------------------------------------------------
Deque ЗНАЧИТЕЛЬНО быстрее
"""


def get_element(lst_or_deque):
    for i in range(1000):
        lst_or_deque[i] = i
    return lst_or_deque


print('Получение элемента:')
print('Обычный список -', timeit(f'get_element({some_lst})', globals=globals(), number=10**5))
print('-'*100)
print('Deque', timeit(f'get_element({some_deque})', globals=globals(), number=10**5))
print('-'*100)
print()
"""
Результаты:
Обычный список - 2.885551999999734
----------------------------------------------------------------------------------------------------
Deque 5.074556300001859
----------------------------------------------------------------------------------------------------
Deque медленнее
"""
"""
Выводы:
Если нет необходимости использовать методы deque 
(appendleft, popleft, extendleft), использовать deque нецелесообразно.
"""